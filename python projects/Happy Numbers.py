def isHappy(n):
    flag = True
    previous = []
    while flag:
        summary = 0
        for i in str(n):
            summary += int(i) ** 2
        n = summary
        if n in previous or n == 1:
            flag = False
        previous.append(summary)
    if n == 1:
        return True
    else:
        return False


def HappyGenerator():
    n = 1
    while True:
        if isHappy(n):
            yield n
        n += 1


def main():
    g = HappyGenerator()
    print('press enter to generate happy numbers'
          '\nenter q to exit')
    while True:
        a = input()
        if a == '':
            print(next(g))
        elif a == 'q':
            break


if __name__ == '__main__':
    main()
