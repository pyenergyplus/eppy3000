"""open and save a file"""

import eppy
fname = "/Users/santoshphilip/Documents/coolshadow/github/eppy3000/Generators_eppy3000"
fname = "/Users/santoshphilip/Documents/coolshadow/github/eppy3000/g_eppy3000"
# fname = "/Users/santoshphilip/Documents/coolshadow/github/eppy3000/Generators"
idf = eppy.openidf(f'{fname}.idf')
idf.saveas(f'{fname}_s.idf')