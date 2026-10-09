'''Question 3: Shopping Cart Management 
A customer adds products to a shopping cart. Write a function that 
accepts a list of product names and performs the following 
operations: 
• Add a new product. 
• Remove a purchased or unwanted product. 
• Display the final cart. 
• Count the total number of products.'''


def shopping_cart(product):
    product.append("Headphones")
    print(product)
    product.remove("mouse")
    print("Final shopping cart",product)
    print("The total number of the product is : ",len(product))
    
shopping_cart(["laptop","mouse","webcm","phone","waterbottle"])