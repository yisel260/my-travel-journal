# lib/cli.py

from helpers import (
    exit_program,
    search_places,
    add_place,
    delete_place,
    add_review,
    get_place_details,
    menu,
    add_review1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            search_places()
        elif choice == "2":
            add_place()
        elif choice == "3":
            delete_place()
        elif choice == "4":
            add_review1()
        elif choice == "5":
            get_place_details()
        else:
            print("Invalid choice")

def select_place():
    pass

if __name__ == "__main__":
    main()
