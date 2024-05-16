# lib/cli.py

from helpers import (
    exit_program,
    search_places,
    add_place,
    delete_place,
    add_review,
    get_place_details,
    menu,
    select_place
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
            place=delete_place()
            delete_place(place)
        elif choice == "4":
            place= select_place()
            add_review(place)
        elif choice == "5":
            place= select_place()
            get_place_details(place)
        else:
            print("Invalid choice")

def select_place():
    pass

if __name__ == "__main__":
    main()
