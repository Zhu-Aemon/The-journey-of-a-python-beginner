a = input()
li = []
for i in range(len(a)):  # 遍历字符串
    if ord('a') <= ord(a[i]) <= ord('z') or ord('A') <= ord(a[i]) <= ord('Z'):  # 判断是否是英语字母
        ch = a[i].lower()  # 英文字母取小写
        if ch not in li:  # 判断字母是否在列表中
            li.append(ch)  # 将符合新的英文字母追加到列表
for ch in li:
    print(ch, end='')  # 字符连续输出，不空格，不换行
