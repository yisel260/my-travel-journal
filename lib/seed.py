
from models.__init__ import CONN, CURSOR
from models.place import Place
from models.review import Review
from faker import Faker
import random 

fake = Faker()


def seed_database():
    Review.drop_table()
    Place.drop_table()
    Place.create_table()
    Review.create_table()

    # Create seed data
    guanajato = Place.create("Guanajuato", "Guanajuato", "Mexico")
    cozumel=Place.create("Cozumel", "Quintanaro", "Mexico")
    tokyo = Place.create("Tokyo", "Kanto", "Japan")
    oaxaca = Place.create("Oaxaca","Oaxaca", "Mexico")
    manila = Place.create("Quezon City","Manila", "Philipoines")
    same_name_city_1 =Place.create("SameNameCity","Region1", "Country1")
    same_name_city_2 = Place.create("SameNameCity","Region2", "Country2")

    
    
   
    Review.create(
                 food_rating=random.randint(1, 5),
                 safety_rating=random.randint(1, 5),
                 affordability_rating=random.randint(1, 5),
                 entertainment_rating=random.randint(1, 5),
                 comment=fake.paragraph(nb_sentences=2, variable_nb_sentences=False),
                 place_id=guanajato.id
)
    
    Review.create(food_rating=random.randint(1, 5),
               safety_rating=random.randint(1, 5),
               affordability_rating=random.randint(1, 5),
               entertainment_rating=random.randint(1, 5),
               comment=fake.paragraph(nb_sentences=2, variable_nb_sentences=False),
               place_id=cozumel.id
               )
    
    Review.create(food_rating=random.randint(1, 5),
               safety_rating=random.randint(1, 5),
               affordability_rating=random.randint(1, 5),
               entertainment_rating=random.randint(1, 5),
               comment=fake.paragraph(nb_sentences=2, variable_nb_sentences=False),
               place_id=tokyo.id
               )
    Review.create(food_rating=random.randint(1, 5),
               safety_rating=random.randint(1, 5),
               affordability_rating=random.randint(1, 5),
               entertainment_rating=random.randint(1, 5),
               comment=fake.paragraph(nb_sentences=2, variable_nb_sentences=False),
               place_id=oaxaca.id
               )
    
    Review.create(food_rating=random.randint(1, 5),
               safety_rating=random.randint(1, 5),
               affordability_rating=random.randint(1, 5),
               entertainment_rating=random.randint(1, 5),
               comment=fake.paragraph(nb_sentences=2, variable_nb_sentences=False),
               place_id=manila.id
               )
    
    Review.create(food_rating=random.randint(1, 5),
               safety_rating=random.randint(1, 5),
               affordability_rating=random.randint(1, 5),
               entertainment_rating=random.randint(1, 5),
               comment=fake.paragraph(nb_sentences=2, variable_nb_sentences=False),
               place_id=same_name_city_1.id
               )
    
    Review.create(food_rating=random.randint(1, 5),
               safety_rating=random.randint(1, 5),
               affordability_rating=random.randint(1, 5),
               entertainment_rating=random.randint(1, 5),
               comment=fake.paragraph(nb_sentences=2, variable_nb_sentences=False),
               place_id=same_name_city_2.id
               )




seed_database()
print("Seeded database")