import numpy as np
import random


def get_coup_gagnant_lignes(matrice, player):

    if np.all(matrice[0][:] == [player, player, None]):
        return 0,2
    elif np.all(matrice[0,:] == [None, player, player]):
        return 0,0
    elif np.all(matrice[0,:] == [player, None, player]):
        return 0,1
    elif np.all(matrice[1,:] == [player, player, None]):
        return 1,2
    elif np.all(matrice[1,:] == [None, player, player]):
        return 1,0
    elif np.all(matrice[1,:] == [player, None, player]):
        return 1,1
    elif np.all(matrice[2,:] == [player, player, None]):
        return 2,2
    elif np.all(matrice[2,:] == [None, player, player]):
        return 2,0
    elif np.all(matrice[2,:] == [player, None, player]):
        return 2,1
    return None

def get_coup_gagnant_colonnes(matrice, player):

    if np.all(matrice[:,0] == [ player, player, None]):
        return 2,0
    elif np.all(matrice[:,0] == [ None, player, player]):
        return 0,0
    elif np.all(matrice[:,0] == [ player, None, player]):
        return 1,0
    elif np.all(matrice[:,1] == [ player, player, None]):
        return 2,1
    elif np.all(matrice[:,1] == [ None, player, player]):
        return 0,1
    elif np.all(matrice[:,1] == [ player, None, player]):
        return 1,1
    elif np.all(matrice[:,2] == [ player, player, None]):
        return 2,2
    elif np.all(matrice[:,2] == [ None, player, player]):
        return 0,2
    elif np.all(matrice[:,2] == [ player, None, player]):
        return 1,2
    return None

def get_coup_gagnant_diagonales(matrice, player):

    if matrice[0][0] == player and matrice[1][1] == player and matrice[2][2] == None:
        return 2,2
    elif matrice[0][0] == player and matrice[1][1] == None and matrice[2][2] == player:
        return 1,1
    elif matrice[0][0] == None and matrice[1][1] == player and matrice[2][2] == player:
        return 0,0
    elif matrice[0][2] == player and matrice[1][1] == player and matrice[2][0] == None:
        return 2,0
    elif matrice[0][2] == player and matrice[1][1] == None and matrice[2][0] == player:
        return 1,1
    elif matrice[0][2] == None and matrice[1][1] == player and matrice[2][0] == player:
        return 0,2
    return None

def coup_gagnant(matrice, player):

    result = get_coup_gagnant_lignes(matrice, player)
    if result != None:
        return result

    result = get_coup_gagnant_colonnes(matrice, player)
    if result != None:
        return result

    result = get_coup_gagnant_diagonales(matrice, player)

    if result != None:
        return result

    return None

def coin(matrice):

    coins_dispo = []

    if matrice[0][0] == None:
        coins_dispo.append((0,0))

    if matrice[0][2] == None:
        coins_dispo.append((0,2))

    if matrice[2][0] == None:
        coins_dispo.append((2,0))

    if matrice[2][2] == None:
        coins_dispo.append((2,2))

    return random.choice(coins_dispo)

def centre(matrice):
    if matrice[1][1] == None:
        return (1,1)

def get_coup(matrice):

    result = coup_gagnant(matrice, "x")
    if result != None:
        return result

    result = coup_gagnant(matrice, "o")
    if result != None:
        return result

    result = centre(matrice)
    if result != None:
        return result

    result = coin(matrice)
    if result != None:
        return result

    assert result != None, "Aucun coup trouvé"