import sqlite3

global data, columns
data = []
columns = ('id', 'name', 'age', 'weight', 'sex', 'type', 'owner')

def get(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.split(',')
            data.append((int(line[0]), line[1], int(line[2]), float(line[3]), line[4], line[5], line[6].replace('\n', '')))
    return data

def put(filename):
    with open(filename, 'w') as file:
        for val in data:
            file.write(','.join([str(i) for i in val]) + '\n')

database = sqlite3.connect('pets.db')
cursor = database.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pets
    (
        id INT,
        name TEXT,
        age INT,
        weight REAL,
        sex TEXT,
        type TEXT,
        owner TEXT
    )
''')


data = get('tests.txt')

for n in data:
    if n not in list(cursor.execute('SELECT * FROM pets')):
        cursor.execute(f'INSERT INTO pets VALUES (?,?,?,?,?,?,?)', n)
        database.commit()
        print(f'Added {n}')
    else:
        print(f'User {n} is already in the database')

for n in list(cursor.execute('SELECT * FROM pets')):
    print(n)
