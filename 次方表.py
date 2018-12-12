print('输入底数')
a = input() 
b = int(1)
print('输入次数')
c = input()
d = float(a)
a = float(a)
c = int(float(c))
e = 1
if c < 1:
    print(str(a) + '从' + str(c) + '到1的' + '次方表')
    while b >= c:
        c = int(c)
        d = float(d)
        a = float(a)
        e = a
        print(str(a) + '的' + str(b) + '次方\t' + str(e))
        e = d ** b
        b = b - 1
else:
    print(str(a) + '的1到' + str(c) + '次方表')
    while b <= c:
        c = int(c)
        d = float(d)
        a = float(a)
        print(str(a) + '的' + str(b) + '次方\t' + str(d))
        d = d * a
        b = b + 1