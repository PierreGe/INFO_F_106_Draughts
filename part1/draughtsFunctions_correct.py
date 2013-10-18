#!/usr/bin/python
# -*- coding: utf8 -*-

from math import *
from config import *


def initBoard(dimension):
	myboard = [ [ FREE_SPACE for i in range(dimension) ] for j in range(dimension) ]
	
	for i in range(int(dimension/2)-1):
		for j in range(1-i%2,dimension,2):
			myboard[i][j]=BLACK_PLAYER
	for i in range(dimension-int(dimension/2)+1,dimension):
		for j in range(1-i%2,dimension,2):
			myboard[i][j]=WHITE_PLAYER
		

		
	return(myboard)



def playerColor(value):
	return value/abs(value)
	

def printBoard(myboard,toplay):
	dimension = len(myboard)
	order = range(dimension) if(toplay==WHITE_PLAYER) else range(dimension-1,-1,-1)
	for row in order:
		#line = ''
		for col in order:
			char = WHITE_SQUARE
			if(myboard[row][col]!=0):# filled case
				# define the array index of the player
				currentPiece = WHITE_PAWN if(playerColor(myboard[row][col]) == WHITE_PLAYER) else BLACK_PAWN
				# define char for simple piece or king 
			
				char = currentPiece
			elif((row+col)%2!=0): char = BLACK_SQUARE# update if black case and no piece
			print(char,sep='',end=' ')
		print('| ',row+1,sep='')
	for i in order: print('-',sep='',end=' ')
	print()
	for pos in order : print(chr(pos+ord('a')),sep='',end=' ')
	print()

def getNewCoord(board,x,y,direction,player):
	dimension=len(board)	
	if	player== WHITE_PLAYER:
		if direction=='L':
			newpos=[player,x-1,y-1]
		elif direction=='R':
			newpos=[player,x-1,y+1]
	elif player== BLACK_PLAYER:
		if direction=='L':
			newpos=[player,x+1,y+1]
		elif direction=='R':
			newpos=[player,x+1,y-1]

	return(newpos)
	
def movePiece(board,x,y,direction):
	dimension=len(board)
	newpos=getNewCoord(board,x,y,direction,board[x][y])
	board[x][y]= FREE_SPACE
	board[newpos[1]][newpos[2]]=newpos[0]
	

def checkMove(board,x,y,direction,player):
	dimension=len(board)
	if board[x][y]!=player:
		return('The player does not have a piece on the chosen square')

	(player,xnew,ynew)=getNewCoord(board,x,y,direction,player)

	if xnew < 0 or ynew < 0 or xnew>=dimension or ynew >=dimension:
		return('Figure is being moved outside the board')
	elif(board[xnew][ynew] != FREE_SPACE):
		return('New square is already occupied')
	
	return(True)


def checkEndOfGame(board,player):
	dimension=len(board)
	possMovesPlayer=checkEndOfGameForPlayer(board,player)
	possMovesPlayer2=checkEndOfGameForPlayer(board,player*(-1))

	if (not possMovesPlayer) and (not possMovesPlayer2):
		return(0)
	elif (not possMovesPlayer):
		return(player*(-1))
	else:
		return(False)
	
def checkEndOfGameForPlayer(board,player):
	dimension=len(board)
	for i in range(0,dimension):
		for j in range(dimension):
			if board[i][j]==player:
				poss=checkMove(board,i,j,'L',player)
				if poss==True:
					return(1)
					
				poss=checkMove(board,i,j,'R',player)
				if poss==True:
					return(1)

	return(0)

					
	
	
	
	
	