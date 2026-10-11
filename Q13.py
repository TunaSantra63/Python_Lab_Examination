"""Question 13: Employee Attendance Record 
A company stores an employee's ID, name, and attendance status 
in a tuple. Write a function that displays the record and reports 
whether the employee is present or absent."""


def employee_attendance(employee):
    for employees in employee:
            ID=employees[0]
            NAME = employees[1]
            ATTENDANCE = employees[2]
    
    
            print("Employee id : ",ID)
            print("Employee name : ",NAME)
            print("Employee present or not : ",ATTENDANCE)
    
    
            if ATTENDANCE == "YES":
                print("This employee is PRESENT")
            else:
                print("This employee in not present")
        
employee=((1123,"Tuna santra","YES"),
          (1125,"Amal roy","NO"),
          (1190,"Nilam Kumar","YES"))
    

    
employee_attendance(employee)