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
    Type = input('Need Ben ?(1/0)')
    if Type == '1':
        break
    elif Type == '0':
        break
    else:
        input('index mistake!')
        continue

V = float(input('V(kN):'))
b = float(input('b(mm):'))
h = float(input('h(mm):'))
C = float(input('C:'))
S_sv = float(input('S_sv:'))
a_s = float(input('a_s(mm):'))
alpha_ac = float(input('alpha_ac(0.7?):'))

V = V*10**3

beta_c = 1

f_yv = f_y_dic[S_sv]
f_c = f_c_dic[C]
f_t = f_t_dic[C]

h_0 = h-a_s
h_w = h_0
if (h_w/b) > 4:
    print('Error: h_w/b >4')
elif (h_w/b) <= 4:
    if (0.25*beta_c*f_c*b*h_0) > V:
        if (alpha_ac*f_t*b*h_0) < V:
            if Type == '0':
                A_sv = float(input('A_sv(mm^2)='))
                num01=((V-alpha_ac*f_t*b*h_0)/(f_yv*h_0))
                print('s<='+str(after_dot(A_sv/num01,0)))
                s = float(input('sv(mm)='))

                rho_sv = (alpha_ac)/(b*s)
                rho_sv_min = 0.24*f_t/f_yv
                if rho_sv<rho_sv_min:
                    print('Error:rho_sv<rho_sv_min')
                    
                ######

            elif Type == '1':
                print('Now Can Not')
        elif (alpha_ac*f_t*b*h_0) >= V:
            print('Follow GB')

    elif (0.25*beta_c*f_c*b*h_0) > V:
        print('Error:Section unfit')

else:
    print('Error')

input()