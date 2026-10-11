"""Question 12: Cricket Match Statistics 
A cricket application stores a player's name, runs scored, balls 
faced, and number of boundaries in a tuple. Write a function to 
calculate the strike rate and display whether the player scored a 
half-century. 
Strike rate = (runs scored / balls faced) × 100."""

def cricket_application(player):
    for players in player:
        player_name=players[0]
        runs_scored=players[1]
        balls_faced=players[2]
        player_boundaries=players[3]
        
        Strike_rate = (runs_scored / balls_faced) * 100.
    
    
    
        print("players_name  :",player_name)
        print("players run :",runs_scored)
        print("players faced the ball  :",balls_faced)
        print("players boundaries :",player_boundaries)
        print("The strike rate  :",Strike_rate)
    
        if runs_scored >=50:
            print("The player scored is half century")
        else:
            print("The player scored not a half century")
    
player =(("virat kohli",75, 50,8),
        ("Rohit Sharma", 45, 30, 6),
        ("Shubman Gill", 32, 25, 3)
          
)

cricket_application(player)    
        
    

    