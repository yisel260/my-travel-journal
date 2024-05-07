# lib/cli.py

from helpers import (
    exit_program,
    search_places,
    add_place,
    #delete_place,
    add_review,
    #get_place_details
    
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
            add_review(place)
        elif choice == "5":
            get_place_details()
        else:
            print("Invalid choice")


def menu():
    print("""Please select an option:
          
          0.Exit the program
          1.Search my places 
          2.Add a new place 
          3.Delete a place 
          4.Review a place 
          5.See details about a place 
    
          """)

if __name__ == "__main__":
    main()
