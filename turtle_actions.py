import turtle



def first_life():
    turtle.Screen().cv._rootwindow.attributes("-topmost", True)
    turtle.TurtleScreen._RUNNING=True
    turtle.penup()
    turtle.goto(0,220)
    turtle.pendown()
    turtle.goto(200,220)
    turtle.goto(200,-220)

def second_life():
    first_life()
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.circle(40)
    

def third_life():
    second_life()
    turtle.goto(0,-100)
    turtle.penup()    
    

def fourth_life():
    third_life()
    turtle.goto(0,50)
    turtle.pendown()
    turtle.goto(50,50)
    

def fifth_life():
    fourth_life()
    turtle.penup()
    turtle.goto(0,50)
    turtle.pendown()
    turtle.goto(-50,50)
    

def sixth_life():
    fifth_life()
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.goto(50,-150)
    

def seventh_life():
    sixth_life()
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.goto(-50,-150)
    

def eighth_life():    
    seventh_life()
    turtle.penup()
    turtle.goto(0,220)
    turtle.pendown()
    turtle.goto(0,180)
    


