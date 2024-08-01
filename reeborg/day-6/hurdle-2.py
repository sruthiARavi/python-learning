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

#hurdle-2 challenge 
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
#while at_goal() is not True:
while not at_goal():
    jump()

    
