def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around() #Or you could just do turn_left() call thrice 
    turn_left()
    

#draw a square 
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

    
