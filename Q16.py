"""Question 16: Mobile Store Inventory 
A mobile store maintains a dictionary containing mobile names 
and their available quantities. Write a function that updates stock 
after a purchase, adds a new mobile model, and displays mobiles 
that are out of stock. 
Assume a purchase must not exceed the available quantity."""


def mobile_store(mobiles,mobile_name,quantity):
    if mobile_name in mobiles:
        if quantity <= mobiles[mobile_name]:
            mobiles[mobile_name]=mobiles[mobile_name]-quantity
            print("purchase successfull")
        else:
            print("purchasing failed")
    else:
        print("there is no model in this name")
        
    new_mobile = input("Enter new mobile name : ")
    new_quantity = int(input("Enter the quantity : "))
    mobiles[new_mobile]=new_quantity
    
    print("\n Updated mobile inventery:")
    for name,Qty in mobiles.items():
        print(name,":",Qty)
        
    print("\n out of stock mobile :")
    for name,Qty in mobiles.items():    
        if Qty == 0:
            print(name)
    
    
    
mobiles={"iphone ":10,
        "samsung":20,
        "motorola":15,
        "realme":14
        }    

mobile_name = input("Enter mobile name purchased  :")
quantity = int(input("Enter the quantity : " ))    
    
mobile_store(mobiles,mobile_name,quantity)