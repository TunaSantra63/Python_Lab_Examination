"""Question 7: Daily Expense Tracker 
A person records daily expenses in a list. Write a function to 
calculate the total expenses, average daily expense, and the days 
on which expenses exceeded ₹1,000."""

def Daily_expenses(expenses):
    total_expenses = sum(expenses)
    daily_expenses = sum(expenses)/ len(expenses)
    
    print("The total expenses is : ",total_expenses)
    print("The average of daily expences : ",daily_expenses)
    
    for day,expence in enumerate(expenses,start=1):
        if expence>=1000:
            print("Day", day, "expense exceeded ₹1,000:", expence)
   

    
Daily_expenses([500,800,1000,1500,2000])
    