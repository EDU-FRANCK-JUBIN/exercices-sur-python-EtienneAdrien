from math import pi


def volumeConeDroit(rayon, hauteur):
    return (pi * rayon ** 2 * hauteur) / 3


if __name__ == '__main__':
    volumeConeDroit(rayon=5, hauteur=5)