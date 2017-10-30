# import random
# import turtle
import time
# fred = turtle.Pen()
# fred.shape("turtle")
# colorlist = ["red", "green", "blue","orange", "yellow"]
# fred.width(3)
# def square(size):
#     for i in range(4):
#         fred.forward(size)
#         fred.left(90)
#  fred.speed(0)

# square(100)
# fred.forward(200)
# square(150)
#
# for i in range(100):
#     x = random.randrange(-200, 200)
#     y = random.randrange(-200, 200)
#     fred.up()
#     fred.goto(x , y)
#     fred.down()
#     col = random.choice(colorlist)
#     fred.color(col)
#     size = random.randrange(10, 200)
#     square(size)
#
# def triangle (size):
#     for i in range(3):
#         fred.forward(size)
#         fred.left(120)
#
# triangle(100)


# turtle.getscreen()._root.mainloop()
#
# turtle.getscreen()._root.mainlo
#
# x = 23
# print x
# print x + 8 * 4
#
# # food = ("steven", "hat", "lunch", "beef")
# # print food
# #
# # ninjas = int(input("How many ninjas are attacking?"))
# #
# #
# # if ninjas > 50:
#     # print ("thats too many!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#
#
# import random

# secret = random.randrange(1, 101)



# guess = 0
# tries = 0
#
# while guess != secret:
#     tries = tries + 1
#     guess = int(input("Make a guess:"))
#
#     if guess > secret:
#         print("Too High sucka!")
#     elif guess < secret:
#         print("Too Low dumb head! ")
#     else:
#         print("You got it !")
# #
import random
# moves =['r', 'p', 's']
# player_win = ['pr','sp','rs']
# while True:
#     player_move = input("your move: ")
#     if player_move == 'q':
#         print("you are a quitter")
#         break
#     if player_move =='r':
#         computer_move = 'p'
#     if player_move == 'p':
#         computer_move = 's'
#     if player_move == 's':
#         computer_move = 'r'
#
#
#
#     print("you", player_move)
#     print ("me ", computer_move)
#     if player_move == computer_move:
#         print("Tie yoy dangit")
#     elif player_move + computer_move in player_win:
#         print("you win, oh no dumby!!!!!!")
#     else:
#         print ("you lose sucker egg head !")


# def triangle (size):
#     for i in range(3):
#         fred.forward(size)
#         fred.left(60)
# triangle(30)








# alpha = "abcdefghijklmnopqrstuvwxyz"
#
# def encrypt(cleartext):
#     cyphertext = ""
#     for char in cleartext:
#         #print 'check all the chars: ', char
#         if char in alpha:
#             # print alpha.find(char)
#             newpos = (alpha.find(char) + 13) % 26
#             cyphertext += alpha[newpos]
#         else:
#             cyphertext += char
#     return cyphertext
#
#
# cleartext = input("Cleartext:")
# cleartext = cleartext.lower()
# print(encrypt(cleartext))

from tkinter import *



WIDTH = 1300
HEIGHT = 800
tk = Tk()
canvas = Canvas(tk,width= WIDTH, height=HEIGHT)


tk.title("Drawing noah  ")
canvas.pack()
class Ball:
    def __init__(self, color, size) :
        self.shape = canvas.create_rectangle(10,10,size,size, fill=color)
        self.xspeed = random.randrange(1,10)
        self.yspeed = random.randrange(1,20)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        canvas.coords()
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed


class Train:
    def __init__(self, x1 ,y1, x2, y2,x3,y3,x4,y4,x5,y5,x6,y6,color):
        self.shape = canvas.create_polygon(x1 ,y1, x2, y2,x3,y3,x4,y4,x5,y5,x6,y6, fill=color)
    # def __init__(self, x1, y1, x2, y2, x3, y3):
    # def __init__(self, color, sizex, sizey):
        # self.shape = canvas.create_rectangle(10, 10, sizex, sizey, fill=color)
        # self.shape = canvas.create_polygon(x1, y1, x2, y2, x3, y3)
        self.xspeed =2 #random.randrange(-2,2)
        self.yspeed =1 #random.randrange(-2,2)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

    def turn(self):

        canvas.move(self.shape, self.yspeed, -self.xspeed)



colors = ['red', 'green', 'blue', 'orange' , 'yellow', 'cyan', 'magenta', 'purple', 'turquoise','gold','brown']


# balls = []
# for i in range(100):
#     balls.append(Ball(random.choice(colors),random.randrange(50, 200)))
# thomas = Train('sky blue', 50, 20)

thomasp = Train(523, 84, 5, 1, 44, 134, 42, 34, 63, 34,1,23, 'green')

# newball = Ball("red", 50)
# newball2 = Ball("green", 10)
# newball3 = Ball("black", 30)
# newball4 = Ball("brown", 15)
# newball5 = Ball("blue", 20)
# newball6 = Ball("yellow", 40)


while True:
    for i in range(100000000000000000):
        thomasp.move()
    thomasp.turn()
    # for ball in balls:
    #     ball.move()
#     newball.move()
#     newball2.move()
#     newball3.move()
#     newball4.move()
#     newball5.move()
#     newball6.move()

    tk.update()
    time.sleep(0.000000000000000000001)













































# canvas.create_line(0,0,500,400)
# canvas.create_rectangle(100,100,250,250, fill="blue")
# canvas.create_oval(10,10,50,50,fill="green")
# canvas.create_polygon(400,10,300,300,500,300, fill="purple")

# for i in range(100):
#     x1 = random.randrange(500)
#     y1 = random.randrange(400)
#     x2 = random.randrange(500)
#     y2 = random.randrange(400)
#     canvas.create_rectangle(x1,y1,x2,y2)












canvas.mainloop()





































































































































#steven is going down





















# name = input("what is your name? ")
# print("hello", name)



















































































