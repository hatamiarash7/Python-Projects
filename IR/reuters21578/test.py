import random


a = {k: random.random() for k in range(100)}
DFTF = open('DFTF.txt', 'wb')
DFTF.write("{: >15} {: >20} {: >15}\n\n".format('ID', 'TOKEN', 'DFTF'))

b = ""
for key, value in a.items():
    b += str(key) + ':' + str(value) + ' '

print b

DFTF.write("{: >15} {: >20}          {}\n\n".format('1', 'TOKEN', b))