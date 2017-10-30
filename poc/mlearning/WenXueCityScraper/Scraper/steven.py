# import random
import time

# import  turtle
# fred = turtle.Pen()
# fred.speed(10)
# def triangle(size):
#     for i in range(3):
#         fred.forward(size)
#         fred.left(120)
# fred.forward(-400)
#
#
# fred.right(90)
# fred.forward(200)
# fred.left(90)
# for i in range(100):
#     triangle(1*i*i)

#  colorlist = ["olive drab","cadet blue","maroon"]
#  fred.speed(0)
#  square(100)
#  fred.forward(200)
# # square(150)
# for i in range(100):
#     x = random.randrange(-200, 200)
#    / y = random.randrange(-200, 200)
#     fred.up()
#     fred.goto(x,y)
#     col = random.choice(colorlist)
#     fred.color(col)
#     size = random.randrange(10,200)
#     fred.down()
#     square(size)

#



# turtle.getscreen()._root.mainloop()














# name = input("what is your name? ")
# print("Hello,", name)
#
# ninjas = int(input("How many ninjas are attacking ?"))
#

# /if ninjas > 50:
#     print("That's too  many!")
#


import random


# secret =random.randrange(1,101)
#
#
# guess = 0
# tries = 0
# while guess != secret:
#     guess = int(input("Make a guess: "))
#     tries = tries + 1
#     if guess > secret:
#         print ("Too High!")
#     elif guess < secret:
#         print ("Too Low!")
#     else:
#         print ("You got it!")

# print("Number of Tries:", tries)
# wins = 0
#
# moves = ['r','p','s']
#
# player_wins = ['pr','sp','rs']
# while True:
#     player_move = input("Your move:")
#     if player_move == 'q':
#         break
#     computer_move = random.choice(moves)
#
#     print("You:",player_move)
#     print("Me:",computer_move)
#     if player_move == computer_move:
#         print("Tie")
#     elif player_move + computer_move in player_wins:
#         print("You win!")
#         wins = wins + 1
#     else:
#         print("You lose, sucka!")
#       print number of wins
# alpha = "abcdefghijklmnopqrstuvwxyz"
#
# def encrypt(cleartext):
#     cyphertext = ""
#     for char in cleartext:
#         if char in alpha:
#             newpos = (alpha.find(char) + 13) % 26
#             cyphertext += alpha[newpos]
#         else:
#             cyphertext += char
#     return cyphertext
#
#
# cleartext = input("Cleartext:")
# cleartext = cleartext.lower()
# print (encrypt(cleartext))
from tkinter import *
import random






WIDTH = 900
HEIGHT = 600



tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Bouncy Ball Simulation 2017")
canvas.pack()


class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill = color)
        self.xspeed = random.randrange(1, 5)
        self.yspeed = random.randrange(9, 30)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed
colors = ['dodgerblue','olive drab', 'cadet blue']

balls = []
for i in range(100):
    balls.append(Ball(random.choice(colors), random.randrange(50, 100)))

# newball = Ball("red", 50)
# newball2 = Ball("orange", 25)
# newball2.yspeed = 0
# newball3 = Ball("yellow", 75)
# newball4 = Ball("green", 100)
# newball5 = Ball("blue", 125)
# newball6 = Ball("purple", 150)
# newball6.xspeed = 0
# newball7 = Ball("olive drab", 175)
# newball8 = Ball("cadet blue",100)
#
# xspeed = 20
# yspeed = 0
while True:
    for ball in balls:
        ball.move()
    # newball.move()
    # newball2.move()
    # newball3.move()
    # newball4.move()
    # newball5.move()
    # newball6.move()
    # newball7.move()
    # newball8.move()

# canvas.move(ball, xspeed, yspeed)
# pos = canvas.coords(ball)
# if pos[3] >= HEIGHT or pos[1] <=0:
#         yspeed = -yspeed
#      if pos[2] >= WIDTH or pos[0] <= 0:
#          xspeed = -xspeed
    tk.update()
    time.sleep(0.01)
#     xspeed += 0
#     yspeed += 2
#     canvas.move(ball2, xspeed2, yspeed2)
#     pos = canvas.coords(ball)
#     if pos[3] >= HEIGHT or pos[1] <=0:
#         yspeed2 = -yspeed2
#     if pos[2] >= WIDTH or pos[0] <= 0:
#         xspeed2 = -xspeed2
#     tk.update()
#     time.sleep(0.01)
#     xspeed += 0
#     yspeed += 2
#     xspeed2 += 0
#     yspeed2 += 2













































































































































































# canvas.create_line(0, 0, 500, 400)
# canvas.create_rectangle(100, 100, 250, 250, fill="blue")
# canvas.create_oval(10, 10, 50, 50, fill="green")
# canvas.create_polygon(400, 10, 300, 300, 500, 300, fill="purple")
# for i in range(100):
#     x1 = random.randrange(500)
#     y1 = random.randrange(400)
#     x2 = random.randrange(500)
#     y2 = random.randrange(400)
#     canvas.create_rectangle(x1,y1,x2,y2)













canvas.mainloop()
