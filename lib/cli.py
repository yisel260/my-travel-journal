# lib/cli.py

from helpers import (
    exit_program,
    search_places,
    add_place,
    delete_place,
    add_review1,
    get_place_details1,
    menu,
    add_review1,
    get_place_details1,
    search_reviews
)


def main():
    while True:
        menu()
        choice = input("> ").strip()
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
        elif choice== "5":
            search_reviews()
        elif choice == "6":
            get_place_details1()
        else:
            print(f"You have entered : {choice}")
            print("That is not a valid choice please enter a number")

def select_place():
    pass

if __name__ == "__main__":
    main()
