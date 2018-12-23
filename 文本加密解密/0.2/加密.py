# 之后应该可以将字数转换部分集合到一个函数里

print('-'*40)

he_fa = ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

z = []#将明文打散成单字
n = 0
m = 0
while m == 0:
    ming_wen = input('请输入明文（只限于英文字母与数字）')
    mingl = len(ming_wen)
    ming_wen = ming_wen.upper()
    while n < mingl:
        if ming_wen[n] in he_fa:
            z.append(ming_wen[n])
            n += 1
            m = 1
        else:
            print('明文中含有不合法字符，请重新输入')
            break

            

ming_wen = z


#ming_wen = list(ming_wen.split())
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

zitoshu = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}

shutozi = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}

n = 0
while n == 0:#选择密钥生成方式
    print("-" *40)
    print('密钥生成方式：')
    print('    1、随机生成')
    print('    2、自行输入')
    print("-" *40)
    way = input('请选择密钥方式：')
    if way == '1':
        mi_yao = chuang_yao(input('密钥长度（可不填）')) 
        n = 1
    elif way == '2':
        while n == 0:
            mi_yao = input('密钥为:')#需要有方法检测输入密钥的合法性
            n = 1
        break
    else:
        print('错误,请重新选择')

mi_yao = mi_yao.upper()

while n < len(mi_yao):  # 将密钥转换成数字
    mi_yao[n] = zitoshu.get[str(mi_yao[n])]
    n += 1


n = 0


while n < len(ming_wen):  # 将明文转换成数字
    ming_wen[n] = zitoshu[ming_wen[n]]
    n += 1

i = 0
n = 0
m = 0

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
    m += 1


n = 0


while n < len(mi_wen):  # 密文数字转文字
    mi_wen[n] = shutozi[mi_wen[n]]
    n += 1


n = 0


while n < len(mi_yao):  # 密钥数字转文字
    mi_yao[n] = shutozi[mi_yao[n]]
    n += 1

mi_yao = ''.join(mi_yao)# 将列表转换成字符串
mi_wen = ''.join(mi_wen)

print('密钥是' + '')
print(mi_yao)  
print('密文是：' + '')
print(mi_wen)
