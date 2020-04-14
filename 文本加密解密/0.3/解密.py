import itertools
import sys
import py2exe

zitoshu = {}
shutozi = {}

he_fa = ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','-']


def cra_dic(hefa):#根据合法字符列表自动创建字符与数字互换的字典
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
        print('！！明文中含有不合法字符，请重新输入！！')
        return 1
    wen = wen.upper()
    while n < len(wen):
        if wen[n] in he_fa:
            n += 1
        else:
            print('！！明文中含有不合法字符，请重新输入！！')
            w = 1
            break
    if w == 0:
        return 0
    else:
        return 1


#################################################################
print('说明：')
print('-' *40)
print('该程序可以实现对相应加密软件的加密结果的解密')

print('-' *40)
n=input('Type ENTER to continue.')

ming_wen = []

cra_dic(he_fa)

while True:
    print("-" *40)
    mi_yao = input('请输入密钥（只限于英文字母与数字）')  
    print("-" *40)
    if yan_zheng(mi_yao) == 1:
        continue
    mi_yao = da_san(mi_yao)
    break


while True:
    print("-" *40)
    mi_wen = input('请输入密文(只限于英文字母与数字)')
    print("-" *40)
    if yan_zheng(mi_wen) == 1:
        continue
    mi_wen = da_san(mi_wen)
    break


n = 0
m = 0


for n in range(len(mi_yao)):  # 将密钥转换成数字
    mi_yao[n] = zitoshu[mi_yao[n]]


n = 0


for n in range(len(mi_wen)):  # 将密文转换成数字
    mi_wen[n] = zitoshu[mi_wen[n]]


i = 0
k = 0
n = 0
ming = 0
m = 0
 
for i in mi_wen:  # 解密部分
    if n >= len(mi_yao):
        n = 0
    k = mi_yao[n]
    if n < len(mi_yao):
        ming = (k + i) % 37
        ming_wen.append(ming)
        n += 1

mingl = len(ming_wen)
n = 0
m = 0

while m < mingl:  # 明文数字转文字
    ming_wen[m] = shutozi[ming_wen[m]]
    m += 1

ming_wen = ''.join(ming_wen)
print("-" *40)
print('明文是：')
print(ming_wen)
print("-" *40)

n = input('Type ENTER to exit.')