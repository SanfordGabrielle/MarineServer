import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO species (name, genus, max_age, region, average_size) VALUES (?, ?, ?, ?, ?)",
            ('Orca', 'Orcinus Orca', '80', 'North Pacific Ocean', '22')
            )

cur.execute("INSERT INTO species (name, genus, max_age, region, average_size) VALUES (?, ?, ?, ?, ?)",
            ('Seal', 'Pinniped', '30', 'North Pacific Ocean', '22')
            )

cur.execute("INSERT INTO species (name, genus, max_age, region, average_size) VALUES (?, ?, ?, ?, ?)",
            ('Marlin', 'Istiophoridae', '20', 'North Pacific Ocean', '11')
            )

cur.execute("INSERT INTO species (name, genus, max_age, region, average_size) VALUES (?, ?, ?, ?, ?)",
            ('Bluefin Tuna', 'Tuna', '40', 'North Atlantic Ocean, Mediterranean', '5')
            )

cur.execute("INSERT INTO species (name, genus, max_age, region, average_size) VALUES (?, ?, ?, ?, ?)",
            ('Green Moray Eel', 'Gymnothorax', '25', 'Western Atlantic Ocean', '8')
            )

cur.execute("INSERT INTO species (name, genus, max_age, region, average_size) VALUES (?, ?, ?, ?, ?)",
            ('Blue Whales', 'Balaenoptera', '110', 'All Oceans, Arctic', '110')
            )

connection.commit()
connection.close()
