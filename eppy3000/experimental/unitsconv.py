# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""function to extract the units of the fields and to do unit conversions"""

import eppy3000.experimental.conversiondata as conversiondata

def getfieldunits(epobject, fieldname):
    try:
        return epobject.eppy_objepschema[fieldname]['units']
    except KeyError as e:
        return None
        
def getarrayfieldunits(epobject, arrayname, itemname):
    try:
        return epobject.eppy_objepschema[arrayname]['items']['properties'][itemname]['units']
    except KeyError as e:
        return None
        

def getfield_ipunits(epobject, fieldname):
    try:
        return epobject.eppy_objepschema[fieldname]['ip-units']
    except KeyError as e:
        return None

def getarrayfield_ipunits(epobject, arrayname, itemname):
    try:
        return epobject.eppy_objepschema[arrayname]['items']['properties'][itemname]['ip-units']
    except KeyError as e:
        return None
        
def getconvert_factors(epobject, fieldname):
    """return new units, convertion_factors"""
    units = getfieldunits(epobject, fieldname)
    ipunits = getfield_ipunits(epobject, fieldname)
    return unitconversiondata(units, ipunits)
    
def fieldisarray(epobject, fieldname):
    """returns True if the field is an array"""
    try:
        if epobject.eppy_objepschema[fieldname]['type'] == 'array':
            return True
        else: 
            return False
    except KeyError as e:
        return False
        
def getarraykeys(epobject, arrayname):
    """return the item names in the array"""
    if fieldisarray(epobject, arrayname):
        result =  list(epobject.eppy_objepschema[arrayname]['items']['properties'].keys())
        return result
    else:
        return []

    
def getarrayconvert_factors(epobject, arrayname):
    """if the field an array, return new units, convertion_factors of items in array """
    convert_factors = []
    for itemname in getarraykeys(epobject, arrayname):
        units = getarrayfieldunits(epobject, arrayname, itemname)
        ipunits = getarrayfield_ipunits(epobject, arrayname, itemname)
        convert_factors.append(unitconversiondata(units, ipunits))
    return convert_factors
        
def unitconversiondata(units, ipunits=None):
    """given the units and ip_units, get the conversiondata for the units"""
    si, ip = conversiondata.getconversions()
    try:
        dctval = si[units]
        if not ipunits:
            convval = dctval[0]
        else:
            dct = dict(dctval)
            convval = (ipunits, dct[ipunits])
    except KeyError as e:
        dctval = None
        convval = None
    return units, convval
    
def getconversiondata(units, ipunits=None):
    """given the units and ip_units, get the conversiondata for the units"""
    si, ip = conversiondata.getconversions()
    if (not units) and (not ipunits):
        return None
    try:
        dctval = si[units]
        if not ipunits:
            convval = dctval[0]
        else:
            dct = dict(dctval)
            convval = (ipunits, dct[ipunits])
    except KeyError as e:
        dctval = None
        convval = (units, None)
    return convval

def convertfield(epobject, fieldname):
    """return converted value and units"""
    pass
    
def add(a, b):
    return a + b
    
def doconversions(val, units, conv):
    if units:
        try:
            ustr = f"[{conv[0]}]"
            convfactor = conv[1]
            newval = val * convfactor
        except TypeError as e:
            newval = val
            ustr = ""
    else:
        newval = val
        ustr = ""
    return newval, ustr

def do_noconversions(val, units):
    """do no conversions"""
    newval = val
    if not units:
        ustr = ""
    else:
        ustr = f"[{units}]" 
    return newval, ustr      
    

def do_conversions(val, conv):
    if not conv:
        ustr = ""
        newval = val
    else:
        new_units, factor = conv
        if factor == ['1.8', '(plus', '32)']:
            try:
                newval = val * 1.8 + 32
            except TypeError as e:
                newval = val
        else:
            try:
                newval = val * factor
            except TypeError as e:
                newval = val
        ustr = f"[{new_units}]"
    return newval, ustr

    
# from
# https://stackoverflow.com/questions/9640109/allign-left-and-right-in-python
def align_left_right(left: str, right: str, total_len: int = 80) -> str:
    left_size = max(0, total_len - len(right) - 1)  # -1 to account for the space
    return format(left, f"<{left_size}") + " " + right

    