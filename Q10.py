"""Question 10: GPS Location Tracking 
A delivery application stores the latitude and longitude of a 
delivery location in a tuple. Write a function to display the 
coordinates and determine whether they represent a location in 
the approximate bounding box of Kolkata: latitude 22.4–22.8 and 
longitude 88.2–88"""


def delivery_location(location):
    latitude=location[0]
    longitude=location[1]
    
    if 22.4<= latitude <= 22.8 and 88.2 <= longitude <= 88.5 :
        
        print("This location is in approximate bounding box of kolkata")
    else:
        print("This location is outside of kolkata")
    
    
    
    
location=(22.5726,88.3639)
    
delivery_location(location)