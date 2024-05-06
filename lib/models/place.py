from models.__init__ import CURSOR, CONN


class Place:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, region, country, id=None):
        self.id = id
        self.name = name
        self.region = region
        self.country = country


    def __repr__(self):
        return f"{self.name},{self.region}, {self.country}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Please type the name of the place"
            )

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if isinstance(region, str) and len(region):
            self._region = region
        else:
            raise ValueError(
                "Please reentry the name of the region"
            )
        
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if isinstance(country, str) and len(country):
            self._country = country
        else:
            raise ValueError(
                "ooops! Something went wrong , please try again"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Place instances """
        sql = """
            CREATE TABLE IF NOT EXISTS places (
            id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            country TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS places;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO places (name, region, country)
            VALUES (?, ?,?)
        """

        CURSOR.execute(sql, (self.name, self.region, self.country))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    @classmethod
    def create(cls, name, region, country):
        """ Initialize a new Department instance and save the object to the database """
        place = cls(name, region, country)
        place.save()
        return place

    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
            UPDATE places
            SET name = ?, region = ?, country = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.region, self.country, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM places
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Place object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        place = cls.all.get(row[0])
        if place:
            # ensure attributes match row values in case local instance was modified
            place.name = row[1]
            place.region = row[2]
            place.country = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            place = cls(row[1], row[2],row[3])
            place.id = row[0]
            cls.all[place.id] = place
        return place

    @classmethod
    def get_all(cls):
        """Return a list containing a Department object per row in the table"""
        sql = """
            SELECT *
            FROM places
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Department object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM places
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Department object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM places
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def reviews(self):
        """Return list of reviews associated with current department"""
        from review import Review
        sql = """
            SELECT * FROM reviews
            WHERE  place_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Review.instance_from_db(row) for row in rows
        ]