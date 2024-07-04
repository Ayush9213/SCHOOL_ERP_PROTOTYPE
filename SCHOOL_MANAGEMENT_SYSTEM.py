#SCHOOL MANAGEMENT SYSTEM
#SCHOOL ERP SYSTEM 
#ONLINE SOURCE CODE LINK:- https://github.com/Ayush9213/SCHOOL_ERP_PROTOTYPE
#MADE BY AYUSH KUMAR CLASS 12th

#ALL IMPORTED FUNCTIONS
import mysql.connector
import os
import time
import getpass

#def FUNCTION TO PRINT SLOWLY 
def slow_print(text, delay=0.0):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#WELCOME MESSAGE USING def FUNCTION 
def welcome():
     slow_print("********************************************************************************************************")
     slow_print("* __          __  _                        ___________                                                 *") 
     slow_print("* \ \        / / | |                      |___________|                                                *")
     slow_print("*  \ \  /\  / /__| | ___ ___  _ __ ___   ___   | | ___                                                 *")
     slow_print("*   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \  | |/ _ \                                                *")
     slow_print("*    \  /\  /  __/ | (_| (_) | | | | | |  __/  | | (_) |                                               *")
     slow_print("*     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  |_|\___/                                                *")
     slow_print("*  ____       _                 _    __  __                                                   _        *")
     slow_print("* / ___|  ___| |__   ___   ___ | |  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_      *")
     slow_print("* \___ \ / __| '_ \ / _ \ / _ \| |  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ | '_ ` _ \ / _ | '_ \| __|     *")
     slow_print("*  ___) | (__| | | | (_) | (_) | |  | |  | | (_| | | | | (_| | (_| |  __| | | | | |  __| | | | |_      *")
     slow_print("* |____/ \___|_| |_|\___/ \___/|_|  |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|     *")
     slow_print("*    ____            _                                        |___/                                    *")
     slow_print("*   / ___| _   _ ___| |_ ___ _ __ ____                                                                 *")
     slow_print("*   \___ \| | | / __| __/ _ | '_ ` _  \                                                                *")
     slow_print("*    ___) | |_| \__ | ||  __| | | | | |                                                                *")
     slow_print("*   |____/ \__, |___/\__\___|_| |_| |_|                                                                *")
     slow_print("*          |___/                                                                                       *")
     slow_print("********************************************************************************************************")
     slow_print("*   ABC GROUP OF SCHOOLS                                             MOBILE NUMBER:-- 9999########     *")
     slow_print("*   CLASS PRE-PRIMARY TO 12TH                                        ENGLISH MEDIUM                    *")
     slow_print("*   ALL SPORTS FACILITES AVAILABLE                                   RANKED 4TH IN TIMES OF INDIA      *")
     slow_print("*   JAMMU AND KASHMIR, INDIA                                         E-MAIL ID:-- abc@gmail.com        *")
     slow_print("********************************************************************************************************")
     slow_print("*   OUR MANAGMENT FEATURES:--                                                                          *")
     slow_print("*      1. STUDENT / PARENT PORTAL                                                                      *")
     slow_print("*      2. TEACHER PORTAL                                                                               *")
     slow_print("*      3. SUBMISSIION OF FEE                                                                           *")
     slow_print("*      4. RESULT GENERATOR AND MANY MORE                                                               *")
     slow_print("********************************************************************************************************")
     enter = input("PRESS ENTER KEY TO CONTINUE:--")

# ESTABLISH A DATABASE CONNECTION
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ayush",
  database="school"
)

my = mydb.cursor()

# CREATE TABLE TEACHERS IF THEY DON'EXISTS
my.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login_id VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);
""")

# CREATE TABLE STUDENTS IF THEY DON'EXISTS
my.execute("""
    CREATE TABLE IF NOT EXISTS students (
    admission_number INT PRIMARY KEY,
    classe VARCHAR(255),
    name VARCHAR(255),
    DOB INT NOT NULL,
    aadhar INT NOT NULL
);
""")

# CREATE TABLE MARKS IF THEY DON'EXISTS
my.execute("""
    CREATE TABLE IF NOT EXISTS marks (
    admission_number INT PRIMARY KEY,
    sub1 VARCHAR(255),
    mark1 INT NOT NULL,
    sub2 VARCHAR(255),
    mark2 INT NOT NULL,
    sub3 VARCHAR(255),
    mark3 INT NOT NULL,
    sub4 VARCHAR(255),
    mark4 INT NOT NULL,
    sub5 VARCHAR(255),
    mark5 INT NOT NULL,
    total_marks INT NOT NULL,
    grace VARCHAR(255),
    percentage INT NOT NULL,
    remarks VARCHAR(255),
    FOREIGN KEY (admission_number) REFERENCES students(admission_number)
    );
""")

# CREATE TABLE FEE IF THEY DON'EXISTS
my.execute("""
    CREATE TABLE IF NOT EXISTS fee (
    admission_number INT PRIMARY KEY,
    fee INT NOT NULL,
    FOREIGN KEY (admission_number) REFERENCES students(admission_number)
    );
""")

# CREATE TABLE ATTENDANCE IF THEY DON'EXISTS
my.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
    admission_number INT ,
    month varchar(255),
    present_days INT NOT NULL,
    absent_days INT NOT NULL,
    leave_days INT NOT NULL
);

""")

#FUCTION TO CLEAR SCREEN AND DELAY OF 1 SEC IN NEXT COMMAND
def clear_screen():
    os.system('cls')
    time.sleep(1)

#def FUNCTION TO ASK ABOUT USER TYPE
def ask1():
    print("******************************************")
    print("*  WHO ARE YOU?                          *")
    print("******************************************")
    print("*  1. TEACHER                            *")
    print("*  2. STUDENT / PARENTS                  *")
    print("******************************************")

#def FUNCTION TO KNOW ABOUT STUDENT STATUS
def stud():
    print("***********************************************")
    print("*    WHAT IS YOUR STATUS?                     *")
    print("***********************************************")
    print("*  1. WANT TO TAKE ADMISSION IN SCHOOL        *")
    print("*  2. EXISTING STUDENT WANT TO DO A ACTION    *")
    print("***********************************************")
    stu = int(input("ENTER YOUR CHHOICE:--"))
    if stu == 1:
        clear_screen()
        new_admission()
    else:
        clear_screen()
        existing()

#def FUNCTION FOR TEACHER PANEL
def teacher():
    print("************************************************")
    print("*                   LOGIN                      *")
    print("************************************************")
    login_id = input("Enter your login ID: ")
    password = getpass.getpass("Enter your password: ")

    my.execute("SELECT * FROM teachers WHERE login_id = %s AND password = %s", (login_id, password))
    result = my.fetchone()

    if result is not None:
        print("Login successful!")
        print()
        print("***********************************************")
        print("*    WHAT YOU WANT TO DO?                     *")
        print("***********************************************")
        print("*  1. TO ENTER THE MARKS OF THE STUDENT       *")
        print("*  2. TO CHECK STUDENT DETAILS LIST           *")
        print("*  3. TO RECORD STUDENT ATTENDANCE            *")
        print("***********************************************")
        task = int(input("ENTER YOUR TASK:--"))
        clear_screen()
        if task == 1:
            enter_marks()
        elif task == 2:
            check_student_details()
        elif task == 3:
            record_attendance()
        else:
            print("WRONG CHOICE ENTERED, EXITING...")
    else:
        print("Invalid login credentials. Access denied.")

#def FUNCTION TO TAKE FEE INPUT
def fee(): 
        clear_screen()
        print("ENTER YOUR ADMISSION NUMBER TO SUBMIT THE FEE\nAFTER ENTERING ADMISSION NUMBER YOUR FEE WILL BE DEDUCTED FROM THE REGISTERED ACCOUNT.")
        print()
        admission_number = int(input("ENTER YOUR ADMISSION NUMBER:--"))
        clear_screen()

        my.execute("SELECT name, classe FROM students WHERE admission_number = %s", (admission_number,))
        student_details = my.fetchone()

        if student_details is None:
            print("No student found with the given admission number.")
            return

        name, classe = student_details
        print("***********************************")
        print("**          FEE RECEIPT          **")
        print("***********************************")
        print(f"Student Name: {name}")
        print(f"Class: {classe}")

        classe = int(classe)

        if classe in [1, 2, 3, 4, 5, 6, 7, 8]:
           fee = 12000
        elif classe in [9, 10]:
           fee = 15000
        elif classe in [11, 12]:
           fee = 18000
        else:
           print("Class information not recognized, please check with the administration.")
           return

        my.execute("SELECT fee FROM fee WHERE admission_number = %s", (admission_number,))
        fee_record = my.fetchone()

        if fee_record is not None:
            print(f"Your fee is : {fee} for a quarter.")
            print("FEE IS SUBMITTED ALREADY")
            print("***********************************")
        else:
            print(f"Your fee is : {fee} for a quarter.")
            my.execute(
                "INSERT INTO fee (admission_number, fee) VALUES (%s, %s)",
                (admission_number, fee)
            )
            mydb.commit()
            print("FEE SUBMITTED SUCCESSFULLY")
            print("***********************************")
  
#def FUNCTION TO REGISTER MARKS OF STUDENT
def enter_marks():
    adms = int(input("ENTER STUDENT'S ADMISSION NUMBER:--"))
    print()
    my.execute("SELECT name, classe FROM students WHERE admission_number = %s", (adms,))
    STU_REC = my.fetchone()
    name, classe = STU_REC
    print("***********************************")
    print("**      REPORT CARD MAKING       **")
    print("***********************************")
    print(f"Student Name: {name}")
    print(f"Class: {classe}")
    print("***********************************") 
    print()

    my.execute("SELECT * FROM marks WHERE admission_number=%s", (adms,))
    existing_record = my.fetchone()
    if existing_record is not None:
        print("Marks are already registered for this student.")
        choice = input("Do you want to update the existing record? (yes/no):--").lower()
        if choice == "yes":
            marks_update(adms)
        elif choice == "no":
            print("EXITING...")
        else:
            print("INVALID CHOICE ENTERED, EXITING...")
    else:
        marks_enter(adms)
    take = int(input("WANT TO REGISTER MORE MARKS (1-YES / 2-NO):--"))
    if take == 1:
        clear_screen()
        enter_marks()
    else:
        print("WORK IS DONE, EXITING...")

        
#def FUNCTION TO UPDATE MARKS OF THE STUDENT        
def marks_enter(adms):
    print("ENTER SUBJECT NAME AND MARKS.")
    print()
    sub1 = input("ENTER SUBJECT-1 NAME:--")
    mark1 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub2 = input("ENTER SUBJECT-2 NAME:--")
    mark2 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub3 = input("ENTER SUBJECT-3 NAME:--")
    mark3 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub4 = input("ENTER SUBJECT-4 NAME:--")
    mark4 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub5 = input("ENTER SUBJECT-5 NAME:--")
    mark5 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    total_marks = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total_marks / 5
    grace = "Yes" if percentage < 40 else "No"

    if percentage >= 90:
        remarks = "Excellent"
    elif percentage >= 80:
        remarks = "Very Good"
    elif percentage >= 70:
        remarks = "Good"
    elif percentage >= 60:
        remarks = "Satisfactory"
    elif percentage >= 50:
        remarks = "Fair"
    else:
        remarks = "Needs Improvement"
    
    query = """
        INSERT INTO marks (admission_number, sub1, mark1, sub2, mark2, sub3, mark3,
          sub4, mark4, sub5, mark5, total_marks, grace, percentage, remarks) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (adms, sub1, mark1, sub2, mark2, sub3, mark3, sub4, mark4, sub5, mark5,
               total_marks, grace, percentage, remarks)
    
    my.execute(query, values)
    mydb.commit()
    print("MARKS REGISTERED SUCCESSFULLY")

        
#def FUNCTION TO ADD MARKS OF A STUDENT        
def marks_update(adms):
    print("ENTER SUBJECT NAME AND MARKS.")
    print()
    sub1 = input("ENTER SUBJECT-1 NAME:--")
    mark1 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub2 = input("ENTER SUBJECT-2 NAME:--")
    mark2 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub3 = input("ENTER SUBJECT-3 NAME:--")
    mark3 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub4 = input("ENTER SUBJECT-4 NAME:--")
    mark4 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    sub5 = input("ENTER SUBJECT-5 NAME:--")
    mark5 = int(input("ENTER MARKS OBTAINED:--"))
    print()
    total_marks = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total_marks / 5
    grace = "Yes" if percentage < 40 else "No"
    
    if percentage >= 90:
        remarks = "Excellent"
    elif percentage >= 80:
        remarks = "Very Good"
    elif percentage >= 70:
        remarks = "Good"
    elif percentage >= 60:
        remarks = "Satisfactory"
    elif percentage >= 50:
        remarks = "Fair"
    else:
        remarks = "Needs Improvement"
            
    query = """
        UPDATE marks 
        SET sub1=%s, mark1=%s, sub2=%s, mark2=%s, sub3=%s, mark3=%s, 
            sub4=%s, mark4=%s, sub5=%s, mark5=%s, total_marks=%s, grace=%s, 
            percentage=%s, remarks=%s 
        WHERE admission_number = %s
    """
    values = (sub1, mark1, sub2, mark2, sub3, mark3, sub4, mark4, sub5, mark5, 
              total_marks, grace, percentage, remarks, adms)
    
    my.execute(query, values)
    mydb.commit()
    print("Marks record updated successfully.")


        
#def FUNCTION TO TAKE NEW ADMISSION
def new_admission():
    cls = input("IN WHICH CLASS WOULD YOU WANT TO TAKE THE ADMISSION:--")
    name = input("ENTER STUDENT'S NAME:--")
    dob = int(input("ENTER STUDENT'S DATE OF BIRTH (only year) :--"))
    aadhar = int(input("ENTER STUDENT AADHAAR CARD NUMBER:--"))


    my.execute("SELECT MAX(admission_number) FROM students")
    result = my.fetchone()
    if result[0] is None:
        admission_number = 1001
    else:
        admission_number = result[0] + 1

    my.execute("INSERT INTO students (admission_number, classe, name, DOB, aadhar) VALUES (%s, %s, %s, %s, %s)",
               (admission_number, cls, name, dob, aadhar))
    mydb.commit()
    
    clear_screen()
    print("YOUR ADMISSION HAS BEEN DONE") 
    print("YOUR ADMISSION NUMBER IS", admission_number)
    print("BE REMEMBER YOUR ADMISSION NUMBER TO ACCESS ERP.")

#def FUNCTION FOR CHECKING STUDENT DETAILS
def check_student_details():
    my.execute("SELECT * FROM students")
    for (admission_number, classe, name, DOB, aadhar) in my:
        print(f"Admission Number: {admission_number}, Class: {classe}, Name: {name}, DOB: {DOB}, Aadhar: {aadhar}")
    input("Press Enter to continue...")

#def FUNCTION TO REGISTER STUDENT ATTENDANCE
def record_attendance():
    admission_number = int(input("Enter student's admission number: "))
    month = input("Enter month: ")

    my.execute("SELECT * FROM attendance WHERE admission_number=%s AND month=%s", (admission_number, month))
    existing_record = my.fetchone()

    if existing_record is not None:
        print("Attendance record already exists for this month.")
        choice = input("Do you want to update the existing record? (yes/no): ").lower()
        if choice == "yes":
            present_days = int(input("Enter number of present days: "))
            absent_days = int(input("Enter number of absent days: "))
            leave_days = int(input("Enter number of leave days: "))

            my.execute("UPDATE attendance SET present_days=%s, absent_days=%s, leave_days=%s WHERE admission_number=%s AND month=%s",
                       (present_days, absent_days, leave_days, admission_number, month))
            mydb.commit()
            print("Attendance record updated successfully.")
        else:
            print("No changes made to the existing record.")
    else:
        present_days = int(input("Enter number of present days: "))
        absent_days = int(input("Enter number of absent days: "))
        leave_days = int(input("Enter number of leave days: "))
        my.execute("INSERT INTO attendance (admission_number, month, present_days, absent_days, leave_days) VALUES (%s, %s, %s, %s, %s)",
                   (admission_number, month, present_days, absent_days, leave_days))
        mydb.commit()
        print("Attendance recorded successfully.")

    take1 = int(input("WANT TO REGISTER MORE RECORD (1-YES / 2-NO):--"))
    if take1 == 1:
        clear_screen()
        record_attendance()
    else:
        print("WORK IS DONE, EXITING...")

#def FUNCTION FOR EXISTING STUDENTS
def existing():
    print("******************************************************")
    print("*            WHAT WOULD YOU WANT TO DO?              *")
    print("******************************************************")
    print("*  1. WANT TO SUBMIT FEE                             *")
    print("*  2. WANT TO SEE RESULT                             *")
    print("*  3. WANT TO UPDATE YOUR DETAILS IN SCHOOL REGISTER *")
    print("*  4. WANT TO CHECK ATTENDANCE                       *")
    print("******************************************************")
    ex = int(input("ENTER YOUR CHOICE:--"))
    if ex == 1:
        fee()
    elif ex == 2:
        see_result()
    elif ex == 3:
        update_details()
    elif ex == 4:
        check_attendance()
    else:
        print("WRONG CHOICE ENTERED")

#def FUNCTION TO SEE RESULTS
def see_result():
    clear_screen()
    admission_number = int(input("ENTER YOUR ADMISSION NUMBER:--"))
    clear_screen()
    my.execute("SELECT name, classe FROM students WHERE admission_number=%s", (admission_number,))
    student_details = my.fetchone()

    my.execute("SELECT * FROM marks WHERE admission_number=%s", (admission_number,))
    result = my.fetchone()

    if student_details and result is not None:
        name, classe = student_details
        print("*****************************************************")
        print("**                   REPORT CARD                   **")
        print("*****************************************************")
        print(f"* NAME: {name}")
        print(f"* CLASS: {classe}")
        print("*****************************************************")
        print(f"* SUBJECT 1: {result[1]},         MARKS: {result[2]}")
        print(f"* SUBJECT 2: {result[3]},         MARKS: {result[4]}")
        print(f"* SUBJECT 3: {result[5]},         MARKS: {result[6]}")
        print(f"* SUBJECT 4: {result[7]},         MARKS: {result[8]}")
        print(f"* SUBJECT 5: {result[9]},         MARKS: {result[10]}")
        print("*****************************************************")
        print(f"* TOTAL MARKS: {result[11]}")
        print(f"* GRACE: {result[12]}")
        print(f"* PERCENTAGE: {result[13]}")
        print(f"* REMARKS: {result[14]}")
        print("*****************************************************")
    else:
        print("NO RESULT FOUND")
        print()
        print("PROBABLY YOUR RESULT IS IN PROGRESS.")
        print()
        print("DO NOT BE WORRY KEEP STUDING")


#def FUNCTION TO UPDATE DETAILS
def update_details():
    clear_screen()
    admission_number = int(input("ENTER YOUR ADMISSION NUMBER:--"))
    print()
    field = input("ENTER THE FIELD YOU WANT TO UPDATE (name/classe/DOB/aadhar):--")
    print()
    new_value = input("ENTER THE NEW VALUE:--")
    my.execute(f"UPDATE students SET {field} = %s WHERE admission_number = %s", (new_value, admission_number))
    mydb.commit()
    print("DETAILS UPDATED SUCCESSFULLY")
    print()
    more = int(input("WANT TO CHANGE MORE (1-yes / 2-no):"))
    if more == 1:
        update_details()
    else:
        ("EXITING...") 

#def FUNCTION TO CHECK DETAILS
def check_attendance():
    clear_screen()
    print("ENTER YOUR ADMISSION NUMBER AND MONTH NAME OF WHICH YOU WANT TO SEE THE ATTENADANCE:--")
    admission_number = int(input("Enter your admission number: "))
    month = input("Enter month: ")
    my.execute("SELECT * FROM attendance WHERE admission_number=%s AND month=%s", (admission_number, month))
    result = my.fetchone()
    if result:
        print()
        print("*****************************")
        print("*     PRESENT DAYS:", result[2])
        print("*     ABSENT DAYS:", result[3])
        print("*     LEAVE DAYS:", result[4])
        print("*****************************")
    else:
        print("No attendance record found for the given month.")
    print()
    chk = int(input("WANT TO CHECK MORE (1-yes / 2-no):"))
    if chk == 1:
        check_attendance()
    else:
        ("EXITING...")

#IMPLEMENTATION OF ALL FUNCTIONS
clear_screen()
welcome()
clear_screen()
ask1()
ask = int(input("ENTER YOUR CHOICE:--"))
clear_screen()
if ask == 1:
    teacher()
elif ask == 2:
    stud()
else:
    print("WRONG CHOICE ENTERED")

