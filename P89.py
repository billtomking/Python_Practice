A = []
for i in range(9999,100000,1):
    if i % 81 == 0:
        if i % 91 ==0:
            print(i)
            b = str(i)
            if b[-3] == '1':
                A.append(i)
print(A)

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
#计算机教材P89练习题
