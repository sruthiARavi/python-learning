def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around()
    turn_left()
    
#maze challenge 
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#edge-case : 
#No hurdles on any side for single step moves i.e. stuck in a loop (keep going in a square) 
while front_is_clear():
    move()
    
turn_left()

#TODO : This still doesn't handle subseqent loops
#Only backtracking will work 

#solution 
while not at_goal(): 
    if right_is_clear(): 
        turn_right()
        move()
    elif front_is_clear():
        move()    
    else:                    
        turn_left()
