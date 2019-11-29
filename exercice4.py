from random import choice
from re import match, findall


def generate_string(length=30):
    seq = ""
    for n in range(0, length):
        letter = choice(['a', 't', 'g', 'c'])
        seq += letter

    return seq


def is_valid(string):
    if match("^[atgc]+$", string) is not None:
        return True
    else:
        return False


def get_number_of_occurence(seq, string):
    return len(findall(seq, string))


if __name__ == '__main__':

    seq = ""
    while not is_valid(seq):
        seq = input("Séquence à rechercher: ")

    string = generate_string()
    print(is_valid(string))
    print("Chaïne: {}".format(string))

    number_of_occurence = get_number_of_occurence(seq=seq, string=string)
    proportion = number_of_occurence * 100 / len(string)

    print("Il y a {}% de {} dans votre chaïne".format(round(proportion, 2), seq))
