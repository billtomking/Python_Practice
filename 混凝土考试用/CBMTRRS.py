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


M = float(input('M(kN*m)='))
b_f_ = float(input('b_f_(mm)='))
h_f_ = float(input('h_f_(mm)='))
b = float(input('b(mm)='))
h = float(input('h(mm)='))
a_s = float(input('a_s(mm)='))
C = float(input('C='))
S = float(input('S='))
A_s = float(input('A_s(mm)='))
print(10*'-')
M = M * 10**6

f_y = f_y_dic[S]
f_c = f_c_dic[C]
f_t = f_t_dic[C]

deta_1 = 0.8
alpha_1 = 1.0

epsilon_cu = 0.0033
E_s = 2*(10 ** 5)

xi_b = after_dot((deta_1)/(1+((f_y)/(epsilon_cu*E_s))), 3)
rho_max = xi_b*((alpha_1*f_c)/(f_y))
rho_min = after_dot(find_max(0.002, 0.45*f_t/f_y), 5)

A_s_min = rho_min*b*h
h_0 = h-a_s
##

if f_y*A_s <= alpha_1*f_c*b_f_*h_f_:
    print('M <= alpha_1*f_c*b_f_*h_f_) =' +
          str(M)+'<=' + str(alpha_1*f_c*b_f_*h_f_))
    T_Type = 1
    print('Type 1')

elif f_y*A_s > alpha_1*f_c*b_f_*h_f_:
    print('M > alpha_1*f_c*b_f_*h_f_ =' +
          str(M)+'>' + str(alpha_1*f_c*b_f_*h_f_))
    T_Type = 2
    print('Type 2')


if T_Type == 1:
    if A_s < (rho_min*b*h):
        print('Error: Bar lack')
    else:
        xi = after_dot((f_y*A_s)/(alpha_1*f_c*b*h_0), 3)
        if xi > xi_b:
            xi = xi_b
            print('Warning: xi>xi_b , xi=xi_b')
        else:
            pass
        alpha_s = after_dot(xi*(1-0.5*xi), 3)
        M_u = alpha_s*alpha_1*f_c*b*(h_0**2)


elif T_Type == 2:
    xi = after_dot((f_y*A_s-alpha_1*f_c*(b_f_-b)*h_f_)/(alpha_1*f_c*b*h_0), 3)

    if xi <= xi_b:
        alpha_s = after_dot(xi*(1-0.5*xi), 3)
        M_u = alpha_s*alpha_1*f_c*b*h_0**2 + \
            alpha_1*f_c*(b_f_-b)*h_f_*(h_0-0.5*h_f_)
    elif xi > xi_b:
        print('Warning : Bar too Much')
        alpha_sb = after_dot(xi_b*(1-0.5*xi_b), 3)
        M_u = alpha_sb*alpha_1*f_c*b*h_0**2 + \
            alpha_1*f_c*(b_f_-b)*h_f_*(h_0-0.5*h_f_)
        pass

print(M_u)
print(M)
if M_u >= (M):
    print('Safe')
else:
    print('Not Safe')

input()