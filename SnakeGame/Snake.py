import turtle
import time 
import random

delay = 0.1

# Score
score = 0 
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by LailaHatt1118")
wn.bgcolor("#024D60")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#2CACAD")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#D9F5F0")
food.penup()
food.goto(0, 50)

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 20, "italic"))

# Game Over display
gameOver_pen = turtle.Turtle()
gameOver_pen.speed(0)
gameOver_pen.color("red")
gameOver_pen.penup()
gameOver_pen.hideturtle()

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

def show_gameOver():
    # Affiche le message GAME OVER
    gameOver_pen.clear()
    gameOver_pen.goto(0, 50)
    gameOver_pen.color("red")
    gameOver_pen.write("GAME OVER!", align="center", font=("Impact", 50, "bold"))
    gameOver_pen.goto(0, 0)
    gameOver_pen.color("white")
    gameOver_pen.write(f"Score Final: {score}", align="center", font=("Arial", 24, "bold"))
    gameOver_pen.goto(0, -40)
    gameOver_pen.color("yellow")
    gameOver_pen.write("Appuyez sur ESPACE pour rejouer", align="center", font=("Arial", 18, "italic"))
    

def reset_game():
    """Réinitialise le jeu"""
    global score, delay
    
    # Effacer le message GAME OVER
    gameOver_pen.clear()
    
    # Réinitialiser la tête
    head.goto(0, 0)
    head.direction = "stop"
    
    # Cacher tous les segments
    for segment in segments:
        segment.goto(1000, 1000)
    
    # Vider la liste
    segments.clear()
    
    # Réinitialiser le score et le délai
    score = 0
    delay = 0.1
    
    # Mettre à jour l'affichage
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 20, "italic"))

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")    
wn.onkeypress(go_left, "Left")
wn.onkeypress(reset_game, "space")  # ESPACE pour rejouer

# Main game loop 
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        show_gameOver()  # ← AJOUTÉ
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments 
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score 
        score = 0
        
        # Reset the delay 
        delay = 0.1
        
        # Update the score display
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 20, "italic"))

    # Check for a collision with the food 
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)   
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#75E2E0")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay (but keep it above a minimum)
        if delay > 0.05:
            delay -= 0.001

        # Increase the score
        score += 10 
        if score > high_score:
            high_score = score 

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 20, "italic"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            show_gameOver()  # ← AJOUTÉ
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Hide the segments 
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

            # Reset the score 
            score = 0
            
            # Reset the delay 
            delay = 0.1
            
            # Update the score display
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 20, "italic"))

    time.sleep(delay)

wn.mainloop()
