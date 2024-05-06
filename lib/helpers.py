# lib/helpers.py
from models.place import Place
from models.review import Review 



def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_all_places():

    places = Place.get_all()
    for i, place in enumerate(places, start=1):
       print(i, place)

def add_place():
    name = str(input("Please enter the name of the place or city you want to add :")).lower().strip()
    region = str(input("Please enter the region associated with the place you want to add :")).lower().strip()
    country = str(input("Please enter the country associated with the place you want to add :")).lower().strip()
    new_place = Place.create(name, region, country)

    print(f"""

       {new_place.name}, {new_place.region}, {new_place.country}  was added to your list of places.
       
       """)
    
    follow_up_menu(new_place)

def follow_up_menu(place):
    print(""" 
          
          What would you like to do next?
          
          1. Add a review to this place
          2. Update or edit this place
          3. Go back to main menu
          
          """)
    choice = input(">")
    if choice == "1":
        add_review(place)
    elif choice == "2":
        update_place(place)
    elif choice == "3":
        pass


def add_review(place):
    print(f"You are adding a review to {place.name}, {place.region},{place.country}")
    print("""How was the food? Please enter your rating from 1 to 5.
          1= It was hard to find anything good to eat!
          5= Delicious! I cannot wait to go back 
          """)
    food_rating = int( input(">"))

    print("""Was this place safe? Please enter your rating from 1 to 5.
          1= Not at all! I was lucky to get back alive!
          5= Very! You can enjoy everything with out worry
          """)
    safety_rating = int( input(">"))

    print("""How affordable was this place? Please enter your rating from 1 to 5.
          1= Not at all! Come ready to spend you savings!
          5= Very! It feels like your money multiplied.
          """)
    affordability_rating = int( input(">"))

    print("""How was the entertaiment? Please enter your rating from 1 to 5.
          1= Not a lot of things to do or see, boring, dissapointing
          5= Wow! So many things to see and do! I need to go back. 
          """)
    entertaiment_rating = int( input(">"))

    print("Enter your thougths about this place.")
    comment= int( input(">"))
    
    new_review = Review.create(food_rating=food_rating, 
                               safety_rating=safety_rating,
                               affordability_rating=affordability_rating,
                               entertaiment_rating= entertaiment_rating,
                               comment = comment)
    print("Review added! ")