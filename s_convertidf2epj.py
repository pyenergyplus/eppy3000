"""convert idf to epj"""

from eppy3000 import idfjsonconverter


fname = "/Users/santoshphilip/Documents/coolshadow/github/eppy3000/eppy3000/resources/snippets/V22_1/Minimal.idf"

epjpath = f"{fname[:-3]}epJSON"
idfjsonconverter.idffile2epjfile(fname)
