from hashlib import md5
from itertools import product
fout = open('out.txt', 'w')
alp = 'qwertyuiopasdfghjklzxcvbnm1234567890'
for i in range(4, 12):
    for pas in product(alp, repeat=i):
        hashh = md5(''.join(pas).encode()).hexdigest()
        print(type(hashh))
        fout.write(f'{hashh} \n')

