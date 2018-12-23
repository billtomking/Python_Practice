import itertools
mi_yao = input('请输入密钥（只限于英文字母与数字）')  # 在加密时自动生成随机密钥
mi_yao = mi_yao.upper()

z = []
n = 0
while n < len(mi_yao):
    z.append(mi_yao[n])
    n += 1
mi_yao = z

mi_wen = input('请输入密文(只限于英文字母与数字)')
mi_wen = mi_wen.upper()

z = []
n = 0
while n < len(mi_wen):
    z.append(mi_wen[n])
    n += 1
mi_wen = z

yao = len(mi_yao)
wen = len(mi_wen)
ming_wen = []
n = 0
m = 0



zitoshu = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}

shutozi = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}


while n < yao:  # 将密钥转换成数字
    mi_yao[n] = zitoshu[mi_yao[n]]
    n += 1
n = 0

while m < wen:  # 将密文转换成数字
    mi_wen[m] = zitoshu[mi_wen[m]]
    m += 1
i = 0
k = 0
n = 0
ming = 0
m = 0
 
for i in mi_wen:  # 解密部分
    if n >= yao:
        n = 0
    k = mi_yao[n]
    if n < yao:
        ming = (k + i) % 36
        ming_wen.append(ming)
        n += 1

mingl = len(ming_wen)
n = 0
m = 0

while m < mingl:  # 明文数字转文字
    ming_wen[m] = shutozi[ming_wen[m]]
    m += 1

ming_wen = ''.join(ming_wen)
print(ming_wen)
