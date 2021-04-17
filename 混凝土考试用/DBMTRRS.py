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
C = float(input('C='))
S = float(input('S='))
a_s = float(input('a_s(mm)='))
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

if M <= alpha_1*f_c*b_f_*h_f_*(h_0-h_f_/2):
    print('M <= alpha_1*f_c*b_f_*h_f_*(h_0-h_f_/2) =' +
          str(M)+'<=' + str(alpha_1*f_c*b_f_*h_f_*(h_0-h_f_/2)))
    T_Type = 1
    print('Type 1')

elif M > alpha_1*f_c*b_f_*h_f_*(h_0-h_f_/2):
    print('M > alpha_1*f_c*b_f_*h_f_*(h_0-h_f_/2) =' +
          str(M)+'>' + str(alpha_1*f_c*b_f_*h_f_*(h_0-h_f_/2)))
    T_Type = 2
    print('Type 2')
##
print(20*'-')
if T_Type == 1:

    alpha_s = after_dot((M)/(alpha_1*f_c*b_f_*h_0**2), 3)
    print('alpha_s = (M)/(alpha_1*f_c*b_f_*h_0**2) =' + '('+str(M) +
          ')/('+str(alpha_1)+'*'+str(f_c)+'*'+str(b_f_)+'*'+str(h_0)+'^2)')
    print('alpha_s='+str(alpha_s))

    xi = after_dot(1-(1-2*alpha_s)**0.5, 3)
    print('xi='+str(xi))

    A_s = after_dot((alpha_1*f_c*b_f_*xi*h_0)/(f_y), 0)
    print('A_s='+str(A_s)+'mm^2')


elif T_Type == 2:

    alpha_s = after_dot((M-alpha_1*f_c*(b_f_-b)*h_f_ *
                         (h_0-h_f_/2))/(alpha_1*f_c*b*h_0**2), 3)
    print('alpha_s='+str(alpha_s))

    xi = after_dot(1-(1-2*alpha_s)**0.5, 3)
    print('xi='+str(xi))

    if xi <= xi_b:

        A_s = after_dot((alpha_1*f_c*b*xi*h_0)/(f_y) +
                        (alpha_1*f_c*(b_f_-b)*h_f_)/(f_y), 0)
        print('A_s='+str(A_s)+'mm^2')

    elif xi > xi_b:
        print('xi > xi_b :' + str(xi)+'>'+str(xi_b))
        print('xi > xi_b , Bar too much ')
        print('Use DBMDRRS ')

        pass

if A_s >= A_s_min:
    print('A_s >= A_s_min')
else:
    print('A_s <A_s_min , mistake')

input()