class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            for i in range(item):
                self.a, self.b = self.b, self.a + self.b
            return self.a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            li = []
            for i in range(stop):
                self.a, self.b = self.b, self.a + self.b
                li.append(self.a)
            return li[start:stop]


def main():
    print('This is a Fibonacci Sequence generator.'
          '\nYou can enter a value to which the sequence is calculated to.'
          '\nYou can enter two numbers, divided by a comma, to show the sequence between these two numbers.')
    while True:
        a = input('>>>')
        li = list(str(a).split(','))
        li = [int(x) for x in li]
        if len(li) == 1:
            x = li[0]
            print(Fib[x])
        elif len(li) == 2:
            x = [li[0], li[1]]
            print(Fib()[x[0]:x[1]])


if __name__ == '__main__':
    main()
