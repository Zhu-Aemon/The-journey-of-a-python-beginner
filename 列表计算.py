s1 = [0, 1, 2, 3, 4, 5, 6]
s2 = []
for i in range(len(s1)):
    if i % 2 == 0:
        s2.append(3)
    else:
        s2.append(4)
s2.pop()
print(s2)
