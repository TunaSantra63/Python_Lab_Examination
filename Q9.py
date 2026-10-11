"""Question 9: Mobile Product Details 
An electronics store stores mobile details in a tuple containing 
brand, model, price, and storage capacity. Write a function to 
display the details and check whether the mobile price is below 
₹30,000."""


def mobile_store(mobile):
    for mobiles in mobile:
        print("Brand : ",mobiles[0]),
        print("Model: ",mobiles[1]),
        print("Price : ",mobiles[2]),
        print("Storage capacity : ",mobiles[3])
        print("compleate one details",mobiles)
        
        if mobiles[2]<30000:
            print("This mobile price is below 30000")
        else:
            print("This mobile price is not below 30000")
    
    
    
mobile=(("Samsung", "Galaxy A26 5G", 25999, "128GB"),
        ("Samsung", "Galaxy A17 5G", 24499, "128GB"),
        ("Apple", "iPhone 16", 69900, "128GB"),
        ("Samsung", "Galaxy S25", 80999, "256GB"),
        ("OnePlus", "OnePlus 13", 69999, "256GB"),
        ("Xiaomi", "Redmi Note 14", 17999, "128GB"),
        ("Realme", "Realme 14 Pro", 24999, "256GB")
        )


mobile_store(mobile)