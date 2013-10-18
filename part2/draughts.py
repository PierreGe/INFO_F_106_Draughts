# -*- coding: utf8 -*-
#
# INFO-F106 - Projet d'année - Partie 2
#
# GÉRARD Pierre  000379259


from draughtsFunctions import *
from config import *


def printCurrentPlayer(player):
    """ Imprime le joueur qui doit jouer"""
    if player == WHITE_PLAYER:
        print("C'est au tour du joueur avec les pièces blanches ({0}/{1})"
              .format(WHITE_PAWN, WHITE_KING))
    elif player == BLACK_PLAYER:
        print("C'est au tour du joueur avec les pièces noires ({0}/{1})"
              .format(BLACK_PAWN, BLACK_KING))


def inputActionChoice():
    """Verifie que le joueur choisit une option correcte"""
    print("Souhaitez vous :\n1) Déplacer une pièce \n2) Proposer une " +
          "partie nulle à l'adversaire\n3) Sauvegarder la partie \n4)" +
          " Restaurer la partie")
    choice = 0
    while not 0 < choice <= 4:
        while True:
            try:
                choice = int(input("  Entrez votre choix : "))
                break
            except ValueError:
                print ("Pensez à ne pas confondre chiffre et lettre")
            finally:
                print ("Veuillez répondre par 1,2,3 ou 4 : ")
    return choice


def inputCoordinates(board):
    """Verifie l'entrer du joueur lorsque qu'il effectuer un premier mouvment"""
    while True:
        try:
            j = input("Entrez la coordonnées en x [a-{0}] : "
                      .format(chr(ord("a") + len(board) - 1)))
            j = ord(j) - ord("a")
            i = input("Entrez la coordonnées en y [1-{0}] : "
                      .format(len(board)))
            i = int(i) - 1
            direction = input("Entrez la direction souhaité : ")
            direction = direction.upper()
            length = 1
            if abs(board[i][j]) == 2:
                length = int(input("Entrez la longueur du déplacement : "))
            return i, j, direction, length
        except TypeError:
            print("Veuillez entrer les coordonnées correctement")
            print("Pensez à n'enter qu'une seule lettre")
        except ValueError:
            print("Veuillez entrer les coordonnées correctement")
            print("Pensez à ne pas confondre chiffre et lettre")
        except IndexError:
            print("Vos coordonnées sont situé hors damier")


def inputCooAfterCapture(board, i, j):
    """Verifie l'entrer du joueur lors d'une rafle"""
    while True:
        try:
            direction = input("Entrez la direction souhaité : ")
            direction = direction.upper()
            length = 1
            if abs(board[i][j]) == 2:
                length = int(input("Entrez la longueur du déplacement : "))
            return direction, length
        except TypeError:
            print("Veuillez entrer les coordonnées correctement")
            print("Pensez à n'enter qu'une seule lettre")
        except ValueError:
            print("Veuillez entrer les coordonnées correctement")
            print("Pensez à ne pas confondre chiffre et lettre")


def inputYesOrNo():
    """Force l'utilisateur a repondre par oui ou par non a une question"""
    while True:
        yesOrNo = input().lower()
        if yesOrNo == "o" or yesOrNo == "n":
            return yesOrNo
        print("Veuillez repondre par oui ou par non (o/n) : ")


def printCapture(captI, captJ):
    """Imprime les coordonnées de la pièce capturé par le joueur"""
    i = captI + 1
    j = chr(captJ + ord("a"))
    print("Vous avez capturé la pièce adverse situé en ({0},{1})".format(j, i))


def main():
    """Fonction principal qui permet de lancer un jeu de dame avec des règles
    légérement modifiées"""
    print("Jeu de dame")
    board = initBoard(DIMENSION)
    if not board:
        raise Exception("Erreur de configuration: damier trop petit")
    player = WHITE_PLAYER  # Le joueur blanc à le trait
    endOfGame = checkEndOfGame(board, player)
    while isinstance(endOfGame, bool) and not endOfGame:
        print(79 * "-")
        printBoard(board, player)
        printCurrentPlayer(player)
        choice = inputActionChoice()
        if choice == 1:
            hasPlayed = False
            hasCaptured = False
            clearance = 1
            while clearance != 0:
                i, j, direction, length = inputCoordinates(board)
                clearance = checkMove(board, i, j, direction,
                                      player, length, hasPlayed, hasCaptured)
                if clearance != 0:
                    print("Votre déplacement n'est pas correct : ")
                    print(strerr(clearance))
            destination, capturedPawn = movePiece(board, i, j, direction,
                                                  length)
            destI, destJ = destination
            becomeKing(board, destI, destJ)
            if capturedPawn == None:
                print("Vous déplacer une pièce sans effectuer de capture")
            else:
                captI, captJ = capturedPawn
                capture(board, captI, captJ)
                hasCaptured = True
                printCapture(captI, captJ)
                printBoard(board, player)
                print("Souhaitez-vous poursuivre une rafle ? o/n : ")
                wantToPlay = inputYesOrNo()
                while (wantToPlay == "o" and
                      (isinstance(endOfGame, bool) and not endOfGame)):
                    direction, length = inputCooAfterCapture(board, destI,destJ)
                    clearance = checkMove(board, destI, destJ, direction,
                                          player, length, hasPlayed,hasCaptured)
                    if clearance != 0:
                        print("Votre déplacement n'est pas correcte : ")
                        print(strerr(clearance))
                    else:
                        destination, capturedPawn = movePiece(board, destI,
                                                              destJ, direction,
                                                              length)
                        destI, destJ = destination
                        becomeKing(board, destI, destJ)
                        captI, captJ = capturedPawn
                        capture(board, captI, captJ)
                        printCapture(captI, captJ)
                        endOfGame = checkEndOfGame(board, player)
                        printBoard(board, player)
                    if isinstance(endOfGame, bool) and not endOfGame :
                        print("Souhaitez-vous poursuivre une rafle ? o/n : ")
                        wantToPlay = inputYesOrNo()
            player = -player
            endOfGame = checkEndOfGame(board, player)
        elif choice == 2:
            player = - player
            printCurrentPlayer(player)
            print("L'adversaire vous propose un nul, acceptez-vous ? o/n : ")
            nulMatch = inputYesOrNo()
            if nulMatch == "o":
                endOfGame = 0
            elif nulMatch == "n":
                endOfGame = False
            player = - player
        elif choice == 3:
            print("Entrez le nom du fichier de sauvegarde (sans" +
                  " l'extension): ")
            saveFileName = input() + ".dat"
            try:
                save(saveFileName, board, player)
            except IOError:
                print("Erreur lors de l'écriture de : ", saveFileName)
            else:
                print("Souhaitez-vous continuer la partie ? o/n : ")
                choiceEndOfGame = inputYesOrNo()
                if choiceEndOfGame == "n":
                    endOfGame = True
        elif choice == 4:
            print("Entrez le nom du fichier que vous voulez charger (sans" +
                  " l'extension): ")
            saveFileName = input() + ".dat"
            try:
                player, board = load(saveFileName)
            except IOError:
                print("Erreur lors de la lecture de : ", saveFileName)
            except:
                print("Le fichier est probablement corrompue")
            else:
                endOfGame = checkEndOfGame(board, player)
    # Attention : isinstance(True,int) renvoi True !
    if not isinstance(endOfGame, bool) and endOfGame == 0:
        print("Le jeu se termine par un match nul")
    elif not isinstance(endOfGame, bool) and endOfGame == 1:
        print("Le jeu se termine par la victoire du joueur avec les pions" +
              " blancs")
    elif not isinstance(endOfGame, bool) and endOfGame == -1:
        print("Le jeu se termine par la victoire du joueur avec les pions" +
              " noirs")
    elif isinstance(endOfGame, bool) and endOfGame:
        print("Vous avez effectué une sauvegarde (La partie n'est pas" +
              " terminée)")


if __name__ == '__main__':
    main()
