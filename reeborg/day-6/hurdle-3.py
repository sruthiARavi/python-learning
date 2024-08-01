def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around()
    turn_left()
    
def jump():     
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#hurdle-2 challenge 
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
     
