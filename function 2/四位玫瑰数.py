def isRose(n):  # 判断n是否是四位玫瑰数，是返回True，不是返回False
    summary = 0
    for i in range(4):
        summary += int(str(n)[i]) ** 4
    if summary == int(n):
        return True
    else:
        return False


def checkNumber(n):  # 检查字符串n是不是构成4位数，是返回整数n，不是返回-1
    if n.isdigit() and len(str(n)) == 4 and str(n)[0] != '0':
        return int(n)
    else:
        return -1


def printRose(a, b):  # 输出区间【a,b】之间所有的四位玫瑰数，不存在输出提示信息
    n = 0
    for num in range(a, b + 1):
        if isRose(num):
            print(num)
            n = n + 1
    if n == 0:
        print("此区间没有四位玫瑰数")


def main():
    a = checkNumber(input())
    if a == -1:
        print("第一个数不是四位数")
        return
    b = checkNumber(input())
    if b == -1:
        print("第二个数不是四位数")
        return
    if a <= b:
        printRose(a, b)
    else:
        printRose(b, a)


main()
