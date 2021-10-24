a = input()
e = list(a.split(','))
for i in range(len(e)):
    if '0' in e:
        e.remove('0')
c = []
for j in range(len(e)):
    s = list((e[j]))
    if '-' in s:
        s.remove('-')
    s = [int(i) for i in s]
    tot = 0
    for i in range(len(s) - 1):
        tot += s[i+1]
    if tot == s[0]:
        c.append(e[j])
length = len(c)
print('符合要求的数有' + str(length) + '个')
for nu in range(len(c)):
    print(c[nu], end=' ')
