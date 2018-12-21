# 之后应该可以将字数转换部分集合到一个函数里
ming_wen = input('请输入明文（带空格）')
ming_wen = ming_wen.upper()
ming_wen = list(ming_wen.split())
mingl = len(ming_wen)
mi_wen = []
n = 0


def chuang_yao(n):  # 用于产生随机密钥，之后可以考虑修改让用户自行输入
    import random
    if n=='':
        n = mingl
    i = 1
    n = int(n)
    mi_yao = []
    while i <= n:
        i += 1
        a = random.randint(0, 35)
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


def zitoshu(yuan):  # 用于将文字转换成数字，以便后续计算
    yuan = str(yuan)
    if yuan == '0':
        return 0
    elif yuan == '1':
        return 1
    elif yuan == '2':
        return 2
    elif yuan == '3':
        return 3
    elif yuan == '4':
        return 4
    elif yuan == '5':
        return 5
    elif yuan == '6':
        return 6
    elif yuan == '7':
        return 7
    elif yuan == '8':
        return 8
    elif yuan == '9':
        return 9
    elif yuan == 'A':
        return 10
    elif yuan == 'B':
        return 11
    elif yuan == 'C':
        return 12
    elif yuan == 'D':
        return 13
    elif yuan == 'E':
        return 14
    elif yuan == 'F':
        return 15
    elif yuan == 'G':
        return 16
    elif yuan == 'H':
        return 17
    elif yuan == 'I':
        return 18
    elif yuan == 'J':
        return 19
    elif yuan == 'K':
        return 20
    elif yuan == 'L':
        return 21
    elif yuan == 'M':
        return 22
    elif yuan == 'N':
        return 23
    elif yuan == 'O':
        return 24
    elif yuan == 'P':
        return 25
    elif yuan == 'Q':
        return 26
    elif yuan == 'R':
        return 27
    elif yuan == 'S':
        return 28
    elif yuan == 'T':
        return 29
    elif yuan == 'U':
        return 30
    elif yuan == 'V':
        return 31
    elif yuan == 'W':
        return 32
    elif yuan == 'X':
        return 33
    elif yuan == 'Y':
        return 34
    elif yuan == 'Z':
        return 35


def shutozi(yuan):  # 用于将计算结果转换成文字
    yuan = str(yuan)
    if yuan == '0':
        return '0'
    elif yuan == '1':
        return '1'
    elif yuan == '2':
        return '2'
    elif yuan == '3':
        return '3'
    elif yuan == '4':
        return '4'
    elif yuan == '5':
        return '5'
    elif yuan == '6':
        return '6'
    elif yuan == '7':
        return '7'
    elif yuan == '8':
        return '8'
    elif yuan == '9':
        return '9'
    elif yuan == '10':
        return 'A'
    elif yuan == '11':
        return 'B'
    elif yuan == '12':
        return 'C'
    elif yuan == '13':
        return 'D'
    elif yuan == '14':
        return 'E'
    elif yuan == '15':
        return 'F'
    elif yuan == '16':
        return 'G'
    elif yuan == '17':
        return 'H'
    elif yuan == '18':
        return 'I'
    elif yuan == '19':
        return 'J'
    elif yuan == '20':
        return 'K'
    elif yuan == '21':
        return 'L'
    elif yuan == '22':
        return 'M'
    elif yuan == '23':
        return 'N'
    elif yuan == '24':
        return 'O'
    elif yuan == '25':
        return 'P'
    elif yuan == '26':
        return 'Q'
    elif yuan == '27':
        return 'R'
    elif yuan == '28':
        return 'S'
    elif yuan == '29':
        return 'T'
    elif yuan == '30':
        return 'U'
    elif yuan == '31':
        return 'V'
    elif yuan == '32':
        return 'W'
    elif yuan == '33':
        return 'X'
    elif yuan == '34':
        return 'Y'
    elif yuan == '35':
        return 'Z'

mi_yao = chuang_yao(input('密钥长度')) 


while n < len(mi_yao):  # 将密钥转换成数字
    mi_yao[n] = zitoshu(mi_yao[n])
    n += 1
n = 0


while n < len(ming_wen):  # 将明文转换成数字
    ming_wen[n] = zitoshu(ming_wen[n])
    n += 1
i = 0
n = 0


for i in ming_wen:  # 加密部分
    if n >= len(mi_yao):
        n = 0
    k = mi_yao[n]
    if n < len(mi_yao):
        mi = (i - k)
        if mi < 0:
            mi += 36
        mi_wen.append(mi)
        n += 1
n = 0


while n < len(mi_wen):  # 密文数字转文字
    mi_wen[n] = shutozi(mi_wen[n])
    n += 1
n = 0


while n < len(mi_yao):  # 密钥数字转文字
    mi_yao[n] = shutozi(mi_yao[n])
    n += 1


print('密钥是' + '')
print(mi_yao)  # 要找方法将列表转换成字符串
print('密文是：' + ' ')
print(mi_wen)
