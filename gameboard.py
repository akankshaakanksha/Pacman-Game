
from random import randint,random 
from pacman import *
from ghost import *

LOSE = 0
WIN = 1
INPLAY = 2 
class Gameboard:
	def __init__(self,n_coins,n_walls,n_ghosts):
		self.n_coins=n_coins
        	self.n_walls=n_walls
        	self.n_ghosts=n_ghosts
		self.coin_pos=[]
		self.wall_pos=[]
		self.ghosts_pos=[]
		self.ghosts=[]
		
     
	
        def plain_board(self):    
       		self.board = [['.' for x in xrange(35)] for y in range(15)]
		
	def coin_populate(self):
	       	Coins_ToBePlaced=self.n_coins
		while Coins_ToBePlaced:
			i = randint(0,14)
			j = randint(0,34)
			if self.board[i][j] == '.':
				Coins_ToBePlaced -= 1
				self.board[i][j] = 'C'
				self.coin_pos = self.coin_pos + [(i,j)]
				   	    
	def wall_populate(self):
		Walls_ToBePlaced=self.n_walls
		while Walls_ToBePlaced:
			i = randint(0,14)
			j = randint(0,34)
			if self.board[i][j] == '.':
				Walls_ToBePlaced -= 1
				self.board[i][j] = 'X'
				self.wall_pos = self.wall_pos + [(i,j)]
	def place_pacman(self):
		Pacman_IsNotPlaced=1
		while Pacman_IsNotPlaced:				
			i = randint(0,14)
			j = randint(0,34)
 			if self.board[i][j] == '.':
				self.board[i][j]='P'	
				self.pacman=Pacman(i,j)
				self.pacman_pos = (i,j)
				Pacman_IsNotPlaced = 0 

		
	def place_ghost(self):
		Ghost_IsPlaced=0
		while not Ghost_IsPlaced:				
			i = randint(0,14)
			j = randint(0,34)
 			if self.board[i][j] == '.':	
				self.board[i][j] = 'G'
				index=len(self.ghosts)
				self.ghosts = self.ghosts + [Ghost(i,j,index)] 								
				self.ghosts_pos = self.ghosts_pos + [(i,j)]
				Ghost_IsPlaced = 1
	def place_allghosts(self):
		for i in range(self.n_ghosts):
			self.place_ghost()
	
	def makeBoard(self):
		self.plain_board()
		self.coin_populate()
		self.wall_populate()
		self.place_pacman()
		self.place_allghosts()
			

	def print_board(self):
		print self.level		
		for i in range(15):
			for j in range(35): 
				print self.board[i][j],
			print '\n'


class Game(Gameboard): 
	def __init__(self,n_coins,n_walls,n_ghosts): 
		Gameboard.__init__(self,n_coins,n_walls,n_ghosts)		
		self.score=0
		self.level=1
		self.gameState = INPLAY
		self.coins_left=n_coins
	
	def getMove(self):
		move=raw_input('Enter Move:')
		if move == 'q': 
			print 'You quit'			
			exit()
		else:
			return move
	def makeMove(self):
		"""
		ghosts move first
		"""		
		for i in self.ghosts:
			i.move(self)
		"""
		pacman makes its move
		"""
                m = self.getMove()
		self.pacman.move(self,m)

	def checkEnd(self):
		pacman_currentposition= (self.pacman.x,self.pacman.y)
		for i in self.ghosts:
			if (i.ghostPosition() == pacman_currentposition):
				self.gameState= LOSE
				return 1
		return 0

	def changeLevel(self):
		self.level +=1
		self.n_coins= 20 + self.level * 5
		self.n_ghosts = self.level 
		self.coin_pos=[]
		self.wall_pos=[]
		self.ghosts=[]
		self.ghosts_pos=[]
		self.ghosts_pos=[]
		self.coins_left=self.n_coins
		self.makeBoard()
		
	
	def playGame(self):
		while(1):		
			while self.coins_left:		
				self.makeMove()
				if not self.checkEnd():
					self.print_board()
					self.scoreDisplay()
				else: 
					print "You Lost :( \n Game End"
					exit()
			print "Level Completed \n "
			self.changeLevel()
			self.print_board()
	
	 
	
			
	def scoreDisplay(self):
		print 'Score: ', self.score
	
	def print_board(self):
		print 'Level:' ,self.level		
		for i in range(15):
			for j in range(35): 
				print self.board[i][j],
			print '\n'

