import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('chenmed_demo.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
''')

# Create patients table
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    condition TEXT,
    treatment TEXT
)
''')

# Insert sample data into the employees table
cursor.executemany('''
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
''', [
    ('John Doe', 'Engineering', 90000),
    ('Jane Smith', 'Marketing', 75000),
    ('Emily Davis', 'Finance', 80000)
])

# Insert sample data into the patients table
cursor.executemany('''
INSERT INTO patients (name, age, condition, treatment)
VALUES (?, ?, ?, ?)
''', [
    ('Alice Brown', 68, 'Hypertension', 'Medication A'),
    ('Bob Johnson', 72, 'Diabetes', 'Insulin'),
    ('Carol White', 65, 'Arthritis', 'Physical Therapy')
])

# Commit the changes and close the connection
conn.commit()
conn.close()
