'''Question 11: Product Order Details 
An e-commerce website stores an order as a tuple containing 
order ID, product name, quantity, and unit price. Write a function 
to calculate the total order value and display the order details. '''



def e_commerce(product):
    
    total_order = 0
    for products in product:
        product_id = products[0]
        product_name = products[1]
        product_quantity=products[2]
        product_price=products[3]
        
        order_price = product_quantity * product_price
        total_order = total_order + order_price
        
        
        print("Product_id : ",product_id)
        print("Product_name : ",product_name)
        print("Product_quantity : ",product_quantity)
        print("product_price : ",product_price)
        print("Unit Price: ₹", product_price)
        print("Total Order Value: ₹", order_price)
    print("Total Order Value of All Products: ₹", total_order)
    
    
    
product=((101,'laptop',1,50000),
        (102,'webcam',2,1500),
        (103,'shirt',2,500),
        (104,'chocolate',2,200)
        )

e_commerce(product)
    