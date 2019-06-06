"""convertion functions - to convert from JSON to IDF and in reverse."""

import json
from munch import Munch
from itertools import zip_longest

from eppy3000 import rawidf


def readiddasmunch(fhandle):
    """read the idd json as a munch"""
    epjs = json.load(fhandle)
    as_munch = Munch.fromDict(epjs)
    return as_munch

def num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError as e:
            return s

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)



def keymapping(somekeys, allkeys):
    """map the keys regardless of case"""
    allkeys = list(allkeys)
    somekeys = list(somekeys)
    ll1 = [i.upper() for i in allkeys]
    ll2 = [i.upper() for i in somekeys]
    mapping = [(i, ll1.index(val)) for i, val in enumerate(ll2)]
    return {somekeys[i]:allkeys[j] for i, j in mapping}

def idf2json(idfhandle, epjsonhandle):
    """convert idf2json"""
    raw_idf = rawidf.readrawidf(idfhandle)
    js = readiddasmunch(epjsonhandle)
    idfobjcount = {}
    idfjson = {}
    keys = raw_idf.keys()
    order = 0
    mapping = keymapping(raw_idf.keys(), js.properties.keys())
    # mapping in case the case does not match between keys
    for akey in keys:
        key = mapping[akey]
        count = idfobjcount.setdefault(key, 0)
        dct = idfjson.setdefault(key, dict())
        fieldnames = js.properties[key].legacy_idd.fields
        idfobjects = raw_idf[akey]
        for idfobject in idfobjects:
            idfobjcount[key] = idfobjcount[key] + 1
            order += 1
            try:
                if fieldnames[0] == 'name':
                    alst = {fieldname:idfvalue for idfvalue, fieldname in
                                        zip(idfobject[2:], fieldnames[1:])}
                    idfobjectname = idfobject[1]
                else:
                    alst = {fieldname:idfvalue for idfvalue, fieldname in
                                            zip(idfobject[1:], fieldnames)}
                    idfobjectname = f"{key} {idfobjcount[key]}"
            except IndexError as e:
                alst = {fieldname:idfvalue for idfvalue, fieldname in
                                        zip(idfobject[1:], fieldnames)}
                idfobjectname = f"{key} {idfobjcount[key]}"
            alst["idf_order"] = order
            numericfields = js.properties[key].legacy_idd.numerics.fields
            for fieldkey in alst.keys():
                if fieldkey in numericfields:
                    alst[fieldkey] = num(alst[fieldkey])

            try:
                extension = js.properties[key].legacy_idd.extension
                extensibles = js.properties[key].legacy_idd.extensibles
                endvalues = idfobject[len(fieldnames) + 1:]
                g_endvalues = grouper(endvalues, len(extensibles))
                extvalues = [{f:t for f, t in zip(extensibles, tup)}
                                            for tup in g_endvalues]

                try:
                    e_numericfields = js.properties[key].legacy_idd.numerics.extensions
                    for e_dct in extvalues:
                        for e_key in e_dct:
                            if e_key in e_numericfields:
                                e_dct[e_key] = num(e_dct[e_key])
                except AttributeError as e:
                    pass

                alst[extension] = extvalues
            except AttributeError as e:
                pass
            dct.update({idfobjectname:alst})
    return json.dumps(idfjson, indent=2)

def json2idf(jsonhandle, epjsonhandle):
    """convert JSON to IDF"""
    lines = []
    js = readiddasmunch(epjsonhandle)
    idfjs = readiddasmunch(jsonhandle)

    for key in idfjs.keys():
        for name in idfjs[key].keys():
            fieldval = []
            fieldnames = js.properties[key].legacy_idd.fields
            lastfield = len(fieldnames) - 1
            comma = ","
            semicolon = ";"
            sep = comma
            for i, fieldname in enumerate(fieldnames):
                if i == lastfield:
                    sep = semicolon
                try:
                    value = idfjs[key][name][fieldname]
                    fieldval.append((fieldname, value))
                except KeyError as e:
                    if fieldname == 'name':
                        fieldval.append((fieldname, name))
                    else:
                        value = None
                        fieldval.append((fieldname, value))


            try:
                extension = js.properties[key].legacy_idd.extension
                extensibles = js.properties[key].legacy_idd.extensibles
                for i, tup in enumerate(idfjs[key][name][extension]):
                    for fld in extensibles:
                        fieldval.append((f"{fld} {i + 1}", tup[fld]))
            except AttributeError as e:
                pass
            fieldval = [(fld, val) for fld, val in fieldval if val != None]
            lastfield = len(fieldval) - 1
            sep = comma
            lines.append(f"{key},")
            for i, (fld, val) in enumerate(fieldval):
                if i == lastfield:
                    sep = semicolon
                valsep = f"{val}{sep}"
                lines.append(f"    {valsep:<25} !- {fld}")
            lines.append("")

    return "\n".join(lines)
