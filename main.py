def print_menu():
    menu = """
Meniu:
m. Afișare meniu
x. Ieșire.
    """

    print(menu)


def main():
    print_menu()

    while True:
        option = input("Introduceți opțiunea: ")

        if option == "m":
            print_menu()
        elif option == "x":
            break

        else:
            print("Opțiune inexistentă!")


if __name__ == "__main__":
    main()
