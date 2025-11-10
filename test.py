import psycopg2
connect  = psycopg2.connect(dbname="postgres", user="postgres", password="8083", host="localhost", port="5432")

cursor = connect.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            Name TEXT,
            Id INT,
            Age INT
        );
    ''')
print("Table created successfully")
connect.commit()
connect.close()


print('Connection successful')