# lib/helpers.py
from models.place import Place
from models.review import Review 

def menu():
    print("""Please select an option:
          
          0.Exit the program
          1.Search my places 
          2.Add a new place 
          3.Delete a place 
          4.Review a place 
          5.Search reviews 
          6.See details about a place 
    
          """)

def exit_program():
    print("Goodbye! See you after your next andventure! ")
    exit()

def search_places():
    while True:
        print(""" I want to :
            1. See countries I have visited
            2. See the regions or states in a country I have visited 
            3. See all places I have visited 
            4. Search for a place by name
            5. Return to main menu

            """)
        choice = str(input(">")).strip()
        places = Place.get_all()
        
        if choice == "1":
            countries =[]
            for place in places:
                if place.country not in countries:
                    countries.append(place.country)

            for i, country in enumerate(countries, start=1):
                print(i, country.capitalize())

            follow_up_choice= 0
            
            while True:
                print("""
                
                What would you like to do next?
                1. Select a country and see places I have visited there
                2. Go back to main menu
                
                """)
            
                follow_up_choice =int(input("Enter a Number: "))

                if follow_up_choice == 1:
                    print("Please chose a country by its number")
                    country = int(input("Enter a the number of the country you want to select:"))
                    country_choice = countries[country-1]
                    places = Place.find_by_country(country_choice)
                    print (f"You have visited the following places in {country_choice}:")
                    for i, place in enumerate(places, start=1):
                        print(i,f"{ place.name.capitalize()},{place.region.capitalize()}")
                    while True:
                        print("""
                                
                                What would you like to do next?
                                1. Select a place and see details about it
                                2. Go back to main menu

                                """)
                        choice_2 = input(">").strip()

                        if choice_2 == "1": 
                            print("Please select a place by number")
                            user_choice= int(input(">"))
                            place = places[user_choice-1]
                            get_place_details(place)
                            return

                        elif choice_2 == "2":
                            return
                        
                elif follow_up_choice == 2:
                    return
                else: 
                    print(f"You have entered:  {follow_up_choice}  .That is not a valid choice. Please try again.")
            
        elif choice == "2":
            country = str(input("Enter the country you want to search:")).strip().lower()
            places_in_country = Place.find_by_country(country)
            regions =[]
            for place in places_in_country:
                if place.region not in regions:
                    regions.append(place.region) 

            print ( f"You have visited the folowing regions or states in {country}")
            for i, region in enumerate(regions, start=1):
                print(i, region.capitalize())
            
            if len(regions) == 1:
                region = regions[0]
                print( """ What would you like to do next?
                        
                        1. see the places in this region I have visited in this region
                        2. go back to main menu
                        
                        """)
                region_user_choice = input(">")

                if region_user_choice == "1":
                    places = Place.find_by_region(region)
                    for i, place in enumerate(places, start =1):
                        print(i,{place.name})
                    while True:
                            print("""
                                    
                                    What would you like to do next?
                                    1. Select a place and see details about it
                                    2. Go back to main menu

                                    """)
                            choice_2 = input(">").strip()

                            if choice_2 == "1": 
                                print("Please select a place by number")
                                user_choice= int(input(">"))
                                place = places[user_choice-1]
                                get_place_details(place)
                                return

                            elif choice_2 == "2":
                                return
                elif region_user_choice == "2":
                    return
                else:
                    print (f"You have entered :{region_user_choice}.That is not a valid choice.Plase try again")

            if len(regions)>1:
               
               while True:
                    print("""
                    
                    What would you like to do next?
                    1. Select a region and see places I have visited there
                    2. Go back to main menu
                    
                    """)

                    follow_up_choice =int(input(">"))

                    if follow_up_choice == 1:
                        print("Please chose a region by its number")
                        region = int(input("Enter a the number of the region you want to select:"))

                        if region >=1 and region < len(regions):
                            region_choice = regions[region-1]
                            places = Place.find_by_region(region_choice)
                            print (f"You have visited the following places in {region_choice}:")
                            for i, place in enumerate(places, start=1):
                                print(i, place.name)
                                while True:
                                    print("""
                                            
                                            What would you like to do next?
                                            1. Select a place and see details about it
                                            2. Go back to main menu

                                            """)
                                    choice_2 = input(">").strip()

                                    if choice_2 == "1": 
                                        print("Please select a place by number")
                                        user_choice= int(input(">"))
                                        place = places[user_choice-1]
                                        get_place_details(place)
                                        return

                                    elif choice_2 == "2":
                                        return
                                    else: 
                                         print(f"""You have entered {choice}.That is not a valid choice.
                                                    please look at the numbers next to the regions and make your choice
                                                    by entering a number.""")
                                
                    elif follow_up_choice == 2:
                            return
                    else:
                            print(f"You have entered {follow_up_choice}. That is not a valid choice. Please try again.")
                            
                        

        elif choice == "3":
            for i, place in enumerate(places, start=1):
                print(i, place)

            while True:
                print("""
                        
                        What would you like to do next?
                        1. Select a place and see details about it
                        2. Go back to main menu

                        """)
                choice_2 = input(">").strip()

                if choice_2 == "1": 
                    print("Please select a place by number")
                    user_choice= int(input(">"))
                    place = places[user_choice-1]
                    get_place_details(place)
                    return

                elif choice_2 == "2":
                    return
                else: 
                    print(f"You have entered {choice_2}.That is not a valid choice please try again.")

        elif choice == "4":
                    name = str(input("Please enter the name of the place: ")).strip().lower()
                    place = Place.find_by_name(name)
                    if place : 
                        for i, place in enumerate(places, start=1):
                            print(i, place)
                    else: 
                        print(f"You have entered {name}. There are no matches for this name. ")
                    break
        
        elif choice == '5':
            return
        else:
            print(f"You have entered: {choice}. That is not a valid choice. Please try again.")

def add_place():
    name = str(input("Please enter the name of the place or city you want to add :")).lower().strip()
    region = str(input("Please enter the region associated with the place you want to add :")).lower().strip()
    country = str(input("Please enter the country associated with the place you want to add :")).lower().strip()
    new_place = Place.create(name, region, country)

    print(f"""

       {new_place.name.capitalize()}, {new_place.region.capitalize()}, {new_place.country.capitalize()}  was added to your list of places.
       
       """)
    
    follow_up_menu(new_place)

def follow_up_menu(place):
    while True:
        print(""" 
            
            What would you like to do next?
            
            1. Add a review to this place
            2. Go back to main menu
            
            """)
        choice = input(">")
        if choice == "1":
            add_review(place)
            break
        elif choice == "2":
            return
        else:
            print("Please enter a valid choice.")

def add_review1():
     place= select_place()
     add_review(place)


def add_review(place):
    print(f"You are adding a review to {place.name.capitalize()}, {place.region.capitalize()},{place.country.capitalize()}")
    while True:
        print("""How was the food? Please enter your rating from 1 to 5.
            
            1= It was hard to find anything good to eat!
            5= Delicious! I cannot wait to go back 
            """)
        food_rating_input = int( input(">"))
        if food_rating_input >=1 and food_rating_input <=5:
            food_rating = food_rating_input
            break
        else: 
            print("""
                  The rating must be a number from 1 to 5. 
                  """)
                
    while True:
        print("""Was this place safe? Please enter your rating from 1 to 5.
            1= Not at all! I was lucky to get back alive!
            5= Very! You can enjoy everything without worry
            """)
        safety_rating_input = int( input(">"))
        if safety_rating_input >=1 and safety_rating_input <=5:
            safety_rating = safety_rating_input
            break
        else: 
            print("""
                  The rating must be a number from 1 to 5. 
                  """)

    while True:
        print("""How affordable was this place? Please enter your rating from 1 to 5.
            1= Not at all! Come ready to spend you savings!
            5= Very! It feels like your money multiplied.
            """)
        affordability_rating_input = int( input(">"))
        if affordability_rating_input >=1 and affordability_rating_input <=5:
            affordability_rating= affordability_rating_input
            break
        else:
            print("""
                  The rating must be a number from 1 to 5. 
                  """)

    while True:
        print("""How was the entertaiment? Please enter your rating from 1 to 5.
            1= Not a lot of things to do or see, boring, dissapointing
            5= Wow! So many things to see and do! I need to go back. 
            """)
        entertainment_rating_input = int( input(">"))
        if entertainment_rating_input>=1 and entertainment_rating_input<=5:
            entertainment_rating = entertainment_rating_input
            break
    while True:
        print("Enter your thougths about this place.")
        comment_input= str( input(">"))
        if comment_input:
            comment = comment_input
            break
        else: 
            print("The Comment section cannot be empty.")

    
    new_review = Review.create(food_rating=food_rating, 
                               safety_rating=safety_rating,
                               affordability_rating=affordability_rating,
                               entertainment_rating= entertainment_rating,
                               comment = comment,
                               place_id = place.id)
    
    
    print("Review added! ")

    print (new_review)


def delete_place():

    place=select_place()
    while True:
        print(f"""
            You are about to delete {place}
            is this correct?

            1. Yes
            2. No
            
            """)
        choice = input(">")
        if choice == "1": 
            reviews = place.reviews()  
            for review in reviews:
                review.delete()       
            place.delete()
            print (f"{place} has been deleted!")
            return
        elif choice == "2":
            return
        else: 
            print ("You must chooce either 1 or 2.")

def search_reviews():
    reviews = Review.get_all()
    while True: 
        print("""What would you like to do?
            1. See all reviews
            2. Search reviews for places with  a specific rating in a category
            3. See reviews of a specific place""")
        
        choice = input(">")
        if choice == "1":
        
            for review in reviews: 
                place = Place.find_by_id(review.place_id)

                print (f"""
                        {place}
                        {review}
                        """)
            break
            
        elif choice == "2":
            while True:
                print("""What category would you like to look at?
                    1.Food
                    2.Safety
                    3.Affordability 
                    4.Entertainment 
                    """)
                
                category_choice = input(">")
                valid_choices = [1,2,3,4,5,]
                if category_choice =="1":
                        while True:
                            print(f"""Please enter a number from 1 to 5 
                            Show me places that have a food rating of : """)
                            try:
                                rating_input = int(input(">"))
                                if rating_input in valid_choices:
                                    rating= rating_input
                                    places = []
                                    for review in reviews:
                                        if review.food_rating == rating:
                                            place = Place.find_by_id(review.place_id)
                                            places.append(place)
                                    if places:
                                        for i, place in enumerate(places, start=1):
                                            print(i, place)
                                        return
                                    else: 
                                        print("No places match your search!")
                                        break
                            except :
                                print("Please enter a valid number from 1 to 5")

                elif category_choice=="2":
                        while True:
                            print(f"""Please enter a number from 1 to 5 
                            Show me places that have a safety rating of : """)
                            try:
                                rating_input = int(input(">"))
                                if rating_input in valid_choices:
                                    rating = rating_input
                                    places = []
                                    for review in reviews:
                                        if review.safety_rating == rating:
                                            place = Place.find_by_id(review.place_id)
                                            places.append(place)
                            
                                    if places:
                                        for i, place in enumerate(places, start=1):
                                            print(i, place)
                                            return
                                    else: 
                                        print("No places match your search!")
                                        break
                            except:
                                 print("Please enter a valid number from 1 to 5")

                elif category_choice=="3":
                        while True:       
                            print(f"""Please enter a number from 1 to 5 
                            Show me places that have a affordability rating of : """)
                            try:
                                rating_input = int(input(">"))
                                if rating_input in valid_choices:
                                    rating = rating_input
                                    places = []
                                    for review in reviews:
                                        if review.affordability_rating == rating:
                                            place = Place.find_by_id(review.place_id)
                                            places.append(place)
                                        
                                    if places:
                                        for i, place in enumerate(places, start=1):
                                            print(i, place)
                                        return
                                    else: 
                                        print("No places match your search!")    
                                        break
                            except:
                                  print("Please enter a valid number from 1 to 5")
                        
                elif category_choice=="4":
                        while True:
                            print(f"""Please enter a number from 1 to 5 
                            Show me reviews that have a enetertainment rating of : """)
                            try:
                                rating_input = int(input(">"))
                                if rating_input in valid_choices:
                                    rating = rating_input
                                    places = []
                                    for review in reviews:
                                        if review.entertainment_rating == rating:
                                            place = Place.find_by_id(review.place_id)
                                            places.append(place)
                                    if places:
                                        for i, place in enumerate(places, start=1):
                                            print(i, place)
                                        return
                                    else: 
                                        print("No places match your search!")
                                        break
                            except:
                                  print("Please enter a valid number from 1 to 5")          
                else:
                    print("Please enter a valid choice, a number from 1 to 4.")

        elif choice == "3":
            place =select_place()
            reviews = place.reviews()
            print(f"These are the reviews associated with {place}")
            for i, review in enumerate(reviews, start = 1):
                    print(f"""
                        Review {i},
                        Food:{review.food_rating}
                        Safety:{review.safety_rating}
                        Affordability:{review.affordability_rating}
                        Entertainment:{review.entertainment_rating}
                        Comment:{review.comment}""")

            review_follow_up_actions(reviews,place)
            return
        else:
            print("please enter a valid choice, a number from 1 to 3. ")
          
def review_follow_up_actions(reviews,place):
            while True:         
                print("""What would you like to do next?
                        1. Delete a review 
                        2. Delete all reviews
                        3. Add a new review
                        4. Go back to the main menu""")
                
                choice = input(">")
                if choice == "1":
                    if len(reviews) == 1:
                        print(f"Deleting review of {place}.")
                        review = reviews[0]
                        review.delete()
                        print("Review deleted successfully!")
                        return

                    if len(reviews) > 1:
                        while True:
                            print("Please reference the list of reviews and choose the one you want to delete")
                            print("I want to delete review number : ")
                            user_selection = int(input(""))
                            if user_selection >=1 and user_selection < len(reviews):
                                review = reviews[user_selection - 1]
                                review.delete()
                                print(f"review number {user_selection} has been deleted.")
                elif choice == '2':
                    for review in reviews:
                        print(f"Deleting review of {place}.")
                        review = reviews[0]
                        review.delete()
                        print("Review deleted successfully!")
                        return
                elif choice == "3":
                    add_review(place)
                    return
                elif choice == "4":
                    return
                    

def get_place_details1():
    place = select_place()
    get_place_details(place)

def get_place_details(place):
    
    print (f"""
           
             Place:{place.name}
             Region:{place.region}
             Country:{place.country}

             """)
    
    reviews = place.reviews()
    if reviews:
        for i, review in enumerate(reviews, start = 1):
            print(f"""
                    Review {i},
                    Food:{review.food_rating}
                    Safety:{review.safety_rating}
                    Affordability:{review.affordability_rating}
                    Entertainment:{review.entertainment_rating}
                    Comment:{review.comment}
                        """)
    else:
        print ("You have not added any reviews to this place")

def select_place():
    while True:
        print ("""How would you like to select a place?
            1. Select from a list of all my places
            2. Search for a place by name""")
        
        choice = input(">")

        if choice == "1":
            while True:
                places= Place.get_all()
                for i, place in enumerate(places, start=1):
                    print(i, place)
                try:
                    number_choice =int(input("Enter the number of your choice:"))
                    if isinstance(number_choice,int) and number_choice >=1 and number_choice <= len(places):
                        selected_place = places[number_choice-1]
                        return selected_place
                    else: 
                        print(f"""
                            You have entered {number_choice}. 
                            That is not a valid choice. Please try again.
                            Enter the number that matches your choice""")
                except ValueError :
                    print("""
                          Please enter a valid number!
                          """)
                    
        elif choice == '2': 
            place_name= input("Enter the name of the place:").lower().strip()
            places = Place.find_by_name(place_name)
            print (places)

            if places:
                if len(places) == 1:
                   selected_place = places[0]
                   return selected_place
            
                elif len(places) > 1:
                    print ("There are several places with that name please select the correct one from the list.")
                    for i, place in enumerate(places, start = 1):
                        print (i, place)
                    user_choice = int(input("The number of your choice:>"))
                    selected_place = places[user_choice-1]
                    return selected_place
                else: 
                    print(f"Oh no! We found no places with the name {place_name}")
        else: 
            print(f"You have entered {choice} . That does not match a valid choice please try again.")
                

            

        
             
    