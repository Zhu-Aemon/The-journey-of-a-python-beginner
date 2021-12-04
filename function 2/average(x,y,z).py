def average(x, y, z):
    f = lambda x, y, z: (x + y + z) / 3
    return f(x, y, z)


print('%.2f' % (average(2, 2, 2)))
