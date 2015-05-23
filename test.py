import unittest
from gameboard import *

game = Game(20,20,1)
game.makeBoard()
moves = ['a','w','s','d']
class test(unittest.TestCase):
    prevx,prevy = game.pacman.x,game.pacman.y
    game.print_board()
    game.pacman.move(game,'a')
    x,y = game.pacman.x,game.pacman.y
    if  game.board[prevx-1][prevy] == 'X' :
        assert(prevx==x)
        assert(prevy == y )
    else:
        assert(x == prevx -1 )
        assert(prevy == y)

