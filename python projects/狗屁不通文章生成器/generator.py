import random
import data

x = input('输入你的主题：')
y = input('你想说多少句话：')
gp = ''
for i in range(int(y)):
    if random.randint(0, 4) == 4:
        gp += data.datalist[random.randint(0, len(data.datalist) - 1)]
        gp += '。'
    else:
        gp += data.datalist[random.randint(0, len(data.datalist) - 1)]
        gp += '，'

print(gp.replace('d', x))
