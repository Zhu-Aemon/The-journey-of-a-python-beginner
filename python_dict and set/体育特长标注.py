group = '鲁智深 柴进 宋江 林冲 卢俊义 孙二娘 史进 吴用 李逵'
footBallGroup = '吴用 卢俊义 鲁智深'
pingpangGroup = '林冲 孙二娘 李逵'

group1 = set(group.split(' '))
football1 = set(footBallGroup.split(' '))
pp1 = set(pingpangGroup.split(' '))
blank = group1 - (football1 & pp1)

group = set()
for i in football1:
    group.add(i + '(足球）')
for i in pp1:
    group.add(i + '（乒乓）')
for i in blank:
    group.add(i)

print(group)
