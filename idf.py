"""use the class IDF"""

from eppy3000.modelmaker import IDF

fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
idf = IDF(fname)

print(idf.idfobjects['AirLoopHVAC'][0])
# print(idf)

# idf.saveas('karamba.txt')
# idfobjects = {key:[val1 for val1 in val.values()] for key, val in idf.idf.items()}