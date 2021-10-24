chinese = [76, 63, 79, 82, 53, 78, 67]
math = [88, 56, 78, 92, 69, 75, 82]
s = []
for i in range(len(chinese)):
    s.append(chinese[i] + math[i])
print('每位组员总分： ' + str(s))
maxnum = max(s)
tot = 0
for i in range(len(s)):
    tot += s[i]
avg = tot / len(s)
avg = ('%.2f' % avg)
print('最高总分：' + str(maxnum) + ',' + '小组平均分' + str(avg))
