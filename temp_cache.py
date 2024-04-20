"""test out the dbm cache in EPJ"""

from eppy3000.modelmaker import EPJ

fname = "eppy3000/resources/snippets/V9_6/1ZoneDataCenterCRAC_wPumpedDXCoolingCoil.epJSON"
schemadbmname = "../EplusSchema/schema"
epj1 = EPJ(epjname=fname, schemadbmname=schemadbmname)
epj2 = EPJ(epjname=fname, schemadbmname=schemadbmname)
print(f"{epj1.dbmdct=}")
epj1.dbmdct.update(dict(a=1, b=2))
print(f"{epj1.dbmdct=}")
print(f"{epj2.dbmdct=}")
