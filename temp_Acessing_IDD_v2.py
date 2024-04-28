"""Recreate the steps in the online docs:

https://eppy3000.readthedocs.io/en/latest/usage.html#Accessing-the-IDD

using schema from dbm


Now code this to use multiple IDD versions.
"""

from eppy3000.modelmaker import EPJ

epschemaname = "/Applications/EnergyPlus-9-6-0/Energy+.schema.epJSON"
fname = "eppy3000/resources/snippets/V9_6/1ZoneDataCenterCRAC_wPumpedDXCoolingCoil.epJSON"
schemadbmname = "../EplusSchema/schema"
epj = EPJ(epjname=fname, epschemaname=epschemaname, schemadbmname=schemadbmname, dbm_cache=False)
aloops =  epj.epobjects['AirLoopHVAC']
aloop =  aloops[0]
print(aloop)


fieldnames = epj.epschema.epschemaobjects['AirLoopHVAC'].fieldnames()
print(fieldnames)

fieldnames = aloop.dbmfieldnames()
print(fieldnames)
fieldprop = aloop.dbmfieldproperty("branch_list_name")
print(fieldprop)
zone = epj.epobjects["Zone"][0]
fieldprop = zone.dbmfieldproperty("direction_of_relative_north")
print(fieldprop)

versions = epj.epobjects["Version"][0]
print(versions)
