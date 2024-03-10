pw="Turnbull01!"



# Zoltan Biro  
# 101220698

import psycopg


with psycopg.connect(f"dbname=COMP3005a3q1 user=postgres password={pw}") as conn:
    with conn.cursor() as cur:

        def getAllStudents():
            cur.execute("SELECT * FROM students;")
            print()
            for record in cur:
                print(record)
            print()

        def addStudent(first_name, last_name, email, enrollment_date):
            cur.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');")
            print("Entry added Successfully\n")

        def updateStudentEmail(student_id, new_email):
            cur.execute(f"UPDATE students SET email='{new_email}' WHERE student_id={int(student_id)};")
            print("Entry updated successfully\n")

        def deleteStudent(student_id):
            cur.execute(f"DELETE FROM students WHERE student_id={int(student_id)};")
            print("Entry deleted successfully\n")

        option =0
        while (option !="5"):
            option = input("""Choose a function to use:
    1. getAllStudents()
    2. addStudent(first_name, last_name, email, enrollment_date)
    3. updateStudentEmail(student_id, new_email)
    4. deleteStudent(student_id)
    5. quit
    Input a single number: """)
            
            if(option=="1"):
                getAllStudents()
            if(option=="2"):
                args=input("Enter the arguments separated by spaces: ")
                args=args.split()
                if(len(args)!=4):
                    print("Please enter 4 and only 4 arguments")
                else:
                    addStudent(args[0],args[1],args[2],args[3])
            if(option=="3"):
                args=input("Enter the arguments separated by spaces: ")
                args=args.split()
                if(len(args)!=2):
                    print("Please enter 2 and only 2 arguments")
                else:
                    updateStudentEmail(args[0],args[1])
            if(option=="4"):
                args=input("Enter the argument: ")
                if(len(args)!=1):
                    print("Please enter 1 and only 1 arguments")
                else:
                    deleteStudent(args)
        conn.commit()                   



