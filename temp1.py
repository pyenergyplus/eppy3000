"""develop the run functions here"""

import eppy

# Make an epJSON file
# fname = "./eppy3000/resources/snippets/V9_3/Minimal.idf"
# wfile = "./eppy3000/resources/weatherfiles/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
# idf = eppy.openidf(fname, epw=wfile)
#
# import eppy3000.oldeppy as oldeppy
# epschema = './eppy3000/resources/schema/V9_3/Energy+.schema.epJSON'
# epj = oldeppy.idf2epj(idf, open(epschema, 'r'))
# epj.saveas("a.epj")
# print(dir(epj))
# print(epj.epw)

from eppy3000.modelmaker import EPJ

# import eppy3000.runner.run_functions as run_functions


fname = "./eppy3000/resources/snippets/V9_3/Minimal.epJSON"
wfile = "./eppy3000/resources/weatherfiles/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
epschema = "./eppy3000/resources/schema/V9_3/Energy+.schema.epJSON"
epj = EPJ(fname, epw=wfile, epschemaname=epschema)
# run_functions.run(epj, output_suffix="D", output_prefix="gumby")
epj.run()
