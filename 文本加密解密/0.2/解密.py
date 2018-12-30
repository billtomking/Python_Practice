import itertools
import sys

zitoshu = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35,'-':36}

shutozi = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z',36:'-'}

he_fa = ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','-']

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

print('说明：')
print('-' *40)
print('该程序可以实现对相应加密软件的加密结果的解密')
print('合法字符为英文字母、数字以及‘-’符号')
print('-' *40)
n=input('Type anything to continue.')

ming_wen = []

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

n = input('Type anything to exit.')