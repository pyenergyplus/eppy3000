"""testing print E+ Munch"""

from munch import Munch
from eppy3000.readidf import readidfjson

fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
idf = readidfjson(fname)

for key, val in idf.items():
    print()
    print()
    print(key)
    if isinstance(val, Munch):
        for key1, val1 in val.items():
            print()
            print('    {0: <36} !-  {1} {2}'.format(key1, key, 'NAME'))
            if isinstance(val1, Munch):
                for key2, val2 in val1.items():
                    if isinstance(val2, (Munch, list)):
                        print('        {0}'.format(key2))
                    else:
                        print('        {0: <32} !-  {1}'.format(val2, key2))
            else:
                print('*'*8, val1)
    else:
        print('*'*8, val)


