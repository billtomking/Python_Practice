ming_wen = input('请输入明文（带空格）')
ming_wen = list(ming_wen.split())
mingl = len(ming_wen)
def chuang_yao(n):#用于产生随机密钥，之后可以考虑修改让用户自行输入
    import random
    if n == None:
        n = int(mingl)
    i = 0
    mi_yao = []
    while i <= n:
        i +=1
        a = random.randint(0,35)
        if a == 0:
            b = '0'
        elif a == 1:
            b = '1'
        elif a == 2:
            b = '2'
        elif a == 3:
            b = '3'
        elif a == 4:
            b = '4'
        elif a == 5:
            b = '5'
        elif a == 6:
            b = '6'
        elif a == 7:
            b = '7'
        elif a == 8:
            b = '8'
        elif a == 9:
            b = '9'
        elif a == 10:
            b = 'A'
        elif a == 11:
            b = 'B'
        elif a == 12:
            b = 'C'
        elif a == 13:
            b = 'D'
        elif a == 14:
            b = 'E'
        elif a == 15:
            b = 'F'
        elif a == 16:
            b = 'G'
        elif a == 17:
            b = 'H'
        elif a == 18:
            b = 'I'
        elif a == 19:
            b = 'J'
        elif a == 20:
            b = 'K'
        elif a == 21:
            b = 'L'
        elif a == 22:
            b = 'M'
        elif a == 23:
            b = 'N'
        elif a == 24:
            b = 'O'
        elif a == 25:
            b = 'P'
        elif a == 26:
            b = 'Q'
        elif a == 27:
            b = 'R'
        elif a == 28:
            b = 'S'
        elif a == 29:
            b = 'T'
        elif a == 30:
            b = 'U'
        elif a == 31:
            b = 'V'
        elif a == 32:
            b = 'W'
        elif a == 33:
            b = 'X'
        elif a == 34:
            b = 'Y'
        elif a == 35:
            b = 'Z'
        mi_yao.append(str(b))
    return mi_yao
mi_yao = chuang_yao(12)
print(mi_yao)
    