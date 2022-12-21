from turtle import Turtle,Screen
import random
is_race_on = False
my_screen = Screen()
my_screen.setup(width = 500,height = 400)

colors = ["violet","indigo","blue","green","yellow","orange","red"]
y_positions = [-120,-80,-40,0,40,80,120]


turtle_choose = my_screen.textinput("There is a turtle race","Choose a colour(VIBGYOR)")

bet = int(my_screen.textinput("Win 7 times money","Make a bet!"))
all_turtles = []
for turtle_index in range(0,7):
    turtle_racer = Turtle()
    turtle_racer.shape("turtle")
    turtle_racer.penup()
    turtle_racer.color(colors[turtle_index])
    turtle_racer.goto(-230,y_positions[turtle_index])
    all_turtles.append(turtle_racer)

random.shuffle(all_turtles)
if turtle_choose and bet:
    is_race_on = True
while(is_race_on == True):
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if turtle_choose == winner:
                print(f"You are the WInner!!!! 🥳🥳, The {winner} turtle Won!!")
                print(f"You Won your bet , here is your prie money : Rs {bet*7}")
            else:
                print(f"You are the Loser😭😭 , The {winner} turtle Won!! ")
                print(f"Sorry to say but you lost your bet of Rs {bet}")
            is_race_on = False

        distance = random.randint(0,10)
        turtle.forward(distance)




































