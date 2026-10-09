'''Question 2: Online Mobile Store 
An online store maintains a list of mobile prices. Write a function 
to display all mobiles costing more than ₹20,000, calculate the 
total inventory value, and find the most expensive mobile price.'''

def mobile_price(price):
    expensive_mobile =max(price)
    total_price = sum(price)
    
    for _ in price:
        if(_>20000):
            print("Mobile costing more than rs 20000",_)
            
     
    print("Total inventory value is : " , total_price)   
    print("The most expensive mobile price is : " , expensive_mobile)   
mobile_price([20000,30000,40000,50000,60000,150000,70000])
