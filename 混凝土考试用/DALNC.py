f_c_dic = {15: 7.2, 20: 13.4, 25: 16.7, 30: 14.3, 35: 16.7, 40: 19.1, 45: 21.1,
           50: 23.1, 55: 25.3, 60: 27.5, 65: 29.7, 70: 31.8, 75: 33.8, 80: 35.9}

f_t_dic = {15: 0.91, 20: 1.10, 25: 1.27, 30: 1.43, 35: 1.57, 40: 1.71, 45: 1.80,
           50: 1.89, 55: 1.96, 60: 2.04, 65: 2.09, 70: 2.14, 75: 2.18, 80: 2.22}

f_y_dic = {300: 270, 400: 360, 500: 435, 550: 400, 600: 430}


def after_dot(n, i):
    h = ((n*10 ** i+0.5)//1)/10**i
    return h


def find_max(a, b):
    if a > b:
        return a
    else:
        return b


while True:
    Type = input('Know A ?(1/0)')
    if Type == '1':
        A = float(input('A(mm^2)'))
        break
    elif Type == '0':
        break
    else:
        input('index mistake!')
        continue

N = float(input('N(kN)='))
C = float(input('C='))
S_ = float(input('S_='))
N = N*10**3

f_y_ = f_y_dic[S_]
f_c = f_c_dic[C]
f_t = f_t_dic[C]

rho_min_ = 0.55/100

if Type == '1':
    phi = float(input('phi='))

    A_s_ = ((N)/(0.9*phi)-f_c*A)/f_y_
    rho = A_s_/A
    if rho > (3/100):
        print('rho > 3%')
        A_s_ = ((N)/(0.9*phi)-f_c*A)/(f_y_-f_c)


elif Type == '0':
    # method 2
    phi = 1
    rho_ = float(input('rho_(/%)=(1/%-3/%)'))
    rho_ = rho_/100

    A = (N)/(0.9*phi*(f_c+f_y_*rho_))
    A_s_ = A*rho_
    print('A='+str(A))
    print('JieMian?')

    A = float(input('A(mm^2)'))
    phi = float(input('phi='))

    A_s_ = ((N)/(0.9*phi)-f_c*A)/f_y_

    rho = A_s_/A
    if rho < rho_min_:
        print('A_s_ too small , A_s_ = min')
        print('A_s_min='+str(rho_min_*A))
        A_s_ = rho_min_*A
    else:
        pass
print(10*'-')
print('A='+str(A))
print('A_s_='+str(A_s_))

input()