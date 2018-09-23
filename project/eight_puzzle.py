#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Shihab Karim
# email: skarim9@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

# Number 1 of Task V
def process_file(filename, algorithm, param):
    """ Takes three inputs, filename, algorithm, and param
        and performs several tasks. It opens the file,
        filename, converts each line of the file into a
        digit string, takes steps to solve the eight puzzle,
        and reports the number of moves in solutions. Also,
        it performs a couple more cumulative computations
    """
    file = open(filename, 'r')
    puz_count = 0
    total_moves = 0
    total_states = 0

    for line in file:
        digitstr = line[:-1]
        init_board = Board(digitstr)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return
        soln = None
        try:
            soln = searcher.find_solution(init_state)
            if soln == None:
                print(digitstr + ':', \
                  'no solution', end='\n')
            else:
                print(digitstr + ':', soln.num_moves, \
                      'moves,', searcher.num_tested, \
                      'states tested')
                puz_count += 1
                total_moves += soln.num_moves
                total_states += searcher.num_tested
        except KeyboardInterrupt:
            print(digitstr + ':', \
                  'search terminated, no solution', end='\n')
        

    print('\n')
    if puz_count == 0:
        print('solved', puz_count, 'puzzles')
    else:
        avg_moves = total_moves / puz_count
        avg_states = total_states / puz_count
        print('solved', puz_count, 'puzzles')
        print('averages:', avg_moves, 'moves,', avg_states, \
              'states tested')

    file.close()
        
        
