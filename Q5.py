'''Question 5: Social Media Likes 
A social media platform stores the number of likes received by five 
posts in a list. Write a function to find the post with the highest 
likes, calculate total likes, and display posts that received at least 
100 likes.'''




def social_media(likes):
    highest_likes = max(likes)
    total_likes = sum(likes)

    print("Highest likes:", highest_likes)
    print("Total likes:", total_likes)

    
    posts = [like for like in likes if like >= 100]
    print("Posts with at least 100 likes:", posts)


        
social_media([10,30,50,100,150,150,200,1000,1500])