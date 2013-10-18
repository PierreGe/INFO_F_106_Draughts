# -*- coding: utf8 -*-
#
# INFO-F106 - Projet d'année - Partie 1
#
# GÉRARD Pierre  000379259


from config import *


def initBoard(dimension):
    """Crée et retourne un damier dont la taille sera passé en paramètre qui
    est représenté par une matrice """
    if dimension > 4:
        board = []
        for idxRow in range(dimension):
            ligne = []
            for idxColumn in range(dimension):
                if (idxRow + idxColumn) % 2 == 0:
                    ligne.append(FREE_SPACE)
                elif idxRow < (dimension // 2) - 1:
                    ligne.append(BLACK_PLAYER)
                elif (dimension % 2) == 0 and idxRow > (dimension // 2):
                    ligne.append(WHITE_PLAYER)
                elif (dimension % 2) == 1 and idxRow > (dimension // 2) + 1:
                    ligne.append(WHITE_PLAYER)
                else:
                    ligne.append(FREE_SPACE)
            board.append(ligne)
    else:
        board = False
    return board


def printBoard(board, player):
    """Imprime le damier avec les pions de l'utilisateurs situés en dessous
    pour faciliter la lecture de ce dernier """
    if player == -1:
        for idxRow, row in enumerate(reversed(list(board))):
            for idxColumn, column in enumerate(reversed(list(row))):
                if column == 1:
                    print(WHITE_PAWN, " ", end="")
                elif column == -1:
                    print(BLACK_PAWN, " ", end="")
                elif (idxRow + idxColumn) % 2 == 0:
                    print(WHITE_SQUARE, " ", end="")
                else:
                    print("   ", end="")
            print(" |", DIMENSION - idxRow)  # Indication de la ligne
        print("_  " * len(board))
        for i in range(len(board)):  # Indication de la colonne en lettre
            print(chr(ord("a") + len(board) - 1 - i) + "  ", end="")
        print("")

    else:
        for idxRow, row in enumerate(board):
            for idxColumn, column in enumerate(row):
                if column == 1:
                    print(WHITE_PAWN, " ", end="")
                elif column == -1:
                    print(BLACK_PAWN, " ", end="")
                elif (idxRow + idxColumn) % 2 == 0:
                    print(WHITE_SQUARE, " ", end="")
                else:
                    print("   ", end="")
            print(" |", idxRow + 1)
        print("_  " * len(board))
        for i in range(len(board)):
            print(chr(ord("a") + i) + "  ", end="")
        print("")


def movePiece(board, i, j, direction):
    """Deplace un pion d'une position sur une autre"""
    player = board[i][j]
    if direction == "L":
        direction = -1
    elif direction == "R":
        direction = 1
    board[i - player][j + direction * player] = player
    board[i][j] = 0


def checkMove(board, i, j, direction, player):
    """Verifie si le coup joué par le joueur est valide Elle retournera True
    si le coup est valide sinon l'erreur commise par le joueur"""
    if direction == "L":
        direction = -1
    else:
        direction = 1
    if not (0 <= i < DIMENSION and 0 <= j < DIMENSION):
        clearance = "Vous avez entré des coordonnées hors damier"
    elif board[i][j] == 0:
        clearance = "Il n'y a pas de pion sur cette case."
    elif board[i][j] != player:
        clearance = "Vous ne pouvez bouger que vos pions."
    elif (0 <= i - player < DIMENSION and 
          0 <= j + direction * player < DIMENSION and 
          board[i - player][j + direction * player] != 0):
        clearance = "La destination contient déjà un pion"
    elif (not (0 <= i - player < DIMENSION and 
          0 <= j + direction * player < DIMENSION)):
        clearance = "La destination du pion est en dehors du damier"
    else:
        clearance = True
    return clearance


def checkEndOfGame(board, player):
    """Verifie si la partie est terminée et dans ce cas renvoyer le joueur qui
    a gagné, 0 pour un match nul et False si la partie n’est pas encore
    terminée"""
    movementPlayer = False
    movementOtherPlayer = False
    for idxRow, row in enumerate(board):
        for idxColumn, column in enumerate(row):
            if idxRow < DIMENSION and idxColumn < DIMENSION:
                if column == player:
                    if (0 <= idxColumn + 1 < DIMENSION and
                       board[idxRow - player][idxColumn + 1] == 0):
                       movementPlayer = True
                    if (0 <= idxColumn - 1 < DIMENSION and 
                       board[idxRow - player][idxColumn - 1] == 0):
                       movementPlayer = True
                elif column == -player:
                    if (0 <= idxColumn + 1 < DIMENSION and 
                       board[idxRow + player][idxColumn + 1] == 0):
                       movementOtherPlayer = True
                    if (0 <= idxColumn - 1 < DIMENSION and 
                       board[idxRow + player][idxColumn - 1] == 0):
                       movementOtherPlayer = True
    if movementPlayer:
        gameEnd = False
    elif not movementPlayer and not movementOtherPlayer:
        gameEnd = 0
    else:
        gameEnd = -player
    return gameEnd
