
import sys

from draughtsFunctions import *
from config import *
from testCases import *

def initTestBoard1(dimension):
	myboard = [ [ FREE_SPACE for i in range(dimension) ] for j in range(dimension) ]
	myboard[0][0]= BLACK_PLAYER
	myboard[0][2]= BLACK_PLAYER
	myboard[1][1]= WHITE_PLAYER
	return(myboard)
	
def initTestBoard2(dimension):
	myboard = [ [ 0 for i in range(dimension) ] for j in range(dimension) ]
	myboard[0][9]= BLACK_PLAYER
	myboard[1][8]= WHITE_PLAYER
	myboard[4][9]= WHITE_PLAYER
	return(myboard)
	
def initTestBoard3(dimension):
	myboard=initBoard(dimension)
	
	myboard[4][1]= BLACK_PLAYER
	myboard[4][3]= BLACK_PLAYER
	myboard[4][5]= BLACK_PLAYER
	myboard[4][7]= BLACK_PLAYER
	myboard[4][9]= BLACK_PLAYER
	
	myboard[5][0]= WHITE_PLAYER
	myboard[5][2]= WHITE_PLAYER
	myboard[5][4]= WHITE_PLAYER
	myboard[5][6]= WHITE_PLAYER
	myboard[5][8]= WHITE_PLAYER

	return(myboard)
