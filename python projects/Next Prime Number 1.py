# Have the program find prime numbers until the user chooses to stop asking for the next one.
def Prime():
    n = 2
    while True:
        li = []
        for i in range(2, n - 1):
            if n % i == 0:
                li.append(i)
        if len(li) == 0:
            yield n
        n += 1


def main():
    print('if you wanna continue, then press enter'
          '\nif you wanna quit, enter anything you want')
    g = Prime()
    while True:
        a = input()
        if a == '':
            print(next(g))
        else:
            break


if __name__ == "__main__":
    main()
