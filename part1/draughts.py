# -*- coding: utf8 -*-
#
# INFO-F106 - Projet d'année - Partie 1
#
# GÉRARD Pierre  000379259


from draughtsFunctions import *
from config import *


def main():
    """Fonction principal qui permet de lancer un jeu de dame avec des règles
    légérement modifiées"""
    board = initBoard(DIMENSION)
    print("Jeu de dame \n")
    print("Pricipe : Pour déplacer un pion, veuillez introduire ses " +
          "coordonnées et le sens de déplacement souhaité (r pour droite" +
          "et l pour gauche) entre virgules. \nPar exemple i,5,r \n")
    if board:
        player = WHITE_PLAYER  # Le joueur blanc à le trait
        printBoard(board, player)
        while checkEndOfGame(board, player) is False:
            if player == 1:
                print("C'est au tour du joueur avec les pions blancs")
            else:
                print("C'est au tour du joueur avec les pions noirs")
            coordinates = input("Entrer le deplacement souhaité : ")
            # On considère l'utilisateur comme étant "intelligent" et qu'il
            # rentre des coordonnées sous le format correct :
            j, i, direction = coordinates.split(",")
            i = int(i) - 1
            j = ord(j) - ord("a")
            direction = direction.upper()
            clearance = checkMove(board, i, j, direction, player)
            if clearance:
                movePiece(board, i, j, direction)
                player = -player
                printBoard(board, player)
            else:
                print(clearance)
    else:
        print("Erreur de configuration: Il est impossible de jouer avec une" +
              "dimension de plateau aussi petite")


if __name__ == '__main__':
    main()
