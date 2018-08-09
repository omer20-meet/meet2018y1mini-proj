# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import time
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
                             #size.

'''border = turtle.clone()
border.hideturtle()
border.goto(300,300)
border.pendown()
border.goto(600,300)
border.goto(600,-300)
border.goto(-300,-300)
border.goto(-300,300)
'''
bg_choose = input("choose one of the colors from this list:'white', 'yellow', 'blue', 'pink', 'red': ")
turtle.bgcolor(bg_choose)
border = turtle.clone()
border.hideturtle()

border.penup()
border.pensize(5)
border.goto(-300,300)
border.pendown()
border.goto(300,300)
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 2

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
turtle.register_shape("cat.gif") #Add cat picture
turtle.register_shape("rainbow.gif")
snake.shape("rainbow.gif")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)




for item  in range(START_LENGTH) :
    x_pos = snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos = snake.pos()[1]
    
    
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos += SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos, y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    snake_st = snake.stamp()
    stamp_list.append(snake_st)




    
        
        
    
    

###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 150 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN = 1 
LEFT = 2
RIGHT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300


def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")


def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to down
    print("You pressed the down key!")


def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to left
    print("You pressed the left key!")


def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to right
    print("You pressed the right key!")


turtle.onkeypress(up, UP_ARROW) # Create listener for up key

turtle.onkeypress(down, DOWN_ARROW) # Create listener for up key

turtle.onkeypress(left, LEFT_ARROW) # Create listener for up key

turtle.onkeypress(right, RIGHT_ARROW) # Create listener for up key

turtle.listen()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/4/SQUARE_SIZE)+1
    max_x=int(SIZE_X/4/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/4/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/4/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    food.hideturtle()
    food.goto(food_x,food_y)
    food_pos2 = food.pos()
    food_pos.append(food_pos2)
    food_st2 = food.stamp()
    food_stamps.append(food_st2)

    
    

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
        
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

    elif direction==UP:

        snake.goto(x_pos , y_pos + SQUARE_SIZE)
        print("You moved up!")

    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        turtle.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        quit()
        
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        turtle.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        turtle.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        quit()
        
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        turtle.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        quit()

    if snake.pos() in pos_list:
        turtle.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
        time.sleep(1)
        quit()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    snake.shape("square")
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 

    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")

    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    #for i in range(len(pos_list)-1):
     #   snake.shape("rainbow.gif")
      #  old_stamp = stamp_list.pop(i)
       # snake.clearstamp(old_stamp)
        #snake.goto(pos_list[i]) #hopefully make the snake's head niancat
        #newstamp = snake.stamp()
        #stamp_list.insert(i, newstamp)
        #snake.shape("cat.gif") 
        


    if len(food_stamps) <= 0 :
    	make_food()

    

        
    
    #HINT: This if statement may be useful for Part 84
    #piece of the tail
    turtle.ontimer(move_snake,TIME_STEP)






turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_st = food.stamp()
    food_stamps.append(food_st)
    food.hideturtle()
    
    

    
move_snake()





