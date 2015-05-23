
from person import *
from gameboard import * 
LOSE = 0
WIN = 1
INPLAY = 2 
class Ghost(Person):
	def __init__(self,x,y,index):
		Person.__init__(self,x,y)
		self.index = index
		
	def move(self,game):
		ghost_moved=0
		prevx=self.x
		prevy=self.y
		while not ghost_moved: 		
			move= randint(0,3)
		
			if move == 0:
				if (self.checkWall(self.x+1,self.y,game)):				
					self.x += 1
					ghost_moved = 1
	
			elif move == 1:
				if (self.checkWall(self.x-1,self.y,game)):
				        self.x -= 1
					ghost_moved = 1
	
			elif move == 2:
				if (self.checkWall(self.x,self.y-1,game)):				
					self.y -= 1
					ghost_moved = 1
	
			else:
				if (self.checkWall(self.x,self.y+1,game)):				
					self.y +=1
					ghost_moved = 1
		if ghost_moved:
			game.board[self.x][self.y] = 'G'
			if (prevx,prevy) in game.coin_pos:
				game.board[prevx][prevy]= 'C'
			else : 
				game.board[prevx][prevy]= '.'
			game.ghosts[self.index]= self
			game.ghosts_pos[self.index]=(self.x,self.y)
							
	
			
			 
	def ghostPosition(self):
		return (self.x, self.y)
