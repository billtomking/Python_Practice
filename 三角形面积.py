A = input('边长1：')
B = input('边长2：')
C = input('边长3：')
A = float(A)
B = float(B)
C = float(C)
if A <= B + C:
    if B <= A + C:
        if C <= A + B:
            #用三角函数算面积
            cosC = (A**2 + B**2 - C**2)/(2 * A * B)
            cosC = float(cosC)
            sinC = (1 - (cosC)**2)**0.5
            print(cosC)
            print(sinC)
            S = 0.5 * sinC * A * B
            # 用另一个公式计算面积
            s = (A + B + C) / 2
            area = (s*(s-A)*(s-B)*(s-C)) ** 0.5
            print('三角形面积为 %0.2f' %area)#" %0.2f' %area"是什么？
            print(S)
            print('误差=' + str(area - S))
        else:
            print('边长错误')
    else:
            print('边长错误')
else:
            print('边长错误')

