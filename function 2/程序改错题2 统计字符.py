def gt5(s):
    gt5s = 0
    for c in s:
        if c.isdigit() and int(c) >=5:
            gt5s += 1
    return gt5s


while True:
    s = input("")
    if s.lower() == 'end':
        break
    print('字符串为"{}"，其中单个数字大于等于5的有{}个'.format(s, gt5(s)))
