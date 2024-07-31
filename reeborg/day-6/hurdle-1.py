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

#hurdle-1 challenge 
for number in range(1, 7): #to do 6 jumps
    move()
    jump()
    turn_left()



    
