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


M = float(input('M=(kN*m)'))
b = float(input('b=(mm)'))
h = float(input('h=(mm)'))
a_s = float(input('a_s=(mm)'))
a_s_ = float(input('a_s_=(mm)'))
C = float(input('C?'))
S = float(input('S?'))
S_ = float(input('S_?'))
A_s = float(input('A_s=(mm^2)'))
A_s_ = float(input('A_s_=(mm^2)'))
print(10*'-')
##
M = M * 10**6

f_y = f_y_dic[S]
f_y_ = f_y_dic[S_]
f_c = f_c_dic[C]
f_t = f_t_dic[C]

deta_1 = 0.8
alpha_1 = 1.0

epsilon_cu = 0.0033
E_s = 2*(10 ** 5)

xi_b = after_dot((deta_1)/(1+((f_y)/(epsilon_cu*E_s))), 3)
rho_max = xi_b*((alpha_1*f_c)/(f_y))
rho_min = after_dot(find_max(0.002, 0.45*f_t/f_y), 5)
##
h_0 = h-a_s

xi = (f_y*A_s-f_y_*A_s_)/(alpha_1*f_c*b*h_0)

if xi >= (2*a_s_/h_0) and xi <= xi_b:
    alpha_s = xi*(1-0.5*xi)
    M_u = alpha_s*alpha_1*f_c*b*h_0**2+f_y_*A_s_*(h_0-a_s_)
elif xi > xi_b:
    print('bar too much')
    alpha_sb = xi_b*(1-xi_b)
    M_u = alpha_sb*alpha_1*f_c*b*h_0**2+f_y_*A_s_*(h_0-a_s_)
elif xi < (2*a_s_/h_0):
    print('A_s_ useless')
    M_u = f_y*A_s*(h_0*a_s_)
else:
    print('Terr Error')

print(M_u)

if M_u >= M:
    print('Safe')
else:
    print('Not Safe')

input()