
from ghost import *
from gameboard import *
from person import * 
LOSE = 0
WIN = 1
INPLAY = 2 
class Pacman(Person):
	def __init__(self,x,y):
		Person.__init__(self,x,y)
	
	def move(self,game,move):
		pacman_moved = 0
		prevx=self.x
		prevy=self.y
		if move == 'a':	
			if self.checkWall(prevx,prevy - 1,game):
				self.y= self.y -1
				pacman_moved = 1		
		elif move == 's':
			if self.checkWall(prevx + 1,prevy,game):
				self.x= self.x + 1
				pacman_moved = 1
		elif move == 'd':
			if self.checkWall(prevx,prevy + 1,game):
				self.y= self.y + 1
				pacman_moved = 1
		elif move == 'w':
			if self.checkWall(prevx-1,prevy,game):
				self.x= self.x - 1
				pacman_moved = 1
		
		else: 
			print "Illegal Move : Press either 'a', 'w', 'd' , 's' to move or Press 'q' to quit "   
		

		if pacman_moved == 1:
			game.board[prevx][prevy]='.'
			game.board[self.x][self.y]='P'		
			if ((self.x,self.y) in game.coin_pos):
				self.collectCoin(game)

	def collectCoin(self,game):
		game.coin_pos.remove((self.x,self.y))				
		game.score += 1
		game.coins_left -= 1		 
		

