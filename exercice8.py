if __name__ == '__main__':
    x = {'a', 'b', 'c', 'd'}
    y = {'s', 'b', 'd'}

    print(x, y)
    print('c' in x)
    print('a' in y)
    print(x - y, y - x)
    print(x.union(y))
    print(x.intersection(y))