from hashlib import md5
from itertools import product

fout = open('out.txt', 'w')
alp = 'qwertyuiopasdfghjklzxcvbnm1234567890'
ran = range(1,4)
print(f'число операций:{sum([len(alp)**x for x in ran])}')
for i in ran:
    for pas in product(alp, repeat=i):
        hashh = md5(''.join(pas).encode()).hexdigest()
        fout.write(f'{hashh} \n')

