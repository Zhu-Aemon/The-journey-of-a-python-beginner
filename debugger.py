x = input().split(',')
x = [eval(i) for i in x]
minf = x[0]
i = 0
while i < len(x):
    if minf > x[i]:
        minf = x[i]
    i = i + 1
print("最小元素=", minf)
