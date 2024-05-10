# lib/helpers.py
from models.place import Place
from models.review import Review 


def exit_program():
    print("Goodbye!")
    exit()

def search_places():

    print(""" I want to :
          1. See countries I have visited
          2. See the regions or states in a country I have visited 
          3. See all places I have visited 
          4. Search for a place by name

          """)
    choice = str(input(">"))
    places = Place.get_all()
    if choice == "1":
        countries =[]
        for place in places:
            if place.country not in countries:
                countries.append(place.country)

        for i, country in enumerate(countries, start=1):
           print(i, country)

    if choice == "2":
        country = str(input("Enter the country you want to search:"))
        places_in_country = Place.find_by_country(country)
        regions =[]
        for place in places_in_country:
            if place.region not in regions:
                regions.append(place.region)
        print ( f"You have visited the folowing regions or states in {country}")
        for i, region in enumerate(regions, start=1):
           print(i, region)

    if choice == "3":
       for i, place in enumerate(places, start=1):
           print(i, place)

    if choice == "4":
        name = str(input("Please enter the name of the place: "))
        place = Place.find_by_name(name)
        if len(place) == 1:
           print(f"{place.name},{place.region},{place.country}")
        else:
            print("There are too many places with this name!")


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
    comment= str( input(">"))
    
    new_review = Review.create(food_rating=food_rating, 
                               safety_rating=safety_rating,
                               affordability_rating=affordability_rating,
                               entertaiment_rating= entertaiment_rating,
                               comment = comment,
                               place_id = place.id)
    
    print("Review added! ")

    def grab_place_menu():
        print("""What would you like to do : 
          
          1. Add a place then review it
          2. Search for a place I have already added to review
          """)


def delete_place(place):
    place.delete()
