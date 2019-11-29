def diviseurs_propres(number):
    diviseurs = []
    for n in range(2, number):
        if number % n == 0:
            diviseurs.append(n)
    return diviseurs


if __name__ == '__main__':
    number = 0

    while number <= 0:
        try:
            number = int(input("Entrez un entier strictement positif: "))
        except ValueError:
            number = 0

    diviseurs = diviseurs_propres(number)

    if diviseurs:
        diviseurs = [str(x) for x in diviseurs]
        result = "Diviseurs propres sans répétitions de {}: {}".format(number, ", ".join(diviseurs))
    else:
        result = "Diviseurs propres sans répétitions de {}: Aucun il est premier".format(number)

    print(result)

