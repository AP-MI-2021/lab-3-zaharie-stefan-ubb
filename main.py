def input_data():
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


def main():
    print_menu()
    lst = []

    while True:
        option = input("Introduceți opțiunea: ")

        if option == "m":
            print_menu()
        elif option == "x":
            break
        elif option == "i":
            lst = input_data()

        else:
            print("Opțiune inexistentă!")


if __name__ == "__main__":
    main()
