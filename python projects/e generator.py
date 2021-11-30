import math
from decimal import *

while True:
    def calculator(k):
        getcontext().prec = k
        k = k + 1
        e = 0
        for i in range(k):
            e += Decimal(1/math.factorial(i))
        return Decimal(e)

    def main():
        print(
            'welcome to e calculator,'
            'In the shell below Enter the number of digits upto which the value of e should be calculated '
            'or enter a quit to exit'
              )
        a = (input('>>>'))
        if not a.isdigit():
            print('please enter a digit')
        else:
            print(calculator(int(a)))


    if __name__ == '__main__':
        main()
