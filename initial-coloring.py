# import package
import turtle
  
MULTIPLIER = 30

# screen object
wn = turtle.Screen()
  
# method to perform action
def draw_line_to(x, y):
  turtle.goto(x, y)
  turtle.write(str(x)+","+str(y))

def fill_square(x,y):
    ''' if you click inside a square in the checkboard, it will fill it '''
    if 0 < x and x < 8*MULTIPLIER and 0 < y and y < 8*MULTIPLIER:
        xFloor = x // MULTIPLIER * MULTIPLIER
        yFloor = y // MULTIPLIER * MULTIPLIER
        
        turtle.hideturtle()

        turtle.penup()

        turtle.goto(xFloor, yFloor)
        turtle.setheading(90)
        turtle.pendown()

        turtle.pen(pencolor="green", pensize=1)

        turtle.begin_fill() 

        for i in range(4):
            turtle.forward(MULTIPLIER)
            turtle.right(90)
            turtle.fillcolor("pink")
          
        turtle.end_fill()

  
# onclick action 
wn.onclick(fill_square)


def draw_board():
    ''' draws an 8 x 8 chessboard '''
    boardDrawer = turtle.Turtle()
    boardDrawer.color((0.6, 0.6, 0.6)) # grey
    boardDrawer.penup()
    boardDrawer.goto(0,0)
    # draw vertical
    for i in range(0, 8+1):
        boardDrawer.pendown()
        boardDrawer.goto(i*MULTIPLIER, 8*MULTIPLIER)
        boardDrawer.penup()
        boardDrawer.goto((i+1)*MULTIPLIER, 0)

    boardDrawer.goto(0,0)
    # draw horizontal
    for j in range(0, 8+1):
        boardDrawer.pendown()
        boardDrawer.goto(8*MULTIPLIER, j*MULTIPLIER)
        boardDrawer.penup()
        boardDrawer.goto(0, (j+1)*MULTIPLIER)

   
    
draw_board()

wn.mainloop()
        
