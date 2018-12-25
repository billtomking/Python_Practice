# 之后应该可以将字数转换部分集合到一个函数里
import sys

zitoshu = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35,'-':36}

shutozi = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z',36:'-'}

he_fa = ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','-']


def da_san(wen):#打散字符
    n = 0
    z = []
    wen = wen.upper()
    while n < len(wen):
        z.append(wen[n])
        n += 1
    return z


def yan_zheng(wen):#用于验证字符串合法性
    n = 0
    w = 0
    try:
        len(wen)
    except:
        print('明文中含有不合法字符，请重新输入')
        return 1
    wen = wen.upper()
    while n < len(wen):
        if wen[n] in he_fa:
            n += 1
        else:
            print('明文中含有不合法字符，请重新输入')
            w = 1
            break
    if w == 0:
        return 0
    else:
        return 1



def chuang_yao(n):  # 用于产生随机密钥，之后可以考虑修改让用户自行输入
    import random
    if n=='':
        n = len(ming_wen)
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


mi_wen = []

print('说明：')
print('-' *40)
print('该程序可以实现对英文字母的简单加密')
print('合法字符为英文字母、数字以及‘-’符号')
print('加密后可以使用对应解密程序解密')
print('-' *40)
n=input('Type anything to continue.')
n=0

print('-'*40)
while True:
    ming_wen = input('请输入明文（只限于英文字母与数字）')
    print('-'*40)
    if yan_zheng(ming_wen) == 1:
        continue
    ming_wen = da_san(ming_wen)
    break


n = 0
while True:#选择密钥生成方式
    print("-" *40)
    print('密钥生成方式：')
    print('    1、随机生成')
    print('    2、自行输入')
    print("-" *40)
    way = input('请选择密钥方式：')
    print('-'*40)
    if way == '1':
        mi_yao = chuang_yao(input('密钥长度（可不填）')) #需要判断输入是否合法
        print('-'*40)
        break
    elif way == '2':
        while n == 0:
            mi_yao = input('密钥为:')#需要有方法检测输入密钥的合法性
            print('-'*40)
            if yan_zheng(mi_yao) == 1:
                continue
            mi_yao = mi_yao.upper()
            mi_yao = da_san(mi_yao)
            break
        break
    else:
        print('错误,请重新选择')
        continue



while n < len(mi_yao):  # 将密钥转换成数字
    mi_yao[n] = zitoshu[str(mi_yao[n])]
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
            mi += 37
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

print('')
print('')

n = input('Type anything to exit.')
sys.exit()