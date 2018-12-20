import random
from time import time
i = 1
r = 0
w = 0
c = 0
t1 = time()
while i <= 10 :
    s = random.randint(1,4)
    a = random.randint(1,100)
    b = random.randint(1,100)
    if s ==1:
        c = a + b
        print(str(a) + "+" + str(b) + "=")
        d = input()
        d = int(d)
        c = int(c)
        if d == c:
            print("正确\n")
            r +=1
        else:
            print('错误,正确答案是' + str(c) + '\n')
            w +=1
    elif s ==2:
        c = a - b
        print(str(a) + "-" + str(b) + "=")
        d = input()
        d = int(d)
        c = int(c)
        if d == c:
            print("正确\n")
            r +=1
        else:
            print('错误,正确答案是' + str(c) + '\n')
            w +=1
    elif s ==3:
        print(str(a) + "*" + str(b) + "=")
        c = a * b
        d = input()
        d = int(d)
        c = int(c)
        if d == c:
            print("正确\n")
            r +=1
        else:
            print('错误,正确答案是' + str(c) + '\n')
            w +=1
    elif s ==4:
        shang = random.randint(-20,20)
        c = shang
        print(str(shang * a) + "/" + str(a) + "=")
        d = input()
        d = int(d)
        c = int(c)
        if d == c:
            print("正确\n")
            r +=1
        else:
            print('错误,正确答案是' + str(c) + '\n')
            w +=1
    i+=1
print('共用时:' + '')
print(time()-t1)
print('正确：' + str(r) + '个\t' + '错误：' + str(w) + '个\t' + '正确率' + str(r/(r+w)*100) + "%")
    
