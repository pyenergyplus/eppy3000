# Slightly different from how BOX works in
# https://github.com/cdgriffith/Box/wiki/Quick-Start#access-boxes-inside-lists

from munch import Munch

my_box = Munch.fromDict({"team": {"red": {"leader": "Sarge", "members": []}}})
# see doc for fromDict at bottome of email
print(my_box.team.red.leader)
# Sarge

my_box.team.blue = Munch({"leader": "Church", "members": []})

print(repr(my_box.team.blue))
# Munch({'leader': 'Church', 'members': []})

my_box.team.red.members = [
    Munch({"name": "Grif", "rank": "Minor Junior Private Negative First Class"}),
    Munch({"name": "Dick Simmons", "rank": "Captain"}),
]

print(my_box.team.red.members[0].name)
# Grif


# reading epJSON
import json
from munch import Munch
from io import StringIO

txt = """{
    "Version": {
        "Version 1": {
            "version_identifier": "9.3",
            "idf_order": 1
        }
    },
    "SimulationControl": {
        "SimulationControl 1": {
            "do_zone_sizing_calculation": "Yes",
            "do_system_sizing_calculation": "Yes",
            "do_plant_sizing_calculation": "Yes",
            "run_simulation_for_sizing_periods": "No",
            "run_simulation_for_weather_file_run_periods": "Yes",
            "idf_order": 2
        }
    },
    "Building": {
        "Empire State Building": {
            "north_axis": 30,
            "terrain": "City",
            "loads_convergence_tolerance_value": 0.04,
            "temperature_convergence_tolerance_value": 0.4,
            "solar_distribution": "FullExterior",
            "maximum_number_of_warmup_days": 25,
            "minimum_number_of_warmup_days": 6,
            "idf_order": 3
        }
    },
    "Site:Location": {
        "CHICAGO_IL_USA TMY2-94846": {
            "latitude": 41.78,
            "longitude": -87.75,
            "time_zone": -6,
            "elevation": 190,
            "idf_order": 4
        }
    }
}"""
# filepath = "./eppy3000/resources/epJSON/V9_3/smallfile.epJSON"
# with open(filepath, "r") as fhandle:
with StringIO(txt) as fhandle:
    as_json = json.load(fhandle)
    as_munch = Munch.fromDict(as_json)
# You can do the same for schema

print(as_munch.Version)
# Munch({'Version 1': Munch({'version_identifier': '9.3', 'idf_order': 1})})

print(Munch.fromDict.__doc__)
#  Recursively transforms a dictionary into a Munch via copy.
#
#             >>> b = Munch.fromDict({'urmom': {'sez': {'what': 'what'}}})
#             >>> b.urmom.sez.what
#             'what'
#
#             See munchify for more info.
#


import munch

print(munch.munchify.__doc__)
#  Recursively transforms a dictionary into a Munch via copy.
#
#         >>> b = munchify({'urmom': {'sez': {'what': 'what'}}})
#         >>> b.urmom.sez.what
#         'what'
#
#         munchify can handle intermediary dicts, lists and tuples (as well as
#         their subclasses), but ymmv on custom datatypes.
#
#         >>> b = munchify({ 'lol': ('cats', {'hah':'i win again'}),
#         ...         'hello': [{'french':'salut', 'german':'hallo'}] })
#         >>> b.hello[0].french
#         'salut'
#         >>> b.lol[1].hah
#         'i win again'
#
#         nb. As dicts are not hashable, they cannot be nested in sets/frozensets.
