def min_max_moy(l):
    min = l[0]
    max = l[0]
    moy = 0

    for n in l:
        if n < min:
            min = n
        if n > max:
            max = n

        moy += n

    moy /= len(l)

    return min, max, moy


if __name__ == '__main__':
    print(min_max_moy([10, 18, 14, 20, 12, 16]))
