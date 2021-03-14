import sqlite3
import sys

argument = sys.argv
base_name = argument[1]

connector = sqlite3.connect(base_name)
my_cursor = connector.cursor()
my_cursor.execute("CREATE TABLE measures (measure_id INT PRIMARY KEY, measure_name VARCHAR(30) UNIQUE);")
my_cursor.execute("CREATE TABLE ingredients (ingredient_id INT PRIMARY KEY, ingredient_name VARCHAR(30) NOT NULL UNIQUE);")
my_cursor.execute("CREATE TABLE meals (meal_id INT PRIMARY KEY, meal_name VARCHAR(30) NOT NULL UNIQUE);")
my_cursor.execute("INSERT INTO measures (measure_id, measure_name) VALUES (1, 'ml'), (2, 'g'),"
                  "(3, 'l'), (4, 'cup'), (5, 'tbsp'), (6, 'tsp'), (7, 'dsp'), (8, '') ")
my_cursor.execute("INSERT INTO ingredients (ingredient_id, ingredient_name) VALUES (1, 'milk'), (2, 'cacao'),"
                  "(3, 'strawberry'), (4, 'blueberry'), (5, 'blackberry'), (6, 'sugar') ")
my_cursor.execute("INSERT INTO meals (meal_id, meal_name) VALUES (1, 'breakfast'), (2, 'brunch'),"
                  "(3, 'lunch'), (4, 'supper') ")
connector.commit()
connector.close()
