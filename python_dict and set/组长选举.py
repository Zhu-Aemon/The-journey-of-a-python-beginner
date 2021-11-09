vote = ['鲁智深', '柴进', '宋江', '吴用', '林冲', '卢俊义',
        '柴进', '柴进', '孙二娘', '史进', '吴用', '卢俊义', '柴进',
        '林冲', '宋江', '宋江', '卢俊义', '吴用', '吴用']

result = {}
l = set(vote)
for i in l:
    j = vote.count(i)
    result[i] = j

print('得票情况：', end='')
print(result)
print('最高票数：', max(result.values()))

ls = []
for k,v in result.items():
    if v == max(result.values()):
        ls.append(k)

print('最高得票者：', end='')
for i in ls:
    print(i, end=' ')