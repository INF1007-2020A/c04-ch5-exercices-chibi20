#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = number * -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    Liste_nom = []
    for i in prefixes:
        Liste_nom.append(i+suffixe)

    return Liste_nom

def is_prime_nuber(number):
    for i in range(2, number//2):
        if number % i == 0:
            return False

    return True


def prime_integer_summation() -> int:
    prime = [2, 3, 5]
    number=6
    somme = 0
    while len(prime) < 100:
        if is_prime_nuber(number):
            prime.append(number)
            somme += number
        number += 1

    return somme


def factorial(number: int) -> int:
    factorielle = 1
    for i in range(1, number+1):
        factorielle = factorielle * i

    return factorielle


def use_continue() -> None:
    for i in range(1, 11):
        if i ==5:
            continue
        else:
            print (i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    final = []
    for i in groups:
        if len(i) > 3 or len(i) <= 10:
            final.append(True)
            continue
        if 25 in i:
            final.append(True)
            continue
        if 50 in i:
            is_50=True
        else:
            is_50=False

        est_accepté = True
        for j in i:
            if j < 18:
                est_accepté = False
                break
            if j > 70 and is_50:
                est_accepté=False
                break

        final.append(est_accepté)





    return [final]


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
