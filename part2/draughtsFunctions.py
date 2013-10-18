# -*- coding: utf8 -*-
#
# INFO-F106 - Projet d'année - Partie 2
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
    """Imprime le damier avec les pions et les dames de l'utilisateurs situés
    en dessous pour faciliter la lecture de ce dernier """
    if player == -1:
        for idxRow, row in enumerate(reversed(list(board))):
            for idxColumn, column in enumerate(reversed(list(row))):
                if column == 1:
                    print(WHITE_PAWN, " ", end="")
                elif column == -1:
                    print(BLACK_PAWN, " ", end="")
                elif column == 2:
                    print(WHITE_KING, " ", end="")
                elif column == -2:
                    print(BLACK_KING, " ", end="")
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
                elif column == 2:
                    print(WHITE_KING, " ", end="")
                elif column == -2:
                    print(BLACK_KING, " ", end="")
                elif (idxRow + idxColumn) % 2 == 0:
                    print(WHITE_SQUARE, " ", end="")
                else:
                    print("   ", end="")
            print(" |", idxRow + 1)
        print("_  " * len(board))
        for i in range(len(board)):
            print(chr(ord("a") + i) + "  ", end="")
        print("")


def playerColor(value):
    """Renvoi le joueur a qui appartient le pion passé en paramètre"""
    return value / abs(value)


def getNewCoord(board, i, j, direction, player, length=1):
    """Retourne les coordonnées de la destination du pion et les coordonnées
    de la case situé après (ignore les limites du damier)"""
    if player == WHITE_PLAYER:
        if direction == 'L':
            newpos = (i - length, j - length)
            nextpos = (i - length - 1, j - length - 1)
        elif direction == 'R':
            newpos = (i - length, j + length)
            nextpos = (i - length - 1, j + length + 1)
        elif direction == "LB":
            newpos = (i + length, j - length)
            nextpos = (i + length + 1, j - length - 1)
        elif direction == "RB":
            newpos = (i + length, j + length)
            nextpos = (i + length + 1, j + length + 1)
    elif player == BLACK_PLAYER:
        if direction == 'L':
            newpos = (i + length, j + length)
            nextpos = (i + length + 1, j + length + 1)
        elif direction == 'R':
            newpos = (i + length, j - length)
            nextpos = (i + length + 1, j - length - 1)
        elif direction == "LB":
            newpos = (i - length, j + length)
            nextpos = (i - length - 1, j + length + 1)
        elif direction == "RB":
            newpos = (i - length, j - length)
            nextpos = (i - length - 1, j - length - 1)
    return(newpos, nextpos)


def movePiece(board, i, j, direction, length=1):
    """ Deplace une pièce sur le damier et retourne ses nouvelles coordonnées
    et s'il y a une capture de pions les coordonnées du pion capturé"""
    pawn = board[i][j]
    player = playerColor(pawn)
    newpos, nextpos = getNewCoord(board, i, j, direction, player, length)
    if board[newpos[0]][newpos[1]] != 0:
        res = (nextpos, newpos)
        board[i][j] = 0
        board[nextpos[0]][nextpos[1]] = pawn
    else:
        res = (newpos, None)
        board[i][j] = 0
        board[newpos[0]][newpos[1]] = pawn
    return res


def checkMove(board, i, j, direction, player, length=1, hasPlayed=False,
              hasCaptured=False):
    """Verifie si le coup joué par le joueur est valide Elle retournera le code
    erreur correspondant a la situation. Elle gere les erreurs suivantes :
            NO_ERROR
            PAWN_ONLY_ONE_MOVE
            BAD_DIRECTION_FORMAT
            ONLY_KING_GO_BACK
            SPACE_OCCUPIED
            CANNOT_JUMP_OUTSIDE
            TOO_LONG_JUMP
            CANNOT_GO_OUTSIDE
            NO_FREE_WAY
            NO_PIECE
            OPPONENT_PIECE
            MUST_CAPTURE
            + hasPlayed==True et hasCaptured==False : MUST_CAPTURE
    """
    if direction not in ("R", "L", "RB", "LB"):
        return BAD_DIRECTION_FORMAT
    pawn = board[i][j]
    if pawn == FREE_SPACE:
        return NO_PIECE
    if playerColor(pawn) != player:
        return OPPONENT_PIECE
    newpos, nextpos = getNewCoord(board, i, j, direction, player, length)
    if (not 0 <= newpos[0] < len(board) or not 0 <= newpos[1] < len(board)):
        return CANNOT_GO_OUTSIDE
    if (board[newpos[0]][newpos[1]] != 0 and
            playerColor(board[newpos[0]][newpos[1]]) == player):
        return SPACE_OCCUPIED
    if abs(pawn) == 1:  # Si c'est un pion
        if length != 1:
            return PAWN_ONLY_ONE_MOVE
        if (board[newpos[0]][newpos[1]] != 0 and
                playerColor(board[newpos[0]][newpos[1]]) == -player):
            #Prise
            if (not 0 <= nextpos[0] < len(board) or
                    not 0 <= nextpos[1] < len(board)):
                return CANNOT_JUMP_OUTSIDE
            if board[nextpos[0]][nextpos[1]] != 0:
                return TOO_LONG_JUMP
        else:
            # Pas de prise
            if direction == "RB" or direction == "LB":
                return ONLY_KING_GO_BACK
            if hasCaptured == True:
                return MUST_CAPTURE
    if abs(pawn) == 2:  # Si c'est une dame
        if length - 1 > countFree(board, i, j, direction):
            return NO_FREE_WAY
        if (board[newpos[0]][newpos[1]] != 0 and
                playerColor(board[newpos[0]][newpos[1]]) == -player):
            # Prise
            if (not 0 <= nextpos[0] < len(board) or
                    not 0 <= nextpos[1] < len(board)):
                return CANNOT_JUMP_OUTSIDE
            if board[nextpos[0]][nextpos[1]] != 0:
                return TOO_LONG_JUMP
        else:
            # Pas de prise
            if hasCaptured == True:
                return MUST_CAPTURE
    if hasPlayed and not hasCaptured:
        return MUST_CAPTURE  # A verifier lors de la partie 3
    return NO_ERROR


def checkEndOfGame(board, player):
    """Verifie si la partie est terminée et dans ce cas renvoyer le joueur qui
    a gagné, 0 pour un match nul et False si la partie n’est pas encore
    terminée"""
    possMovesPlayer, pawnLeftPlayer = checkEndOfGameForPlayer(board, player)
    possMovesPlayer2, pawnLeftPlayer2 = checkEndOfGameForPlayer(board, -player)
    if (not possMovesPlayer) and (not possMovesPlayer2):
        return(0)
    elif (not possMovesPlayer):
        return(player * (-1))
    elif possMovesPlayer and not pawnLeftPlayer2:
        return player
    else:
        return(False)


def checkEndOfGameForPlayer(board, player):
    """Verifie si la partie est terminé pour le joueur passé en paramètre
    et retourne un tuple dont le premier element est un bool qui indique si
    le joueur peut encore se déplacer et le deuxième element est un bool
    qui indique si l'autre joueur possède encore des pions"""
    pawnLeft = False
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and playerColor(board[i][j]) == player:
                pawnLeft = True
                poss = checkMove(board, i, j, 'L', player)
                if poss == 0:
                    return True, pawnLeft
                poss = checkMove(board, i, j, 'LB', player)
                if poss == 0:
                    return True, pawnLeft
                poss = checkMove(board, i, j, 'R', player)
                if poss == 0:
                    return True, pawnLeft
                poss = checkMove(board, i, j, 'RB', player)
                if poss == 0:
                    return True, pawnLeft
    return 0, pawnLeft


def becomeKing(board, i, j):
    """Transforme le pion situé en (i,j) en dame si nécessaire"""
    if i == 0 and board[i][j] == WHITE_PLAYER:
        board[i][j] = 2
    elif i == (len(board) - 1) and board[i][j] == BLACK_PLAYER:
        board[i][j] = -2


def capture(board, i, j):
    """Enleve une piece capturée du damier"""
    board[i][j] = 0


def countFree(board, i, j, direction, player=None, length=0):
    """Compte recursivement le nombre de case libre avant un obstacle (pion ou
    limite du damier)"""
    if player == None:
        pawn = board[i][j]
        player = playerColor(pawn)
    newpos, nextpos = getNewCoord(board, i, j, direction, player)
    i, j = newpos
    if (not(0 <= i < len(board)) or
            not (0 <= j < len(board)) or board[i][j] != 0):
        res = length
    else:
        length += 1
        res = countFree(board, i, j, direction, player, length)
    return res


def strerr(errCode):
    """Convertit le code d'erreur en un message console plus explicite"""
    if errCode == 0:
        return ("Pas d’erreur, le coup est autorisé")
    if errCode == 1:
        return ("Vous ne pouvez pas déplacer un pion de plus d’une case en" +
                " diagonale")
    if errCode == 2:
        return ("Le format de déplacement que vous avez entré n’est pas bon " +
                "(seulement L, R, LB et RB)")
    if errCode == 3:
        return ("Vous ne pouvez pas déplacer un pion en arrière sans capture")
    if errCode == 4:
        return ("Vous ne pouvez pas déplacer une pièce sur une case qui est " +
                "déjà occupée")
    if errCode == 5:
        return ("Vous ne pouvez pas déplacer une pièce pour capturer un pion" +
                " si la capture aboutit à l’extérieur du damier")
    if errCode == 6:
        return ("Vous ne pouvez pas déplacer une pièce au-dessus de plusieurs" +
                " autres pièces")
    if errCode == 7:
        return ("Vous ne pouvez pas déplacer une pièce à l’extérieur du damier")
    if errCode == 8:
        return ("Lorsque vous essayez de déplacer une dame en capturant" +
                " une pièce adverse vous ne pouvez pas la deposer ailleurs que"+
                " dans la case qui suit la capture")
    if errCode == 9:
        return ("Vous avez entré des coordonnées du damier où il n’y a pas" +
                " de pièce")
    if errCode == 10:
        return ("Vous ne pouvez pas déplacer une pièce adverse")
    if errCode == 11:
        return ("Vous ne pouvez pas poursuivre une rafle sans capturer une " +
                "pièce adverse")


def save(filename, board, player):
    """Sauvegarde le damier et joueur qui doit jouer dans un fichier .dat """
    stringToSave = str(player) + "\n"
    stringToSave += str(len(board)) + "\n"
    for ligne in board:
        stringToSave += " ".join(map(str, ligne)) + "\n"
    saveFile = open(filename, "w")
    saveFile.write(stringToSave)
    saveFile.close()


def load(filename):
    """Charge une partie précédemment enregistrée pour en extraire un damier
    sa dimension et le joueur qui devait jouer """
    savedFile = open(filename, "r")
    lineList = savedFile.readlines()
    savedFile.close()
    player = int(lineList[0].strip())
    dimension = int(lineList[1].strip())
    board = [[0 for i in range(dimension)]for j in range(dimension)]
    for indexRow, row in enumerate(lineList[2:]):
        row = row.strip().split(" ")
        for indexColumn, column in enumerate(row):
            board[indexRow][indexColumn] = int(column)
    return player, board
