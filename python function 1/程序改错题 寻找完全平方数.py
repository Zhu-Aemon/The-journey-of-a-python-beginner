def filterLst(L):
    outL = []
    for x in L:
        for j in range(x + 1):
            if j * j == x:
                outL.append(x)
    return outL


s = input()
data = list(s.split(','))
data_int = [int(x) for x in data]
result = filterLst(data_int)
if len(result) != 0:
    print("完全平方数有", result)
else:
    print("无符合要求的数！")
