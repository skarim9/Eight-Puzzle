#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Shihab Karim
# email: skarim9@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    # Number 1
    def __init__(self, depth_limit):
        """ a constructor that constructs a new Searcher
            object by initializing the following attributes,
            states(untested states), num_tested(tested
            states), and depth limit(how deep state-space
            search tree Searcher will go)
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    # Number 2
    def add_state(self, new_state):
        """ Takes a single State object called new_state and
            adds it to the Searcher's list of untested states
        """
        self.states += [new_state]

    # Number 3
    def should_add(self, state):
        """ Takes a State object called State and returns
            True if the called Searcher should add state to
            its list of untested states and False otherwise.
        """
        if self.depth_limit != -1 and \
           state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True

    # Number 4
    def add_states(self, new_states):
        """ Takes a list of State objects called new_states,
            and processes the elements of new_states one at
            a time
        """
        for x in new_states:
            if self.should_add(x) == True:
                self.add_state(x)

    # Number 5
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    # Number 6
    def find_solution(self, init_state):
        """ Performs a full state-space search that begins
            at the specified initial state init-state and
            ends when the goal state is found or when the
            Searcher runs out of untested states
        """
        self.add_state(init_state)
        while len(self.states) > 0:
            s = self.next_state()
            if s.is_goal() == True:
                self.num_tested += 1
                return s
            else:
                self.num_tested +=1
                self.add_states(s.generate_successors())
        return None

### Add your BFSeacher and DFSearcher class definitions below. ###
# Number 1 of Task IV
class BFSearcher(Searcher):
    """ a subclass of the Searcher class that performs
        breadth-first search (BFS) instead of random search
    """

    def next_state(self):
        """ Overrides the next_state method that is inherited
            from Searcher. Instead of randomly choosing from
            a list of untested states, this version of
            next_state should follow FIFO ordering
        """
        s = self.states[0]
        self.states.remove(s)
        return s

# Number 2 of Task IV
class DFSearcher(Searcher):
    """ a subclass of the Searcher class that performs depth-
        first search (DFS) instead of random search
    """

    def next_state(self):
        """ Overrides the next_state method that is inherited
            from Searcher. Instead of randomly choosing from
            a list of untested states, this version of
            next_state should follow LIFO ordering
        """
        s = self.states[-1]
        self.states.remove(s)
        return s


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
# Number 4d
def h1(state):
    """ a heuristic function that takes a State object
        called state, and that computes and returns an
        estimate of how many additional moves are needed to
        get from state to the goal state
    """
    return state.board.num_misplaced()

# Number 4b of Task V
def h2(state):
    """ a heuristic function that takes a State object called
        state, and that computes and returns a more accurate
        estimate than h1 of how many additional moves
        are needed to get from state to the goal state. This
        function takes into account the current and
        respective positions of each tile and how many turns
        does each tile need in order to reach their
        respective goal position. 
    """
    return state.board.turns_from_goal()


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    # Number 4b
    def __init__(self, heuristic):
        """ a constructor that constructs a new
            GreedySearcher object
        """
        super().__init__(-1)
        self.heuristic = heuristic
        

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

    # Number 4c
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    # Number 4e
    def add_state(self, state):
        """ Overrides the add_state method that is inherited
            from Searcher. Method should add a sublist that
            is a [priority, state] pair, where priority is
            the priority of state that is determined by the
            priority method
        """
        p = self.priority(state)
        self.states += [[p, state]]

    # Number 4f
    def next_state(self):
        """ Overrides the next_state method that is inherited
            from Searcher. This version of next_state should
            choose one of the states with the highest
            priority
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]

### Add your AStarSeacher class definition below. ###
# Number 5
class AStarSearcher(GreedySearcher):
    """ a subclass of the GreedySearcher class. It inherits
        from both GreedySearcher and the Searcher class since
        GreedySearcher inherits from the Searcher class.
        This class performs the A* search
    """
    def priority(self, state):
        """ Overrides the priority method from the
            GreedySearcher class. This version computes the
            priority using the heuristic function and
            number of moves it took to get to that state from
            the initial state
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
