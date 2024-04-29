"""code to generate dbm (Energy+.schema.epJSON) of multiple version of Energyplu"""

from eppy3000.dbm_functions import json2dbm


def make_createall_in_verfolder(fname, outer_folder, justdbmname):
    try:
        result = json2dbm.createall_in_verfolder(fname, outer_folder, justdbmname)
        print(f"dbm created in {result}")
    except FileExistsError as e:
        print(f"The dbm for {fname} has already been created")

fnames = []
fname = "/Applications/EnergyPlus-22-1-0/Energy+.schema.epJSON"
fnames.append(fname)
fname = "/Applications/EnergyPlus-9-6-0/Energy+.schema.epJSON"
fnames.append(fname)
outer_folder = "../AllEplusDBM"
justdbmname = None

for fname in fnames:
    make_createall_in_verfolder(fname, outer_folder, justdbmname)

