def func(number):
    return 2 * number ** 3 + number - 5


def tabuler(function, min, max, step):
    assert min < max
    assert step

    for n in range(min, max, step):
        print(function(n))


if __name__ == '__main__':
    tabuler(func, 1, 10, 1)
