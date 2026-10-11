"""Question 17: Online Shopping Bill 
An online shopping cart stores product names and prices in a 
dictionary. Write a function to calculate the subtotal, apply a 10% 
discount when the subtotal is at least ₹5,000, and display the final 
bill."""

def shopping_store(product):
    for customer,products in product.items():
        subtotal=sum(products.values())
        print("customer",customer)
        print("subtotal",subtotal)
        
        
        if subtotal>=5000:
            discount=subtotal*10 /100
            final_amount = subtotal-discount
            
            print("Discount is :",discount)
            print("The final price is : ",final_amount)
        else:
            print("Discount : 0")
            print("The final price is : ",subtotal)
        
     
product={
    "customer 1":{
        "laptop":50000,
        "phone":30000,
        "makeup product":5000,
        "books":1000}, 
    "customer 2":{
        "webcam":5000,
        "calculator":100
        },
    "customer":{
        "books":500,
        "makeup":1000
                    
    }
        
 }
    
shopping_store(product)