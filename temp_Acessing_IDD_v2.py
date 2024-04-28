"""Recreate the steps in the online docs:

https://eppy3000.readthedocs.io/en/latest/usage.html#Accessing-the-IDD

using schema from dbm


Now code this to use multiple IDD versions.
"""

from eppy3000.modelmaker import EPJ

epschemaname = "/Applications/EnergyPlus-9-6-0/Energy+.schema.epJSON"
fname = "eppy3000/resources/snippets/V9_6/1ZoneDataCenterCRAC_wPumpedDXCoolingCoil.epJSON"
schemadbmname = "../AllEplusDBM/9.6/schema"
epj = EPJ(epjname=fname, epschemaname=epschemaname, schemadbmname=schemadbmname, dbm_cache=True)
aloops =  epj.epobjects['AirLoopHVAC']
aloop =  aloops[0]
# print(aloop)


fieldnames = epj.epschema.epschemaobjects['AirLoopHVAC'].fieldnames()
# print(fieldnames)

# print(f"{type(aloop)=}")
fieldnames = aloop.dbmfieldnames()
# print(fieldnames)
fieldprop = aloop.dbmfieldproperty("branch_list_name")
# print(fieldprop)

print(f"{epj.alldbms['9.6'].keys()=}")
zone = epj.epobjects["Zone"][0]
fieldprop = zone.dbmfieldproperty("direction_of_relative_north")

print(f"{epj.alldbms['9.6'].keys()=}")
print(f"{epj.alldbms.keys()=}")
# print(fieldprop)
# 
# versions = epj.epobjects["Version"][0]
# print(versions)

# 

fname1 = "eppy3000/resources/snippets/V22_1/Minimal.epJSON"
schemadbmname1 = "../AllEplusDBM/22.1/schema"
epj1 = EPJ(epjname=fname1, epschemaname=epschemaname, schemadbmname=schemadbmname1, dbm_cache=True)
print(f"{epj.alldbms.keys()=}")
print(f"{epj1.alldbms.keys()=}")
print(f"{epj.alldbms['9.6'].keys()=}")
print(f"{epj.alldbms['22.1'].keys()=}")
