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

def delete_contact():
    name = input("Enter name for delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Number is deleted")

#Lab 11: 1)
def search_by_pattern():
    pattern = input("Enter pattern to search (part of name or phone): ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No matches found.")
    cur.close()
    conn.close()
# 2)
def insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("User inserted or updated successfully.")
#3.
def insert_many_users():
    num_users = int(input("How many users do you want to insert? "))
    
    names = []
    phones = []
    
    for _ in range(num_users):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        
        names.append(name)
        phones.append(phone)
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()
    
    cur.close()
    conn.close()
    
    print("Users inserted or updated successfully.")
#4.

def get_paginated_contacts():
    limit = int(input("Enter limit (how many records to show): "))
    offset = int(input("Enter offset (how many records to skip): "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_with_pagination(%s, %s)", (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
#5

def delete_by_name_or_phone():
    name = input("Enter name (or leave empty): ")
    phone = input("Enter phone (or leave empty): ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user_by_name_or_phone(%s, %s)", (name if name else None, phone if phone else None))
    conn.commit()
    cur.close()
    conn.close()
    print("User(s) deleted successfully.")

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
        print("7. Search by pattern (using SQL function)")
        print("8. Insert or update user (using procedure)")
        print("9. Insert many users (with validation)")
        print("10. Get contacts with pagination")
        print("11. Delete by name or phone (procedure)")
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
            print("Leaving...")
            break
        elif choice == "7":
            search_by_pattern()
        elif choice == "8":
            insert_or_update()
        elif choice == "9":
            insert_many_users()
        elif choice == "10":
            get_paginated_contacts()
        elif choice == "11":
            delete_by_name_or_phone()
        else:
            print("Error number, try again.")




if __name__ == "__main__":
    menu()