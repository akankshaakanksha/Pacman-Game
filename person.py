from gameboard import *
class Person:

	def __init__(self,x,y):
		self.x= x 
		self.y=y

	
	def checkWall(self,x,y,game):
		if x>=0 and y>=0 and x<15 and y<35 and game.board[x][y]!= 'X':
			return 1
		else:
			return 0
