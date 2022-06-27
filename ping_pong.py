# immport turtle module for screen
import turtle
import time

wind = turtle.Screen() # make sxreen
wind.title("Ping Pong")  #name of wind
wind.bgcolor("blue")  # background color
wind.setup(width=600,height=600)     #area
wind.tracer(0)    # stop windo to ake updata it self
# paddle 1
paddle1=turtle.Turtle()  # intialize turtle object(shape)
paddle1.speed(0)  #fast speed for paddle
paddle1.shape("square")
paddle1.shapesize(stretch_wid=4,stretch_len=1) 
paddle1.color("black")
paddle1.penup()  # for delete eow after moving
paddle1.goto(-240,0)   # X ,  Y
# paddle 2
paddle2=turtle.Turtle()
paddle2.speed(0)  #fast speed for paddle
paddle2.shape("square")
paddle2.shapesize(stretch_wid=4,stretch_len=1) 
paddle2.color("white")
paddle2.penup()  # for delete eow after moving
paddle2.goto(240,0)   # X ,  Y
paddle2.dy=0.1

# ball 
ball=turtle.Turtle()
ball.speed(0)  #fast speed for paddle
ball.shape("circle") 
ball.color("yellow")
ball.penup()  # for delete eow after moving
ball.goto(0,0)   # X ,  Y

ball.dx = 0.1
ball.dy = 0.1

#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,255)
score.write("Player 1 : 0 , Player 2 : 0 ",align="center" , font=("courier",12,"normal"))


# function up paddle 1
def paddle1_up():
    y1=paddle1.ycor()   # assing cor of paddle1 to y1
    y1+=20              # move y1 to up 
    paddle1.sety(y1)    # new value after moveing assing to paddle1
    if paddle1.ycor() > 235:
        paddle1.sety(235)
        
def paddle1_down():
    y1=paddle1.ycor()   # assing cor of paddle1 to y1
    y1-=20              # move y1 to up 
    paddle1.sety(y1)    # new value after moveing assing to paddle1    
    if paddle1.ycor() < -235:
        paddle1.sety(-235)

   #   2
def paddle2_up():
    y1=paddle2.ycor()   
    y1+=20               
    paddle2.sety(y1)    
    if paddle2.ycor() > 235:
        paddle2.sety(235)    
def paddle2_down():
    y1=paddle2.ycor()  
    y1-=20               
    paddle2.sety(y1)        
    if paddle2.ycor() < -235:
        paddle2.sety(-235)




# keyboard pressing
wind.listen()       # tell secreen to get value
wind.onkeypress(paddle1_up,"w")  # when press on w call function paddle1_up
wind.onkeypress(paddle1_down,"s")
wind.onkeypress(paddle2_up,"Up")  # when press on w call function paddle1_up
wind.onkeypress(paddle2_down,"Down")

#----------------------------------------

#game loop to make the game running
while True:
    wind,turtle.update() #stop screen updateing
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    paddle2.sety(paddle2.ycor())
    paddle2.goto(240,ball.ycor())   
      
   # border check up and down
    if ball.ycor() > 265:
        ball.sety(265)
        ball.dy*=-1
    if ball.ycor() < -265:
        ball.sety(-265)
        ball.dy*=-1

    # border check right and left
    if ball.xcor() > 265:
        ball.goto(0,0)
        ball.dx*=-1
        score1 +=1
        score.clear()
        score.write(f"Player 1 : {score1} , Player 2 : {score2} ",align="center" , font=("courier",12,"normal"))
    if score1==4:
        score.clear()
        score.write("Player one is win",align="center" , font=("courier",12,"normal"))
        time.sleep(3)
        break
         
    if score2==4:
        score.clear()
        score.write("Player tow is win",align="center" , font=("courier",12,"normal"))
        time.sleep(3)
        break
    if ball.xcor() < -265:
        ball.goto(0,0)
        ball.dx*=-1
        score2 +=1
        score.clear()        
        score.write(f"Player 1 : {score1} , Player 2 : {score2} ",align="center" , font=("courier",12,"normal"))

    # test paddles and pall
    if (ball.xcor() < -230 and ball.xcor() >- 240) and (ball.ycor() < paddle1.ycor()+50 and ball.ycor() > paddle1.ycor()-50 ):
        ball.setx(-230)
        ball.dx *= -1

    if (ball.xcor() > 230 and ball.xcor() < 240) and (ball.ycor() < paddle2.ycor()+50 and ball.ycor() > paddle2.ycor()-50 ):
        ball.setx(230)
        ball.dx *= -1
