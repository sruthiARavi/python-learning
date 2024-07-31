def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around()
    turn_left()
    
def jump():
    #first and last line of the function 
    #only for the purposes of this specific 
    #requirement 
    move()  
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#hurdle-1 challenge 
for step in range(6): #to do 6 jumps, so 0-6, not including 6
    jump()
