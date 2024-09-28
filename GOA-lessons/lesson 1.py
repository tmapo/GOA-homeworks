from turtle import *

#we want a decent home, lets paint it!

#lets get some red brick walls
width(7)
begin_fill()
color("firebrick")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of the square 

#now we need a door
forward(120)
begin_fill()
color("saddlebrown")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()
#the door is finished, it needs a doorknob

#let's get a nice roof
penup()
goto(250, 200)
pendown()
color("maroon")
begin_fill()
forward(300)
right(135)
forward(215)
right(90)
forward(215)
right(135)
end_fill()
#we wont get wet now!

#lets get a doorknob for the door to function properly
penup()
goto(170, 80)
pendown()
begin_fill()
color("yellow")
forward(5)
left(90)
forward(5)
left(90)
forward(5)
left(90)
forward(5)
end_fill()
#you can open the door now! achievemnt huh?

#whats better than natural light in your house? we need some windows!
penup()
goto(30, 60)
pendown()
begin_fill()
color("lightblue")
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
#windowframe part

color("saddlebrown")
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
backward(30)
right(90)
forward(60)
backward(30)
right(90)
forward(30)
backward(60)
#windows are done!
#nice house,the job is done

exitonclick()