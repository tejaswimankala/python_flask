import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

cur.execute ("INSERT INTO Users  (name, email) VALUES ( ?, ?)",
            ( 'tejaswi', 'tejaswi.mankala@gmail.com') )         

cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('Dmart', 'Rice', 300 )
            )
cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('Dmart', 'Sugar', 15 ) 
            )
cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('Dmart', 'Bread', 30 )
            )

cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('BigBazar', 'Rice', 350 )
            )
cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('BigBazar', 'Sugar', 250)
            )
cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('BigBazar', 'Bread', 20)
            )

cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('Supermart', 'Rice', 100 )
            )
cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('Supermart', 'Sugar', 400)
            )
cur.execute("INSERT INTO store_groceries  (store_name, grocery_item, price) VALUES (?, ?, ?)",
            ('Supermart', 'Bread', 80)
            )


connection.commit()
connection.close()