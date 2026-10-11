"""Question 14: Student Result Management 
A college stores student names and marks in a dictionary. Write a 
function that displays each student's result, calculatesQuestion the class average, and identifies students who scored at least 75 
marks. """


def student_result(student):
    total =0
    for name,marks in student.items():
        print("Student name : ",name)
        print("student marks : ",marks)
        
        if(marks>=40):
            print("Pass")
        else:
            print("fail")
        
        total=total+marks
        average = total/ len(student)
        
    print("\n students who has marks up to 75%")
    for name,marks in student.items():
        if marks>=75:
            print(name,":",marks)
    
student={"Tanay das":70,
         "Mainak roy": 80,
         "Anuj gain":60,
         "rittika roy":30}    
student_result(student)