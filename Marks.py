'''Question 1: Student Marks Analysis 
A college stores students' marks in a list. Write a function that 
accepts a list of marks and displays the highest mark, lowest 
mark, average mark, and number of students who passed (marks 
of 40 or above).'''


def analyze_marks(marks): 
    count=0
    highest= max(marks)
    lowest=min(marks)
    average = sum(marks) / len(marks)
    for mark in marks:
        if (mark<=40):
            count=count+1
        
        
    print("Highest Number is : ",highest)
    print("Lowest Number is : ",lowest)
    print("Average Number is : ",average)
analyze_marks([78, 35, 92, 45, 60, 28, 88])
