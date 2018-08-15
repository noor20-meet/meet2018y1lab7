import turtle
turtle.goto(0,0)

up = 0
down = 1
right = 2
left = 3
direction = None

def UP():
    global direction
    direction = up
    print("you pressed the UP key")
    on_move()
    
turtle.onkey(UP, "Up") 
#turtle.listen()

def DOWN():
    global direction
    direction = down
    print("you pressed the DOWN key")
    on_move()
turtle.onkey(DOWN,"Down")
#turtle.listen()

def RIGHT():
    global direction
    direction = right
    print("you pressed the RIGHT key")
    on_move()
turtle.onkey(RIGHT, "Right")
#turtle.listen()

def LEFT():
    global direction
    direction = left
    print("you pressed the LEFT key")
    on_move()
turtle.onkey(LEFT,"Left")
turtle.listen()

def on_move():
    x,y = turtle.pos()
    if direction == up:
        turtle.goto(x,y+10)
    elif direction == down:
        turtle.goto(x,y-10)
    elif direction == right:
        turtle.goto(x+10,y)
    elif direction == left:
        turtle.goto(x-10,y)
        
