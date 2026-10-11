"""Section B: Python Tuple — Questions 8–13 
Question 8: Student Registration Record 
A college stores a student's roll number, name, course, and 
semester in a tuple. Write a function that displays each field 
separately and prints the complete student record."""

def student_records(students):
    for student in students:
        print("Roll no : ",student[0])
        print("Name : ",student[1])
        print("Course : ",student[2])
        print("Semester : ",student[3])
        print("Complete student records",student)
    
students= ((10,"Tuna santra","MCA",2),
        (20,"Ajay santra","BCA",3),
        (30,"Priya kumari","BTECH",4),
        (40,"D kumar","BBA",5)
)
student_records(students)