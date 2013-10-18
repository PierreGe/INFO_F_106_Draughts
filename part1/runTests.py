#!/usr/local/bin/python3
# -*- coding: utf8 -*-

import sys

from draughtsFunctions import *
from config import *
from testCases import *

myboard=initBoard(DIMENSION)
print('\nInitial board:\n')
printBoard(myboard,WHITE_PLAYER)
print('\n-----------------------\n')
printBoard(myboard,BLACK_PLAYER)
print('\n-----------------------')
print('\n-----------------------\n')

myboard=initTestBoard1(DIMENSION)
print('\n when player ',WHITE_PLAYER,'started: ')
printBoard(myboard,WHITE_PLAYER)
print(checkEndOfGame(myboard,1))

print('\n when player ',BLACK_PLAYER,'started: ')
printBoard(myboard,BLACK_PLAYER)
print(checkEndOfGame(myboard,BLACK_PLAYER))
print('\n-----------------------')
print("")
print('\n-----------------------\n')


myboard=initTestBoard2(DIMENSION)
printBoard([ [ 0 for i in range(10) ] for j in range(10) ],1)
printBoard(myboard,WHITE_PLAYER)
print(' ')
print(checkEndOfGame(myboard,WHITE_PLAYER))

printBoard(myboard,BLACK_PLAYER)
print(' ')
print(checkEndOfGame(myboard,BLACK_PLAYER))
print('\n-----------------------\n')
print('\n-----------------------\n')


myboard=initTestBoard3(DIMENSION)
print(' ')
printBoard(myboard,WHITE_PLAYER)
printBoard(myboard,BLACK_PLAYER)
print(checkEndOfGame(myboard,WHITE_PLAYER))
