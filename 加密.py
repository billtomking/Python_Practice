mi_yao = input('请输入密钥（带空格）')#在加密时自动生成随机密钥
mi_yao = list(mi_yao.split())#不能拿用set（）来转换，因为set是无序的,希望找到不用输入时带空格的方法
mi_wen = input('请输入密文(带空格)')
mi_wen = list(mi_wen.split())
yao = len(mi_yao)
wen = len(mi_wen)
ming_wen = []
n = 0
m = 0
def zitoshu(yuan):#用于将密文转换成数字，以便后续计算
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
def shutozi(yuan):#用于将计算结果转换成明文
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
while n < yao:
    mi_yao[n] = zitoshu(mi_yao[n])
    n += 1
print(mi_yao)
n=0
while m < wen:
    mi_wen[m] = zitoshu(mi_wen[m])
    m += 1
i = 0
k = 0
ming = 0
for i in mi_wen:
    k = mi_yao[n]
    if n < yao:
        ming = (k + i)%36
        ming_wen.append(ming)
    elif n >= yao:
        n = 0
mingl = len(ming_wen)
n = 0
m = 0
while m < mingl:
    ming_wen[m] = shutozi(ming_wen[m])
    m += 1
print(ming_wen)