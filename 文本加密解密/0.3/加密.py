# 之后应该可以将字数转换部分集合到一个函数里
import sys

zitoshu = {}
shutozi = {}

he_fa = ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','-',]


def cra_dic(hefa):#创建词典
    for i in range(0,len(hefa)):
        shutozi[i]=hefa[i]
        zitoshu[hefa[i]]=i

def da_san(wen):#打散字符
    z = []
    wen = wen.upper()
    z = list(wen)
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
        a = random.randint(0, len(he_fa))
        b=shutozi[a]
        mi_yao.append(str(b))
    return mi_yao
    
####################################################################################
mi_wen = []

print('说明：')
print('-' *40)
print('该程序可以实现对英文字母的简单加密')
print('*' *40)
print('只有合法字符列表一致的解密程序可以完成解密')
print('-' *40)
n=input('Type ENTER to continue.')
n=0



cra_dic(he_fa)

print('-'*40)
#明文输入部分
while True:
    ming_wen = input('请输入明文（只限于英文字母与数字）')
    print('-'*40)
    if yan_zheng(ming_wen) == 1:
        continue
    ming_wen = da_san(ming_wen)
    break

#密钥输入或生成
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
            mi += int(len(he_fa))
        mi_wen.append(mi)
        n += 1
    m += 1


n = 0


for n in range(len(mi_wen)):  # 密文数字转文字
    mi_wen[n] = shutozi[mi_wen[n]]


n = 0


for n in range(len(mi_yao)):  # 密钥数字转文字
    mi_yao[n] = shutozi[mi_yao[n]]

mi_yao = ''.join(mi_yao)# 将列表转换成字符串
mi_wen = ''.join(mi_wen)

print('密钥是' + '')
print(mi_yao)  
print('密文是：' + '')
print(mi_wen)

print('')
print('')

n = input('Type ENTER to exit.')
