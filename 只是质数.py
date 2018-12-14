from time import time
from pprint import pprint
import csv
nu =3
n=1
g = input('个数')
#t1 = time()
g = int(g)
z=[2]
p=[]
h=[]
while n <= g:
    for i in z:
        if (nu % i) == 0:
            nu += 1
            break
    else:
        z.append(nu)
        h.append([str(nu),str(n)])
        n =n+1
        nu += 1
        #print(str(z) + '\t' + str(n-1) )
#print (z)
with open('only_h.csv','wt',newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(h)
#print(time() - t1)
