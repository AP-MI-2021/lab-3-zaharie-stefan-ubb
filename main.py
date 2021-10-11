from math import sqrt
from itertools import islice, count


def is_prime(num: int) -> bool:
    """Determină dacă numărul dat este prim."""
    if num < 2:
        return False

    for div in islice(count(2), int(sqrt(num) - 1)):
        if num % div == 0:
            return False

    return True


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(1) is False
    assert is_prime(90) is False
    assert is_prime(17) is True
    assert is_prime(6) is False


def input_list():
    raw_data = input("Introduceți o listă de numere: ")
    str_list = raw_data.split()

    int_list = []
    for i in str_list:
        int_list.append(int(i))

    return int_list


def print_menu():
    menu = """
Meniu:
i. Citire date.

m. Afișare meniu.
x. Ieșire.
    """

    print(menu)


def run_tests():
    test_is_prime()


def main():
    run_tests()
    print_menu()
    lst = []

    while True:
        option = input("Introduceți opțiunea: ")

        if option == "m":
            print_menu()
        elif option == "x":
            break
        elif option == "i":
            lst = input_list()

        else:
            print("Opțiune inexistentă!")


if __name__ == "__main__":
    main()
