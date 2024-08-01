def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around()
    turn_left()
    
def jump():     
    #turn and move a step 
    turn_left()
    #keep going until hurdle top 
    while not right_is_clear(): 
        move()     
    #cross the hurdle
    turn_right()
    move()
    turn_right()
    #keep going until hurdle bottom 
    while not wall_in_front():
        move()
    turn_left()

#hurdle-4 challenge 
while not at_goal():    
    if wall_in_front():
        jump()
    else:
        move()
     
        

    
