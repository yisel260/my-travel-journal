
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
    guanajato = Place.create("guanajuato", "guanajuato", "mexico")
    cozumel=Place.create("cozumel", "quintanaro", "mexico")
    tokyo = Place.create("tokyo", "kanto", "japan")
    oaxaca = Place.create("oaxaca","oaxaca", "mexico")
    manila = Place.create("quezon city","manila", "philipines")
    same_name_city_1 =Place.create("sameNameCity","region1", "country1")
    same_name_city_2 = Place.create("sameNameCity","region2", "country2")

    
    
   
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