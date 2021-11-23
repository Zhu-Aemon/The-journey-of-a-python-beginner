# 定义函数getCelsius,将华氏温度转化为摄氏温度
def get_celsius(a):
    b = (a - 32) * 5 / 9  # 计算摄氏温度
    return b  # 返回摄氏温度


f = float(input())  # 输入华氏温度
c = get_celsius(f)  # 调用getCelsius求摄氏温度
print("fahr=%.1f, celsius = %.1f\n" % (f, c))  # 输出结果
