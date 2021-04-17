d_r = [6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 36, 40, 50]
nu_r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
j = 0
pi = 3.1415926535898
A_all = {}


def after_dot(n, i):
    h = ((n*10 ** i+0.5)//1)/10**i
    return h


while i <= len(d_r)-1:
    j = 1
    while j < len(nu_r):
        d = d_r[i]
        r = 0.5*d
        nu = nu_r[j]
        A = after_dot(nu*pi*r**2, 0)
        index = ''
        index = 'd'+str(d)+'*'+str(nu)
        the = {A: index}
        A_all.update(the)
        j = j+1
    i = i+1

while True:
    A_s = int(input('A(mm^2)='))
    print(10*'-')
    delta = 0
    n = 0
    while n < 5:
        A_s_u = A_s+delta
        if A_s_u in A_all:
            print(A_all.get(A_s_u)+' : '+str(A_s_u))
            n = n+1
        else:
            pass
        delta = delta+1

        if A_s_u > 18000:
            break
        else:
            pass
    input()