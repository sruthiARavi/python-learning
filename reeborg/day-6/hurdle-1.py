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
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
'''
for step in range(6): #to do 6 jumps, so 0-6, not including 6
    jump()
'''

#Using while loop 
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1

    
