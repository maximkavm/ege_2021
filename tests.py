import sqlite3

db = sqlite3.connect("1.db")
sql = db.cursor()


sql.execute("""
    CREATE TABLE IF NOT EXISTS departments
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")
db.commit()

sql.execute("""
    INSERT OR REPLACE INTO departments
    ([id], [name])
    VALUES
    (1, 'HR'),
    (2, 'Sales'),
    (3, 'Tech')
""")
db.commit()

sql.execute("""
    CREATE TABLE IF NOT EXISTS employees
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        manager_id INTEGER REFERENCES employees(id),
        departments_id INTEGER REFERENCES departments(id),
        salary INTEGER NOT NULL,
        hire_date DATETIME NOT NULL
    )
""")
db.commit()

sql.execute("""
    INSERT OR REPLACE INTO employees 
    ([id], [fname], [lname], [phone_number], [manager_id], [departments_id], [salary], [hire_date])
    VALUES
    (1, 'James', 'Smith', '12849238923', NULL, 1, 100, '01-01-2020'),
    (2, 'John', 'Johnson', '12849238924', 1, 1, 50, '01-01-2021'),
    (3, 'Michael', 'Williams', '12849238925', 1, 1, 50, '01-01-2021'),
    (4, 'Johnathan', 'Smith', '12849238926', 2, 1, 50, '01-02-2021')
""")
db.commit()