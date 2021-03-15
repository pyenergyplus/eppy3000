# Copyright (c) 2019-2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""convertion functions - to convert from JSON to IDF and in reverse."""

import json
from itertools import zip_longest

from eppy3000 import rawidf
from eppy3000.epschema import read_epschema_asmunch
from eppy3000 import installlocation


def num(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
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
    return {somekeys[i]: allkeys[j] for i, j in mapping}


def idf2json(idfhandle, epjsonhandle):
    """converts the E+ file in the old IDF format to the new JSON format

    Parameters
    ----------
    jsonhandle: io.TextIOWrapper, io.StringIO
        This is the E+ file in the old IDF format
    epjsonhandle: io.TextIOWrapper, io.StringIO
        This is the epjson file (eqv. of the IDD file in the old format)

    Returns
    -------
    str
        E+ file in the new JSON format
    """
    raw_idf = rawidf.readrawidf(idfhandle)
    js = read_epschema_asmunch(epjsonhandle)
    idfobjcount = {}
    idfjson = {}
    keys = raw_idf.keys()
    order = 0
    mapping = keymapping(raw_idf.keys(), js.properties.keys())
    # mapping in case the case does not match between keys
    for akey in keys:
        key = mapping[akey]
        idfobjcount.setdefault(key, 0)
        dct = idfjson.setdefault(key, dict())
        fieldnames = js.properties[key].legacy_idd.fields
        idfobjects = raw_idf[akey]
        for idfobject in idfobjects:
            idfobjcount[key] = idfobjcount[key] + 1
            order += 1
            try:
                if fieldnames[0] == "name":
                    alst = {
                        fieldname: idfvalue
                        for idfvalue, fieldname in zip(idfobject[2:], fieldnames[1:])
                    }
                    idfobjectname = idfobject[1]
                else:
                    alst = {
                        fieldname: idfvalue
                        for idfvalue, fieldname in zip(idfobject[1:], fieldnames)
                    }
                    idfobjectname = f"{key} {idfobjcount[key]}"
            except IndexError as e:
                # catches "if fieldnames[0] == 'name':" when fieldnames = []
                alst = {
                    fieldname: idfvalue
                    for idfvalue, fieldname in zip(idfobject[1:], fieldnames)
                }
                idfobjectname = f"{key} {idfobjcount[key]}"
            alst["idf_order"] = order
            numericfields = js.properties[key].legacy_idd.numerics.fields
            for fieldkey in alst.keys():
                if fieldkey in numericfields:
                    alst[fieldkey] = num(alst[fieldkey])

            try:
                extension = js.properties[key].legacy_idd.extension
                extensibles = js.properties[key].legacy_idd.extensibles
                endvalues = idfobject[len(fieldnames) + 1 :]
                g_endvalues = grouper(endvalues, len(extensibles))
                extvalues = [
                    {f: t for f, t in zip(extensibles, tup)} for tup in g_endvalues
                ]

                try:
                    legacyidd = js.properties[key].legacy_idd
                    e_numericfields = legacyidd.numerics.extensions
                    for e_dct in extvalues:
                        for e_key in e_dct:
                            if e_key in e_numericfields:
                                # fxing bug and debugging here
                                # print(e_key)
                                # print(e_dct)
                                # e_dct[e_key] = num(e_dct[e_key])
                                # if e_dct[e_key] != None:
                                if e_dct[e_key]: # will skip None and '' ->maybe make sure of this
                                    e_dct[e_key] = num(e_dct[e_key])
                except AttributeError as e:
                    pass

                alst[extension] = extvalues
            except AttributeError as e:
                pass
            dct.update({idfobjectname: alst})
    return json.dumps(idfjson, indent=2)


def json2idf(jsonhandle, epjsonhandle):
    """converts the E+ file new JSON format to the old IDF format

    Parameters
    ----------
    jsonhandle: io.TextIOWrapper, io.StringIO
        This is the E+ file in the new JSON format
    epjsonhandle: io.TextIOWrapper, io.StringIO
        This is the epjson file (eqv. of the IDD file in the old format)

    Returns
    -------
    str
        E+ file in the old IDF format
    """
    lines = []
    js = read_epschema_asmunch(epjsonhandle)
    idfjs = read_epschema_asmunch(jsonhandle)

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
                    if fieldname == "name":
                        fieldval.append((fieldname, name))
                    else:
                        value = None
                        # debugging here
                        # fieldval.append((fieldname, value))
                        fieldval.append((fieldname, ''))
            try:
                extension = js.properties[key].legacy_idd.extension
                extensibles = js.properties[key].legacy_idd.extensibles
                for i, tup in enumerate(idfjs[key][name][extension]):
                    for fld in extensibles:
                        # debugging going on here
                        # print(fld)
                        # print(tup)
                        try:
                            fieldval.append((f"{fld} {i + 1}", tup[fld]))
                        except KeyError as e:
                            fieldval.append((f"{fld} {i + 1}", ''))
                        # fieldval.append((f"{fld} {i + 1}", tup[fld]))
            except AttributeError as e:
                pass
            fieldval = [(fld, val) for fld, val in fieldval if val is not None]
            # remove trailing blanks
            fieldval = removetrailingblanks(fieldval)
            # fieldval.reverse()
            # fieldval = [for first, second, in fieldval, if second]
            
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


def getidfversion(fhandle):
    """get the idf version of this file"""
    foundword_version = False
    lines = []
    for line in fhandle:
        cline = line.split('!')[0]
        if foundword_version:
            if ";"  in cline:
                remains = cline.split(";")[0]
                lines.append(remains)
                break
            else:
                lines.append(cline.strip())
        else:
            if "VERSION" in cline.upper():
                foundword_version = True
                fromversion = cline[cline.upper().find("VERSION"):].strip()
                if ";" in fromversion:
                    vline = fromversion.split(";")[0]
                    version = vline.split(",")[1].strip()
                    return version
                else:
                    lines.append(fromversion)
    compose = ''.join(lines)
    if compose:
        return compose.split(",")[1].strip()
    else:
        return None
        
def idffile2epjfile(idfpath, epjpath=None):
    """convert an IDF file on disk to an EPJ file on disk"""
    with open(idfpath, 'r') as idfhandle:
        version = getidfversion(idfhandle)
    schemapath = installlocation.schemapath(version)
    schemahandle = open(schemapath, 'r')
    idfhandle = open(idfpath, 'r')
    epjhandle = open(epjpath, 'w')
    epjtxt = idf2json(idfhandle, schemahandle)


def removetrailingblanks(lst):
    """remove railing blanks in lst
    lst = [(a, b), (a, ''), (b, c), (d, ''), (e, '')]
    return [(a, b), (a, ''), (b, c)]"""
    lst.reverse()
    new_lst = []
    trailing = True
    for fst, snd in lst:
        if trailing:
            if snd != '':
                new_lst.append((fst, snd))
                trailing = False
            else:
                pass
        else:
            new_lst.append((fst, snd))
    new_lst.reverse()
    return new_lst
    

# def f_getidfversion(fhandle):
#     """functional version of getidfversion - an attempt"""
#
#     def aux(lines):
#         for line in lines:
#             cline = line.split('!')[0]
#             if not acc:
#                 if "VERSION" in cline.upper():
#                     if ";" in cline:
#                         version = cline.split(",")[1].strip()
#                         return None
#                     else:
#                         acc.append(cline.strip())
#                 else: pass
#             else:
#                 if ";" in cline:
#                     remains = cline.split(";")[0]
#                     acc.append(remains)
#                     break
#
#     acc = []
#     return aux(fhandle)
#     # what = sum([aux(line.split('!')[0], acc) for line in fhandle if ])
#     return what
    
    # links to figure this out. Look into
    #
    # itertools.takewhile()
    # https://stackoverflow.com/questions/9572833/using-break-in-a-list-comprehension
    #
    # from itertools import ifilter
    # https://www.daniweb.com/programming/software-development/threads/293381/break-a-list-comprehension
    #
    # from itertools import takewhile
    # from functools import partial
    # https://www.reddit.com/r/learnpython/comments/7r3q1a/break_out_of_list_comprehension/
    #