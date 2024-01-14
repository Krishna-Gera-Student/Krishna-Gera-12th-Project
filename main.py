import mysql.connector as sqltor

# Establishing a connection to the MySQL database
mycon = sqltor.connect(host="localhost", user="root", passwd="krish8125", database="school")

# Checking if the connection is successful
if mycon.is_connected():
    print('Welcome to School Portal')
    # Creating a cursor to execute SQL queries
    cursor = mycon.cursor()
    # SQL statement to create the 'student' table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS student (
        SchNo INT,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Class INT,
        Section CHAR(1),
        House VARCHAR(10),
        Age INT,
        English INT,
        Computer INT,
        Physics INT,
        Chemistry INT,
        Maths INT,
        TotalMarks INT,
        Percentage INT,
        Grade CHAR(1)
    )
    """

    # Executing the create table query
    cursor.execute(create_table_query)
# Flag to track login status
login_status = False

# Admin Portal function
def admin():
    while True:
        global login_status 
        if not login_status:
            print(" Welcome to School Admin Portal")
            passwd = input("Enter the Admin Password: ")
            if passwd == "admin":
                login_status = True
                print("""
                    1 for Adding Student Record
                    2 for Deleting Student Record
                    3 for Search for a Student Record
                    4 for Display records of all Students
                    5 for Exit""")
                task = input("What task do you like to perform? : ")
                if task == '1':
                    add()
                    continue
                elif task == '2':
                    delete()
                    continue
                elif task == '3':
                    search()
                    continue
                elif task == '4':
                    display()
                    continue
                elif task == '5':
                    print("Bye bye!")
                    login_status = False  # Logout when exiting
                    break  # Exit the loop and go back
                else:
                    print("Select the task correctly........")
            else:
                print("Incorrect password. Please enter again.")
                login_status = False
        else:
            print("Already logged in as Admin.")
            print("""
                1 for Adding Student Record
                2 for Deleting Student Record
                3 for Search for a Student Record
                4 for Display records of all Students
                5 for Exit""")
            task = input("What task do you like to perform? : ")
            if task == '1':
                add()
                continue
            elif task == '2':
                delete()
                continue
            elif task == '3':
                search()
                continue
            elif task == '4':
                display()
                continue
            elif task == '5':
                print("Bye bye!")
                login_status = False  # Logout when exiting
                break  # Exit the loop and go back
            else:
                print("Select the task correctly........")

# Teacher Portal function
def teacher():
    while True:
        global login_status
        
        if not login_status:
            print(" Welcome to School Teacher Portal")
            passwd = input("Enter the Teacher Login Password: ")
            if passwd == "teacher":
                login_status = True
                print("""
                1 for Adding Student Marks
                2 for Search for a Student Record
                3 for Display records of all Students
                4 for Exit""")
                task = input("What task do you like to perform? : ")
                if task == '1':
                    edit()
                elif task == '2':
                    search()
                elif task == '3':
                    display()
                elif task == '4':
                    print("Bye bye!")
                    login_status = False  # Logout on exiting
                    break  # Exit the loop and go back
                else:
                    print("Select the task correctly........")
                    login_status = False
            else:
                print("Incorrect password. Please enter again.")
                login_status = False
        else:
            print("Already logged in as Teacher.")
            print("""
                1 for Adding Student Marks
                2 for Search for a Student Record
                3 for Display records of all Students
                4 for Exit""")
            task = input("What task do you like to perform? : ")
            if task == '1':
                edit()
            elif task == '2':
                search()
            elif task == '3':
                display()
            elif task == '4':
                print("Bye bye!")
                login_status = False  # Logout on exiting
                break  # Exit the loop and go back
            else:
                print("Select the task correctly........")
                login_status = False

# Student Portal function
def student():
    while True:
        print(" Welcome to School Student Portal")
        print("""
              1 for Checking your Report Card
              2 for exit""")
        task = input("What task do you like to perform? : ")
        if task == '1':
            search()
        elif task == '2':
            print("Bye bye!")
            break  # Exit the loop and go back
        else:
            print("Select the task correctly........")

# Function to add student data
def add():
    n = int(input("How many students do you want to add data for: "))
    for i in range(n):
        print("Add data of Student", i+1)
        schno = int(input("Enter the Scholar No.: "))
        FName = input("Enter First Name: ")
        LName = input("Enter Last Name: ")
        Class = int(input("Enter Class: "))
        Section = input("Enter Section: ").capitalize()
        House = input("Enter House: ").capitalize()
        Age = int(input("Enter Age: "))
        add_student_query = ("INSERT INTO student (SchNo, FirstName, LastName, Class, Section, House, Age) VALUES (%s, '%s', '%s', %s, '%s', '%s', %s)" %(schno, FName, LName, Class, Section, House, Age))
        cursor.execute(add_student_query)
        mycon.commit()
        print("Student Data Added successfully!")

# Function to edit student marks
def edit():
    print("Enter Marks of Student")
    schno = int(input("Enter the Scholar No.: "))
    check_query = ("SELECT * FROM student WHERE SchNo = %s" %(schno))
    cursor.execute(check_query)
    result = cursor.fetchone()
    if result is not None:   
        Eng = int(input("Enter English Marks: "))
        Comp = int(input("Enter Computer Marks: "))
        Phy = int(input("Enter Physics Marks: "))
        Chem = int(input("Enter Chemistry Marks: "))
        Maths = int(input("Enter Maths Marks: "))
        TotalMarks = Eng+Comp+Phy+Chem+Maths
        Percentage = TotalMarks/5
        Grade = ''
        if 90 <= Percentage <= 100:
            Grade = 'A'
        elif 80 <= Percentage < 90:
            Grade = 'B'
        elif 60 <= Percentage < 80:
            Grade = 'C'
        elif 40 <= Percentage < 60:
            Grade = 'D'
        else:
            Grade = 'F'
        update_marks_query = ("UPDATE student SET English = %s, Computer = %s, Physics = %s, Chemistry = %s, Maths = %s, TotalMarks = %s, Percentage = %s, Grade = '%s' WHERE SchNo = %s" %(Eng, Comp, Phy, Chem, Maths, TotalMarks, Percentage, Grade, schno))
        cursor.execute(update_marks_query)
        mycon.commit()
        print("Marks updated successfully!")
    else:
        print(f"Student with SchNo {schno} does not exist in the database.")

# Function to delete a student record
def delete():
    schno = int(input("Enter the Scholar No.: "))
    delete_record_query = "DELETE FROM student WHERE SchNo = %s " %(schno)
    cursor.execute(delete_record_query)
    mycon.commit()
    print(f"Record of Student with {schno} Deleted!!")

# Function to search for a student record
def search():
    schno = int(input("Enter the Scholar No.: "))
    search=("SELECT * FROM student  WHERE schno=%s" %(schno))
    print(f"Record of Student with {schno}")
    cursor.execute(search)
    result = cursor.fetchone()
    if result:
            print("SchNo:", result[0])
            print("FirstName:", result[1])
            print("LastName:", result[2])
            print("Class:", result[3])
            print("Section:", result[4])
            print("House:", result[5])
            print("Age:", result[6])
            print("English:", result[7])
            print("Computer:", result[8])
            print("Physics:", result[9])
            print("Chemistry:", result[10])
            print("Maths:", result[11])
            print("TotalMarks:", result[12])
            print("Percentage:", result[13])
            print("Grade:", result[14])
    else:
            print(f"No record found for Scholar No. {schno}")

# Function to display student records
def display():
    print('''
          1 for Display all records
          2 for Display records with filters''')
    n = input("Enter your choice: ")
    if n == '1':
        print("ALL RECORDS")
        cursor.execute('SELECT * FROM student ORDER BY Schno ASC')
        print(
            f"{'SchNo':<6} {'FirstName':<12} {'LastName':<12} {'Class':<6} {'Section':<6} "
            f"{'House':<11} {'Age':<6} {'English':<8} {'Computer':<8} {'Physics':<8} "
            f"{'Chemistry':<8} {'Maths':<6} {'TotalMarks':<8} {'Percentage':<8} {'Grade':<6}"
        )
        print("-" * 140)
        while True:
            result = cursor.fetchone()
            if result is not None:
                schno = result[0] if result[0] is not None else 'None'
                fname = result[1] if result[1] is not None else 'None'
                lname = result[2] if result[2] is not None else 'None'
                class_val = result[3] if result[3] is not None else 'None'
                section = result[4] if result[4] is not None else 'None'
                house = result[5] if result[5] is not None else 'None'
                age = result[6] if result[6] is not None else 'None'
                english = result[7] if result[7] is not None else 'None'
                computer = result[8] if result[8] is not None else 'None'
                physics = result[9] if result[9] is not None else 'None'
                chemistry = result[10] if result[10] is not None else 'None'
                maths = result[11] if result[11] is not None else 'None'
                total_marks = result[12] if result[12] is not None else 'None'
                percentage = result[13] if result[13] is not None else 'None'
                grade = result[14] if result[14] is not None else 'None'

                print(
                    f"{schno:<6} {fname:<12} {lname:<12} {class_val:<6} {section:<6} "
                    f"{house:<11} {age:<6} {english:<8} {computer:<8} {physics:<8} "
                    f"{chemistry:<8} {maths:<6} {total_marks:<8} {percentage:<8} {grade:<6}"
                )
            else:
                print('No More Records Found')
                break 
    elif n == '2':
        print("RECORDS WITH FILTER")
        filter_by = input("""How do you wanna filter the data 
                    [1 for Class; 2 for Class & Sec; 3 for House; 4 Class & House] : """)
        filter_query = "SELECT * FROM student WHERE %s"
        if filter_by == '1':
            Class = int(input("Enter the Class [1 to 12]: "))
            filter_as = 'CLASS = %s' % Class
        elif filter_by == '2':
            Class = int(input("Enter the Class [1 to 12]: "))
            Sec = input("Enter the Section: ")
            filter_as = "CLASS = %s AND Section = '%s'" % (Class, Sec)
        elif filter_by == '3':
            select_house = input("Select the House [1 for Maple; 2 for Cypress, 3 for Westeria, 4 for Elm]: ")
            if select_house == '1':
                House = 'Maple'
            elif select_house == '2':
                House = 'Cypress'
            elif select_house == '3':
                House = 'Westeria'
            elif select_house == '4':
                House = 'Elm'
            filter_as = "House = '%s'" % House
        elif filter_by == '4':
            Class = int(input("Enter the Class [1 to 12]: "))
            select_house = input("Select the House [1 for Maple; 2 for Cypress, 3 for Westeria, 4 for Elm]: ")
            if select_house == '1':
                House = 'Maple'
            elif select_house == '2':
                House = 'Cypress'
            elif select_house == '3':
                House = 'Westeria'
            elif select_house == '4':
                House = 'Elm'
            filter_as = "CLASS = %s AND HOUSE = '%s'" % (Class, House)
        cursor.execute(filter_query % filter_as)
        print(
            f"{'SchNo':<6} {'FirstName':<12} {'LastName':<12} {'Class':<6} {'Section':<6} "
            f"{'House':<11} {'Age':<6} {'English':<8} {'Computer':<8} {'Physics':<8} "
            f"{'Chemistry':<8} {'Maths':<6} {'TotalMarks':<8} {'Percentage':<8} {'Grade':<6}"
        )
        print("-" * 140)
        while True:
            result = cursor.fetchone()
            if result is not None:
                schno = result[0] if result[0] is not None else 'None'
                fname = result[1] if result[1] is not None else 'None'
                lname = result[2] if result[2] is not None else 'None'
                class_val = result[3] if result[3] is not None else 'None'
                section = result[4] if result[4] is not None else 'None'
                house = result[5] if result[5] is not None else 'None'
                age = result[6] if result[6] is not None else 'None'
                english = result[7] if result[7] is not None else 'None'
                computer = result[8] if result[8] is not None else 'None'
                physics = result[9] if result[9] is not None else 'None'
                chemistry = result[10] if result[10] is not None else 'None'
                maths = result[11] if result[11] is not None else 'None'
                total_marks = result[12] if result[12] is not None else 'None'
                percentage = result[13] if result[13] is not None else 'None'
                grade = result[14] if result[14] is not None else 'None'

                print(
                    f"{schno:<6} {fname:<12} {lname:<12} {class_val:<6} {section:<6} "
                    f"{house:<11} {age:<6} {english:<8} {computer:<8} {physics:<8} "
                    f"{chemistry:<8} {maths:<6} {total_marks:<8} {percentage:<8} {grade:<6}"
                )
            else:
                print('No More Records Found')
                break
    else:
        print("Select the task correctly........")
        display()

# Main loop for user interaction
while True:
    print('''
          1 for Admin
          2 for Teacher
          3 for Student''')
    user_type = input("Please select your user type: ")
    if user_type == '1':
        admin()
        break
    elif user_type == '2':
        teacher()
        break
    elif user_type == '3':
        student()
        break
    else:
        print("Select the user type correctly........")
        print("........Restarting........")

# Closing the database connection after the main loop
mycon.close()