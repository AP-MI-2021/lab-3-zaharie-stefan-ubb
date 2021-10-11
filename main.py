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


def get_longest_all_primes(lst: list[int]) -> list[int]:
    """Determina cea mai lunga subsecventa dintr-o lista data cu proprietatea
    ca toate numerele din ea sunt prime."""
    ans = []
    sequence = []

    for num in lst:
        if is_prime(num):
            sequence.append(num)
        else:
            if len(sequence) > len(ans):
                ans = sequence
            sequence = []

    # edge case, sequence is at the end of the list
    if len(sequence) > len(ans):
        ans = sequence

    return ans


def test_get_longest_all_primes():
    assert get_longest_all_primes([1, 2, 3]) == [2, 3]
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([1]) == []
    assert get_longest_all_primes([3, 3, 3, 3, 1, 2]) == [3, 3, 3, 3]
    assert get_longest_all_primes([2, 1]) == [2]


def get_longest_prime_digits(lst: int) -> list[int]:
    """Determina cea mai lunga subsecventa dintr-o lista cu proprietatea
    ca toate numerele din ea sunt formate doar din cifre prime"""
    ans = []
    sequence = []

    for num in lst:
        num_copy = num
        ok = True
        while num > 0:
            if not is_prime(num % 10):
                ok = False
                break
            num //= 10

        if ok:
            sequence.append(num_copy)
        else:
            if len(sequence) > len(ans):
                ans = sequence
            sequence = []

    # edge case, sequence is at the end of the list
    if len(sequence) > len(ans):
        ans = sequence

    return ans


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([9]) == []
    assert get_longest_prime_digits([1, 2, 3, 4]) == [2, 3]
    assert get_longest_prime_digits([99]) == []
    assert get_longest_prime_digits([10]) == []
    assert get_longest_prime_digits([33, 44, 12, 22, 32, 31]) == [22, 32]


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

1. Determina cea mai lunga subsecventa in care toate nr sunt prime.
2. Determina cea mai lunga subsecventa in care toate nr au cifre prime.

m. Afișare meniu.
x. Ieșire.
    """

    print(menu)


def run_tests():
    test_is_prime()
    test_get_longest_all_primes()
    test_get_longest_prime_digits()


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

        elif option == "1":
            print(get_longest_all_primes(lst))
        elif option == "2":
            print(get_longest_prime_digits(lst))

        else:
            print("Opțiune inexistentă!")


if __name__ == "__main__":
    main()
