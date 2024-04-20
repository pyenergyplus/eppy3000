"""Recreate the steps in the online docs:

https://eppy3000.readthedocs.io/en/latest/usage.html#Accessing-the-IDD

using schema from dbm"""

from eppy3000.modelmaker import EPJ

epschemaname = "/Applications/EnergyPlus-9-6-0/Energy+.schema.epJSON"
fname = "eppy3000/resources/snippets/V9_6/1ZoneDataCenterCRAC_wPumpedDXCoolingCoil.epJSON"
schemadbmname = "../EplusSchema/schema"
epj = EPJ(epjname=fname, epschemaname=epschemaname, schemadbmname=schemadbmname, dbm_cache=False)
aloops =  epj.epobjects['AirLoopHVAC']
aloop =  aloops[0]
print(aloop)

# You can also access the IDD for an IDF object from within the IDF object:

fieldnames = epj.epschema.epschemaobjects['AirLoopHVAC'].fieldnames()
print(fieldnames)

print()
print(f"{type(aloops)=}")
print(f"{type(aloop)=}")
# theepj = aloops.theepj
# print(f"{type(theepj)=}")
print(f"{type(epj)=}")
# print(f"{dir(aloop)=}")
print(f"{type(aloop.eppy_epj)=}")
# print(f"{dir(aloop.eppy_epj)=}")
# with dbm
# aloopschema = aloop.eppydbm()
# print(f"{aloopschema=}")
# fieldnames = aloop.eppy_dbm().fieldnames()
fieldnames = aloop.dbmfieldnames()
print(fieldnames)
fieldprop = aloop.dbmfieldproperty("branch_list_name")
# print(fieldprop)
print(f"{aloop.eppy_epj.dbmdct.keys()=}")
zone = epj.epobjects["Zone"][0]
# fieldnames = zone.dbmfieldnames()
# print(fieldnames)
fieldprop = zone.dbmfieldproperty("direction_of_relative_north")
print(fieldprop)
print(f"{zone.eppy_epj.dbmdct.keys()=}")

