#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Shihab Karim
# email: skarim9@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from board import *

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    # Number 1
    def __init__(self, board, predecessor, move):
        """ a constructor that constructs a new State object
            by initializing four attributes, board,
            predecessor, move, and num_moves
        """
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if self.predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = 1 + self.predecessor.num_moves
        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True

    # Number 2
    def is_goal(self):
        """ Returns True if the called State object is a goal
            state, and False otherwise
        """
        if self.board.tiles == GOAL_TILES:
            return True
        else:
            return False

    # Number 3
    def generate_successors(self):
        """ Creates and returns a list of State objects for
            all successor states of the called State object
        """
        successors = []
        for x in MOVES:   
            b2 = self.board.copy()
            if b2.move_blank(x) == True:
                successor = State(b2, self, x)
                successors += [successor]
        return successors

    # Number 7 of Task III
    def print_moves_to(self):
        """ Prints the sequence of moves that lead from the
            initial state to the State object
        """
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
        else:
            s = self.predecessor.print_moves_to()
            print('move the blank ' + self.move)
            print(self.board)
                
