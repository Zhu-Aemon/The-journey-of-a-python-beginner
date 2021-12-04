# 定义lambda函数getLastBit返回一个数的个位数
getLastBit = lambda x: str(x % 10)


# 定义一个可变参数的函数makeNumber，求任意个整数的个位数构成的一个新整数
def makeNumber(b):
    s = ''
    for i in b:
        s += getLastBit(i)
    return s


# 输入一组逗号分隔的数，截取个位数构成的新整数。
t = list(eval(input()))
print("新整数是%d" % int(makeNumber(t)))
