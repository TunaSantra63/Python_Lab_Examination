'''Question 4: Employee Salary Analysis 
A company stores employee salaries in a list. Write a function to 
calculate the average salary, display salaries above the average, 
and increase every salary by 10%.'''


def emp_salary(salary):
    average_salary=sum(salary) / len(salary)
    print("average_salary", average_salary)
    for sal in salary:
        if sal>average_salary:
            print("Salaries above the average : ",sal)
    increased_salary = [sal * 1.10 for sal in salary]
    print("Salary after 10% increase:", increased_salary)
    



emp_salary([15000,20000,25000,30000,35000,50000,100000])
