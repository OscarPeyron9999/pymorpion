#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      josselin.peyron
#
# Created:     14/01/2021
# Copyright:   (c) josselin.peyron 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from morpion import *
import morpion_ia as ia
import numpy as np
import turtle as t
import time

matrice = np.array([[ None, None, None],
           [ None, None, None],
           [ None, None, None]])

def on_click(x, y):
    print(x, y)
    play(get_cell_from_mouse_position(x, y))

def get_cell_from_mouse_position(mouse_x, mouse_y):
    x = 0
    y = 0
    if (mouse_x < 50) and (mouse_x > -50):
        x = 1
    elif (mouse_x > 50):
        x = 2
    elif (mouse_x < -50):
        x = 0
    if (mouse_y < 50) and (mouse_y > -50):
        y = 1
    elif (mouse_y > 50):
        y = 0
    elif (mouse_y < -50):
        y = 2

    print (x, y)
    return x, y

def draw_coup(cell, player):
    x = cell[0]
    y = cell[1]
    if matrice[x][y] != None :
        print("Erreur! Coup interdit!")
    else :
        matrice[x][y] = player
        draw_croix_ou_rond(x,y, player)


def play(cell):
    global matrice
    if (cell != None):
        if(not_finished(matrice)):
            draw_coup(cell,  'o')
        if(not_finished(matrice)):
            draw_coup(ia.get_coup(matrice),  'x')

def main():
    draw_morpion()
    t.onscreenclick(on_click)
    t.mainloop()


if __name__ == '__main__':
    main()


def get_mouse_click_coor(x, y):
    print(x, y)


