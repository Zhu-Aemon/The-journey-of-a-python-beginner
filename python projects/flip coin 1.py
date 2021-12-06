import random


def CoinFlipper():
    if random.randint(0, 1) == 0:
        return 'head'
    else:
        return 'tail'


def keepFlipping(n):
    for i in range(n):
        print(CoinFlipper(), end=' ')


def main():
    a = int(input('how many times do you want to flip the coin:'))
    return keepFlipping(a)


if __name__ == '__main__':
    main()
