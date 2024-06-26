import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ayush",
  database="school"
)

my = mydb.cursor()



my.execute("""
      INSERT INTO students (admission_number, class_group, actual_class, name, DOB, aadhar)
      VALUES
      (1001, '2', 1, 'Aadhya Sharma', 2007, 2348903),
      (1002, '2', 5, 'Aadhya Sharma', 2007, 2348903),
      (1003, '3', 11, 'Advik Singh', 2009, 3458934),
      (1004, '3', 11, 'Ananya Patel', 2000, 4812345),
      (1005, '3', 11, 'Aradhya Gupta', 2005, 8901236);
 """)

mydb.commit()

my.execute("""
     INSERT INTO marks (admission_number, sub1, mark1, sub2, mark2, sub3, mark3, sub4, mark4, sub5, mark5, total_marks, grace, percentage, remarks)
     VALUES
     (1001, 'Math', 78, 'Science', 60, 'English', 88, 'History', 42, 'Geography', 79, 394, 'No', 78.8, 'Very Good'),       
     (1002, 'Math', 75, 'Science', 80, 'English', 78, 'History', 82, 'Geography', 79, 394, 'No', 78.8, 'Very Good'),
     (1003, 'Math', 65, 'Science', 70, 'English', 68, 'History', 72, 'Geography', 69, 344, 'No', 68.8, 'Good'),
     (1004, 'Math', 55, 'Science', 60, 'English', 58, 'History', 62, 'Geography', 59, 294, 'No', 58.8, 'Satisfactory'),
     (1005, 'Math', 95, 'Science', 96, 'English', 98, 'History', 94, 'Geography', 97, 480, 'No', 96, 'Excellent');
 """)

mydb.commit()

my.execute("""
    INSERT INTO fee (admission_number, fee)
    VALUES
    (1001, 15000)
    (1002, 15000),
    (1003, 18000),
    (1004, 18000),
    (1005, 18000);
""")

mydb.commit()

my.execute("""
    INSERT INTO attendance (admission_number, month, present_days, absent_days, leave_days)
    VALUES
    (1001, 'January', 18, 3, 2),
    (1001, 'February', 18, 1, 3),
    (1001, 'March', 21, 0, 0),
    (1002, 'January', 18, 3, 2),
    (1002, 'February', 20, 1, 2),
    (1002, 'March', 22, 0, 1),
    (1003, 'January', 22, 1, 0),
    (1003, 'February', 19, 0, 4),
    (1003, 'March', 20, 2, 1),
    (1004, 'January', 19, 2, 2),
    (1004, 'February', 18, 1, 3),
    (1004, 'March', 21, 1, 0),
    (1005, 'January', 20, 0, 2),
    (1005, 'February', 22, 1, 0),
    (1005, 'March', 20, 1, 1);
""")

mydb.commit()