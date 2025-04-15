import psycopg2
import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def connect():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",       
        password="Nurik43156.",       
        host="localhost"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table created.")

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", row)
    conn.commit()
    cur.close()
    conn.close()
    print("CSV is downloaded.")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter number: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Number has been added")

def update_contact():
    name = input("Enter name for update: ")
    new_phone = input("Enter new number: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Number updated.")

# Поиск
def search_contact():
    name = input("Enter name for search: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()

# Удаление
def delete_contact():
    name = input("Enter name for delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Number is deleted")

# Меню
def menu():
    create_table()
    while True:
        print("\n=== Phonebook ===")
        print("1. Download from CSV file")
        print("2. Download with console")
        print("3. Update number")
        print("4. Search number")
        print("5. Delete number")
        print("6. Leave")
        choice = input("Choose action: ")
        
        if choice == "1":
            insert_from_csv('contacts.csv')
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Выход...")
            break
        else:
            print("Error number, try again.")

if __name__ == "__main__":
    menu()