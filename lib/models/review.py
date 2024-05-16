from models.__init__ import CURSOR, CONN
from models.place import Place

class Review:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, food_rating ,safety_rating,affordability_rating, entertainment_rating ,comment, place_id, id=None):
        self.id = id
        self.food_rating = food_rating
        self.safety_rating = safety_rating
        self.affordability_rating = affordability_rating
        self.entertainment_rating = entertainment_rating
        self.comment = comment
        self.place_id = place_id

    def __repr__(self):
        return (
            f"{self.place_id}, {self.food_rating},{self.safety_rating},{self.affordability_rating}, {self.comment}" )

    @property
    def food_rating(self):
        return self._food_rating

    @food_rating.setter
    def food_rating(self, food_rating):
        if isinstance(food_rating, int) and food_rating >= 1 and food_rating <= 5:
            self._food_rating = food_rating
        else:
            raise ValueError(
                "The rating must be a number  between 1 and 5"
            )
    
    @property
    def safety_rating(self):
        return self._safety_rating

    @safety_rating.setter
    def safety_rating(self, safety_rating):
        if isinstance(safety_rating, int) and safety_rating >= 1 and safety_rating <= 5:
            self._safety_rating = safety_rating
        else:
            raise ValueError(
                "The rating must be a number  between 1 and 5"
            )
        
    @property
    def affordability_rating(self):
        return self._affordability_rating

    @affordability_rating.setter
    def affordability_rating(self, affordability_rating):
        if isinstance(affordability_rating, int) and affordability_rating >= 1 and affordability_rating <= 5:
            self._affordability_rating = affordability_rating
        else:
            raise ValueError(
                "The rating must be a number  between 1 and 5"
            )
        
    @property
    def entertainment_rating(self):
        return self._entertainment_rating

    @entertainment_rating.setter
    def entertainment_rating(self, entertainment_rating):
        if isinstance(entertainment_rating, int) and entertainment_rating >= 1 and entertainment_rating <= 5:
            self._entertainment_rating = entertainment_rating
        else:
            raise ValueError(
                "The rating must be a number  between 1 and 5"
            )

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        if isinstance(comment, str) and len(comment):
            self._comment = comment
        else:
            raise ValueError(
                "Please enter your commnet again"
            )


    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, place_id):
        if type(place_id) is int and Place.find_by_id(place_id):
            self._place_id = place_id
        else:
            raise ValueError(
                "department_id must reference a place in the database")


    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Employee instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            food_rating INTEGER,
            safety_rating INTEGER,
            affordability_rating INTEGER,
            entertainment_rating INTEGER,
            comment TEXT,
            place_id INTEGER,
            FOREIGN KEY (place_id) REFERENCES places(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Review instances """
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, job title, and department id values of the current Employee object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO reviews (food_rating, safety_rating, affordability_rating, entertainment_rating, comment, place_id)
                VALUES (?, ?, ?,?,?,?)
        """

        CURSOR.execute(sql, (self.food_rating, self.safety_rating, self.affordability_rating,self.entertainment_rating, self.comment,self.place_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Employee instance."""
        sql = """
            UPDATE reviews
            SET food_rating =?, safety_rating =? , affordability_rating =? , comment =?, place_id =?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.food_rating, self.safety_rating, self.affordability_rating, self.comment,self.place_id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Employee instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM reviews
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, food_rating,safety_rating,affordability_rating,entertainment_rating,comment,place_id):
        """ Initialize a new Employee instance and save the object to the database """
        review = cls(food_rating,safety_rating,affordability_rating, entertainment_rating,comment,place_id)
        review.save()
        return review

    @classmethod
    def instance_from_db(cls, row):
        """Return an Employee object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        review = cls.all.get(row[0])
        if review:
            # ensure attributes match row values in case local instance was modified
            review.food_rating = row[1]
            review.safety_raging = row[2]
            review.affordability_rating = row[3]
            review.entertainment_rating = row[4]
            review.comment = row[5]
            review.place_id = row[6]
        else:
            # not in dictionary, create new instance and add to dictionary
            review = cls(row[1], row[2], row[3], row[4], row[5],row[6])
            review.id = row[0]
            cls.all[review.id] = review
        return review

    @classmethod
    def get_all(cls):
        """Return a list containing one Employee object per table row"""
        sql = """
            SELECT *
            FROM reviews
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Employee object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM reviews
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_place_id(cls, place_id):
        """Return Employee object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM reviews
            WHERE place_id is ?
        """

        row = CURSOR.execute(sql, (place_id,)).fetchall()
        return cls.instance_from_db(row) if row else None