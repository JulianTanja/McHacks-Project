#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:03:25 2021

@author: andrewtuckman
"""
class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
            """ constructs a new Board object
                inputs: two positive numbers for height and width
            """
            self.height = height
            self.width = width
            self.slots = [[' '] * width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation of a Board object.
        """
        s = ''        
        for row in range(self.height):
            s += '|'   

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  
            
        s += (2 * self.width + 1) * '-'
        s += '\n'
        s += ' '
        for col in range(self.width):
            if col > 9:
                col = col % 10
            s += str(col)
            s += ' '
        return s

    def add_checker(self, checker, col):
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        row = -1
        for i in range(self.height):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break
            else:
                row -= 1
                
    def reset(self):
        """ reset the Board object on which it is called by setting all slots
            to contain a space character
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
                
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column col
            on the calling Board object. Otherwise, it should return False
        """
        if 0 > col or col > (self.width - 1):
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False
    
    def is_full(self):
        """ returns True if the called Board object is completely full of 
            checkers, and returns False otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board 
            object. If the column is empty, then the method should do nothing
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
          
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False
  
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal-up win for the specified checker
        """
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal-down win for the specified checker
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False
              
    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O', and returns
        True if there are four consecutive slots containing checker on the board.
        Otherwise, returns False.
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_down_diagonal_win(checker) == True:
            return True
        if self.is_up_diagonal_win(checker) == True:
            return True
        if self.is_vertical_win(checker) == True:
            return True
        if self.is_horizontal_win(checker) == True:
            return True
        return False

class Player:
    def __init__(self, checker):
        """ constructs a new Player object
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        
    def __repr__(self):
        """ returns a string representing a Player object
        """
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of 
            the Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'       
           
import random
import time
    
def connect_four(p1, p2, bet):
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!', '\n')
    b = Board(6, 7)
    print(b)
    while True:
        if process_move(p1, b, bet) == True:
            return b

        if process_move(p2, b, bet) == True:
            return b

def process_move(p, b, bet):
    """ takes two parameters: a Player object p for the player whose move
        is being processed, and a Board object b for the board on which the
        game is being played.
        It returns True if a win or a tie, and False otherwise
    """
    global coordinates
    nxt_move = p.next_move(b)
    b.add_checker(p.checker, nxt_move)
    #time.sleep(.6)
    print(b)
    for x in range(len(b.slots)):
        for y in range(len(b.slots[0])):
            if b.slots[x][y]!=' ' and [x,y] not in coordinates:
                coordinates +=[[x,y]]
                print(coordinates)
    if b.is_win_for(p.checker):
        print(str(p.checker), ' wins.')
        if (p.checker == bet):
            global bet_validity
            bet_validity =  True
            print('Congratulations! You bet correctly!')
        else:
            print('You idiot, you guessed wrong.')
        return True
    elif b.is_full():
        print('\n' + "It's a tie!")
        return True
    else:
        return False

class AIPlayer(Player):
    """ creates a more “intelligent” computer player – one that uses
        techniques from artificial intelligence (AI) to choose its next move
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        return 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) \
        + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the
            board, and that returns the index of the column with the maximum
            score
        """
        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores += [i]
        if self.tiebreak == 'LEFT':
            return max_scores[0]
        if self.tiebreak == 'RIGHT':
            return max_scores[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_scores)
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s 
            scores for the columns in b
        """
        scores =  [10] * len(range(b.width))
        for col in range(b.width):
            if not b.can_add_to(col):
                scores[col] = -1
            elif b.is_win_for(self.checker):
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 50:
                    scores[col] = 50
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move
        """
        scores = self.scores_for(b)
        return self.max_score_column(scores)

  
bet = input("Which player do you think will win?: ")   

bet_validity = False
coordinates = []

p1 = AIPlayer('X', 'RANDOM', 2)
p2 = AIPlayer('O', 'RANDOM', 2)
connect_four(p1, p2, bet)



print(coordinates)
      
