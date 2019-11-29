from collections import OrderedDict
from math import floor

if __name__ == '__main__':
    number_to_roman_letter = OrderedDict({
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    })

    number_to_convert = 3999
    roman_string = ""

    for number, roman_letter in number_to_roman_letter.items():
        occurrence = floor(number_to_convert / number)

        if occurrence >= 1:
            for n in range(occurrence):
                roman_string += roman_letter
                number_to_convert -= number

    print(roman_string)
