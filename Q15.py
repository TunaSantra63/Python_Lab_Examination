"""15: Social Media Profile Analysis 
A social media application stores usernames and follower counts 
in a dictionary. Write a function to display all profiles, identify the 
user with the highest followers, and list users with more than 
1,000 followers. 
the class average, and identifies students who scored at least 75 
marks."""



def social_media(creater):
    for username ,followers in creater.items():
        print("prifile name : ",username)
        print("followers: ", followers)
        
        highest_followers=max(creater,key = creater.get)
        
    for username,followers in creater.items():
        if followers>=1000:
            print("those creater have followers more than 1000 :",username,":",followers)
    
    print("The creater who has highest follower : ",username,highest_followers) 
    
    
creater={"aman mallik": 100000,
        "life_hacks":10000,
        "Arun dhavan":300000,
        "riya kumari":500,
        "Tuna santra":400}
    
social_media(creater)