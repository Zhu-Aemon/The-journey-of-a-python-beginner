ninenine = {}
for i in range(1, 10):
    for j in range(1, 10):
        ninenine["{}*{}".format(i, j)] = i * j

key = input()

if key in ninenine.keys():
    val = ninenine[key]
    print(val)

else:
    print('输入的乘法不在九九乘法表中')