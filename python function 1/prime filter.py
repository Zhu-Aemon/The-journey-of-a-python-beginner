def prime_filter(a):
    if a == 0:
        return False
    if a == 1:
        return False
    if a == 2:
        return True
    else:
        li = []
        for i in range(2, a):
            li.append(a % i != 0)
        return False not in li


num = int(input())
ls = [x for x in range(0, num + 1)]
prime_result = list(filter(prime_filter, ls))

for i in range(len(prime_result)):
    print(prime_result[i], end=' ')
