JD =input('输入精度')
JD = float(JD)
w = float(999)
n = 1
e1 = 0
e2 = 0
while w>=JD:
    e1 = (1 + (1/n))**n
    w = e1 - e2
    #print(str(w) + '\t' + str(e2) + '\t' + str(e1))
    n = n+1
    e2 = e1
print( str(w) + '\t' + str(e1))

