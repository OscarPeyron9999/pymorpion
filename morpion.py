#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      josselin.peyron
#
# Created:     12/01/2021
# Copyright:   (c) josselin.peyron 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

from turtle import *

import numpy as np

def draw_cell():

    setheading(0)
    for d in range (4):
        fd(100)
        lt(90)

def draw_quadrillage():

   for e in range (3):
        for f in range (3):
            draw_cell()
            fd(100)
        lt(90)
        fd(100)
        lt(90)
        fd(300)

def draw_lettres():

    up()
    fd(15)
    lt(90)
    fd(50)
    write("A")

    fd(100)
    write("B")

    fd(100)
    write("C")

def draw_nombres():

    bk(265)
    lt(90)
    fd(65)
    write("1")

    fd(100)
    write("2")

    fd(100)
    write("3")

def draw_morpion():

    speed(50)
    ht()

    up()
    bk(150)
    lt(90)
    bk(150)
    down()
    draw_quadrillage()
    draw_lettres()
    draw_nombres()

def draw_rond():

    pensize(10)
    color('red', 'red')
    begin_fill()
    up()
    setheading(0)
    fd(40)
    lt(90)
    down()
    circle(40,360,5000)
    up()
    end_fill()

def draw_croix():
    pensize(10)
    color('green', 'green')
    up()
    setheading(90)
    fd(40)
    lt(90)
    fd(40)
    setheading(315)
    down()
    fd(115)
    up()
    setheading(90)
    fd(80)
    setheading(225)
    down()
    fd(115)
    up()

def get_cell_from_input(input_value):

    x = input_value[0]

    if(x != None and x != "a" and x!="b" and x!="c"):
        return None

    y = input_value[1]

    if(y != None and y != "1" and y!="2" and y!="3"):
        return None

    if x == "a":
        x = 0
    elif x == "b":
        x = 1
    elif x == "c":
        x = 2

    y = int(y)

    y = y - 1

    return y,x

def draw_croix_ou_rond(x,y, value):

    home()

    if x == 0:
        bk(100)
    elif x == 2:
        fd(100)

    setheading(90)

    if y == 0:
        fd(100)
    elif y == 2:
        bk(100)

    if value == "o":
        draw_rond()

    elif value == "x":
        draw_croix()

def is_winner(matrice, player):
    if np.all(matrice[0, :] == [player, player, player]):
        return True
    elif np.all(matrice[1, :] == [player, player, player]):
        return True
    elif np.all(matrice[2, :] == [player, player, player]):
        return True
    if np.all(matrice[:, 0] == [player, player, player]):
        return True
    elif np.all(matrice[:, 1] == [player, player, player]):
        return True
    elif np.all(matrice[ :, 2] == [player, player, player]):
        return True
    elif matrice[0][0] == player and matrice[1][1] == player and matrice[2][2] == player:
        return True
    elif matrice[0][2] == player and matrice[1][1] == player and matrice[2][0] == player:
        return True

    return False

def not_finished(matrice):
    is_winner_o = is_winner(matrice,'o')
    is_winner_x = is_winner(matrice,'x')

    if (is_winner_o):
        print_winner('o')
        return False
    elif (is_winner_x):
        print_winner('x')
        return False
    print("Ca continue !")
    return True

def print_winner(player):
    home()
    setheading(90)
    fd(200)
    if (player == 'o'):
        color('red')
    else:
        color('green')
    style = ('Courier', 30, 'italic')
    write(player.upper() + " a gagné !", font=style, align='center')
    ht()





