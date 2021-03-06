# Arkusz: https://cke.gov.pl/images/stories/Matura2006/a2_inform.pdf
# Wyniki: https://cke.gov.pl/images/stories/WYNIKI.rar

from collections import Counter


def wczytaj(nazwa):
    with open(nazwa) as plik:
        return list(map(str.strip, plik))


def podpunkt_a(lista):
    zliczacz = Counter(lista)
    return {
        "ile_niesamotnych": sum(1 for k, v in zliczacz.items() if v > 1),
        "najczestszy": zliczacz.most_common(1)[0],
    }


def podpunkt_b(lista):
    return sum(1 for i in lista if i[-1] in "ACE")


def podpunkt_c(lista):
    return sum(1 for i in lista if i == i[::-1])


if __name__ == '__main__':
    # zapis do pliku został pominięty, gdyż z treści zadania nie wynika,
    # że to program ma umieszczać odpowiedzi w pliku ;)
    wyrazy = wczytaj('dane.txt')

    wyniki_a = podpunkt_a(wyrazy)
    print('Odpowiedzi do podpunktu a)')
    print(f'Liczba słów występujących więcej niż raz: {wyniki_a["ile_niesamotnych"]}')
    print(f'Słowo o największej liczbie wystąpień: {wyniki_a["najczestszy"][0]}')
    print(f'Liczba jego wystąpień: {wyniki_a["najczestszy"][1]}')
    print()
    print('Odpowiedź do podpunktu b)')
    print(f'Liczb parzystych jest {podpunkt_b(wyrazy)}')
    print()
    print('Odpowiedź do podpunktu c)')
    print(f'Liczba palindromów {podpunkt_c(wyrazy)}')
