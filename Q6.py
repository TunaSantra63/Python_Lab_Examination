'''Question 6: Hospital Patient Queue 
A hospital maintains a list of patients waiting for consultation. 
Write a function that removes the first patient after consultation, 
adds a new patient to the queue, and displays the updated queue.'''

'''Question 6: Hospital Patient Queue'''

def patient_queue(patients):
    
    print(patients)
   
    patients.pop(0)

    patients.append("Rahul")

    
    print("Updated patient queue:", patients)


patient_queue(["Amit", "Priya", "Riya", "Suman"])