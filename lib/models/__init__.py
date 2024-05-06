import sqlite3

CONN = sqlite3.connect('my_places.db')
CURSOR = CONN.cursor()
