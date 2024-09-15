import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('students.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        roll_number INTEGER NOT NULL UNIQUE,
                        marks REAL NOT NULL);''')
    conn.commit()

def add_student(conn, student):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, roll_number, marks) VALUES (?, ?, ?)", student)
    conn.commit()

def update_student(conn, student):
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, marks=? WHERE roll_number=?", student)
    conn.commit()

def delete_student(conn, roll_number):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_number=?", (roll_number,))
    conn.commit()

def search_student(conn, roll_number):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_number=?", (roll_number,))
    return cursor.fetchone()

def get_all_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        while True:
            print("\n1. Add student")
            print("2. Update student")
            print("3. Delete student")
            print("4. Search student")
            print("5. Show all students")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter student name: ")
                roll_number = int(input("Enter student roll number: "))
                marks = float(input("Enter student marks: "))
                add_student(conn, (name, roll_number, marks))
            elif choice == 2:
                name = input("Enter new student name: ")
                marks = float(input("Enter new student marks: "))
                roll_number = int(input("Enter student roll number to update: "))
                update_student(conn, (name, marks, roll_number))
            elif choice == 3:
                roll_number = int(input("Enter student roll number to delete: "))
                delete_student(conn, roll_number)
            elif choice == 4:
                roll_number = int(input("Enter student roll number to search: "))
                student = search_student(conn, roll_number)
                if student is not None:
                    print(f"Student name: {student[1]}, Roll Number: {student[2]}, Marks: {student[3]}")
                else:
                    print("Student not found")
            elif choice == 5:
                students = get_all_students(conn)
                for student in students:
                    print(f"Student name: {student[1]}, Roll Number: {student[2]}, Marks: {student[3]}")
            elif choice == 6:
                break
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()


