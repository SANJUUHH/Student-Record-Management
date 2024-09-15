# Student Record Management System

This Python project provides a console-based student record management system using SQLite as the database. It allows users to perform the following operations:

- Add a student
- Update student details
- Delete a student
- Search for a student
- Show all students

## Features
1. **Add a student**: Insert a new student record.
2. **Update student details**: Modify the name and marks of a student by roll number.
3. **Delete a student**: Remove a student by roll number.
4. **Search for a student**: Retrieve a student's details by roll number.
5. **Show all students**: Display all student records in the database.

## Technologies Used
- **Language**: Python
- **Database**: SQLite

## Prerequisites
- Python 3.x
- SQLite3

## How to Run

1. Clone or download the repository.
2. Open the terminal or command prompt in the project folder.
3. Run the following command:

    ```bash
    python student_management.py
    ```

## How to Use

1. **Run the script** and you will see a menu with several options:
   - Add student
   - Update student
   - Delete student
   - Search student
   - Show all students
   - Exit
   
2. Choose the desired action by typing the corresponding number and following the prompts.

3. When adding, updating, or searching for a student, you'll be asked to provide specific information like the student's name, roll number, and marks.

4. The program will continue to loop until you choose to exit.

## Example Output

1. Adding a Student
   ```plaintext
    1. Add student
    2. Update student
    3. Delete student
    4. Search student
    5. Show all students
    6. Exit
    Enter your choice: 1
    Enter student name: John Doe
    Enter student roll number: 101
    Enter student marks: 85.5

The student has been added successfully!

2. Updating a Student's Information
   ```plaintext
    1. Add student
    2. Update student
    3. Delete student
    4. Search student
    5. Show all students
    6. Exit
    Enter your choice: 2
    Enter new student name: Jane Doe
    Enter new student marks: 90.0
    Enter student roll number to update: 101

 The student details have been updated successfully!

3. Searching for a Student
   ```plaintext
    1. Add student
    2. Update student
    3. Delete student
    4. Search student
    5. Show all students
    6. Exit
    Enter your choice: 4
    Enter student roll number: 101

    Student name: Jane Doe, Roll Number: 101, Marks: 90.0

4. Deleting a Student
   ```plaintext
    1. Add student
    2. Update student
    3. Delete student
    4. Search student
    5. Show all students
    6. Exit
    Enter your choice: 3
    Enter student roll number to delete: 101

  The student has been deleted successfully!

5. Showing All Students (Empty Table)
   ```plaintext
    1. Add student
    2. Update student
    3. Delete student
    4. Search student
    5. Show all students
    6. Exit
    Enter your choice: 5

  No student records found.

