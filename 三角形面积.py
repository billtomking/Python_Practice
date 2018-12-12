A = input('边长1：')
B = input('边长2：')
C = input('边长3：')
A = float(A)
B = float(B)
C = float(C)
if A <= B + C:
    if B <= A + C:
        if C <= A + B:
            cosC = (A**2 + B**2 - C**2)/(2 * A * B)
            cosC = float(cosC)
            sinC = (1 - (cosC)**2)**0.5
            print(cosC)
            print(sinC)
            S = 0.5 * sinC * A * B
            print(S)
        else:
            print('边长错误')
    else:
            print('边长错误')
else:
            print('边长错误')

