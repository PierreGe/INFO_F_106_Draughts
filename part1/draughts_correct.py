#!/usr/bin/python
# -*- coding: utf8 -*-

from draughtsFunctions_correct import *
from config import *

myboard=initBoard(DIMENSION)
currentPlayer=WHITE_PLAYER
printBoard(myboard,currentPlayer)

possMov=0
gameOver=checkEndOfGame(myboard,currentPlayer)

while isinstance(gameOver,bool) and not gameOver:
	while(possMov!=True):
		if currentPlayer==WHITE_PLAYER:
			toPlay=WHITE_PAWN
		else:
			toPlay=BLACK_PAWN
		print('Player',toPlay,', please select the coordinates and the direction L or R of play!')
		x=(str(input('x coordinate, [a-j] ')))
		xNum=ord(x.lower())-ord('a')+1
		y=(int(input('y coordinate, [1-10] ')))
		
		direction=str(input('direction: L or R '))
		
		possMov=checkMove(myboard,y-1,xNum-1,direction.upper(),currentPlayer)
		if(possMov!=True):
			print(possMov)
	
	movePiece(myboard,y-1,xNum-1,direction.upper())
	
	currentPlayer=currentPlayer*(-1)
	gameOver=checkEndOfGame(myboard,currentPlayer)
	printBoard(myboard,currentPlayer)
	possMov=0
	
if gameOver==0 and not isinstance(gameOver,bool):
	print('Draw game')
elif gameOver==1 or gameOver== -1:
	print('Player', (WHITE_PAWN if gameOver == WHITE_PLAYER else BLACK_PAWN), 'won')
