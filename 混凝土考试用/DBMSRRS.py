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


# M b h C S
# A_s
M = float(input('M=(kN*m)'))
b = float(input('b=(mm)'))
h = float(input('h=(mm)'))
a_s = float(input('a_s=(mm)'))
C = float(input('C?'))
S = float(input('S?'))
print(10*'-')

f_y = f_y_dic[S]
f_c = f_c_dic[C]
f_t = f_t_dic[C]

beta_1 = 0.8
alpha_1 = 1
epsilon_cu = 0.0033
E_s = 200000

rho_min = after_dot(find_max(0.45*f_t/f_y, 0.002), 5)
xi_b = after_dot((beta_1)/(1+(f_y)/(epsilon_cu*E_s)), 3)

h_0 = h-a_s

alpha_s = after_dot((M*(10**6))/(alpha_1*f_c*b*(h_0**2)), 3)
xi = after_dot(1-(1-2*alpha_s)**0.5, 3)

if xi > xi_b:
    print('Error: xi>xi_b')
else:
    A_s = (alpha_1*f_c*b*xi*h_0)/(f_y)

print(A_s)

input()