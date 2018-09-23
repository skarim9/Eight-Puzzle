#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Shihab Karim
# email: skarim9@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        # Number 1
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = int(digitstr[3*r + c])
                if int(digitstr[3*r + c]) == 0:
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###

    # Number 2
    def __repr__(self):
        """ Returns a string representation of a Board
            object
        """
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == 0:
                    s += '_ '
                else:
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'
        return s

    # Number 3
    def move_blank(self, direction):
        """ Takes a string input, direction, that specifies
            the direction in which the blank should move
            and attempts to modify the contents of the
            called Board object accordingly. Will return True
            or False to indicate whether the requested move
            was possible
        """
        direct_list = ['up', 'down', 'left', 'right']
        if direction not in direct_list:
            print('unknown direction: ' + direction)
            return False
        else:
            if direction == 'up':
                new_blank_r = self.blank_r - 1
                if new_blank_r < 0:
                    return False
                else:
                    orig_num = self.tiles[new_blank_r][self.blank_c]
                    self.tiles[new_blank_r][self.blank_c] = 0
                    self.tiles[self.blank_r][self.blank_c] = orig_num
                    self.blank_r = new_blank_r
                    return True
            elif direction == 'down':
                new_blank_r = self.blank_r + 1
                if new_blank_r > 2:
                    return False
                else:
                    orig_num = self.tiles[new_blank_r][self.blank_c]
                    self.tiles[new_blank_r][self.blank_c] = 0
                    self.tiles[self.blank_r][self.blank_c] = orig_num
                    self.blank_r = new_blank_r
                    return True
            elif direction == 'right':
                new_blank_c = self.blank_c + 1
                if new_blank_c > 2:
                    return False
                else:
                    orig_num = self.tiles[self.blank_r][new_blank_c]
                    self.tiles[self.blank_r][new_blank_c] = 0
                    self.tiles[self.blank_r][self.blank_c] = orig_num
                    self.blank_c = new_blank_c
                    return True
            else:
                new_blank_c = self.blank_c - 1
                if new_blank_c < 0:
                    return False
                else:
                    orig_num = self.tiles[self.blank_r][new_blank_c]
                    self.tiles[self.blank_r][new_blank_c] = 0
                    self.tiles[self.blank_r][self.blank_c] = orig_num
                    self.blank_c = new_blank_c
                    return True

    # Number 4
    def digit_string(self):
        """ creates and returns a string of digits that
            corresponds to the current contents of the called
            Board object's tiles attribute
        """
        s = ''
        for r in range(3):
            for c in range(3):
                s += str(self.tiles[r][c])
        return s

    # Number 5
    def copy(self):
        """ returns a newly-constructed Board object that
            is a deep copy of the called object
        """
        digitstr = self.digit_string()
        self_copy = Board(digitstr)
        return self_copy

    # Number 6
    def num_misplaced(self):
        """ Counts and returns the number of tiles in the
            called Board object that are not where they
            should be in the goal state
        """
        count = 0
        if self.tiles[0][1] != 1:
            count += 1
        if self.tiles[0][2] != 2:
            count += 1
        if self.tiles[1][0] != 3:
            count += 1
        if self.tiles[1][1] != 4:
            count += 1
        if self.tiles[1][2] != 5:
            count += 1
        if self.tiles[2][0] != 6:
            count += 1
        if self.tiles[2][1] != 7:
            count += 1
        if self.tiles[2][2] != 8:
            count += 1
        return count

    # Number 7
    def __eq__(self, other):
        """ Overloads the == operator. Returns True if the
            called object(self) and the argument(other) have
            the same values for the tiles attribute and
            False otherwise
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False

    # Number 4a of Task V: H2 heuristic
    def turns_from_goal(self):
        """ Counts the amount of steps or turns each
            number/tile is from their respective goal state
            and position. Adds together each tile's steps 
            and gets the total number of turns from the goal
            state
        """
        count = 0
        if self.tiles[0][1] != 1:
            if self.tiles[0][0] == 1 or self.tiles[0][2] == 1 \
               or self.tiles[1][1] == 1:
                count += 1
            elif self.tiles[1][0] == 1 or self.tiles[1][2] == 1 \
                 or self.tiles[2][1] == 1:
                count += 2
            else:
                count += 3
        if self.tiles[0][2] != 2:
            if self.tiles[0][1] == 2 or self.tiles[1][2] == 2:
                count += 1
            elif self.tiles[0][0] == 2 or self.tiles[1][1] == 2 \
                 or self.tiles[2][2] == 2:
                count += 2
            elif self.tiles[1][0] == 2 or self.tiles[2][1] == 2:
                count += 3
            else:
                count += 4
        if self.tiles[1][0] != 3:
            if self.tiles[0][0] == 3 or self.tiles[1][1] == 3 \
               or self.tiles[2][0] == 3:
                count += 1
            elif self.tiles[0][1] == 3 or self.tiles[1][2] == 3 \
               or self.tiles[2][1] == 3:
                count += 2
            else:
                count += 3
        if self.tiles[1][1] != 4:
            if self.tiles[0][1] == 4 or self.tiles[1][0] == 4 \
               or self.tiles[1][2] == 4 or self.tiles[2][1] == 4:
                count += 1
            elif self.tiles[0][0] == 4 or self.tiles[0][2] == 4 \
                 or self.tiles[2][0] == 4 or self.tiles[2][2] == 4:
                count += 2
        if self.tiles[1][2] != 5:
            if self.tiles[0][2] == 5 or self.tiles[1][1] == 5 \
               or self.tiles[2][2] == 5:
                count += 1
            elif self.tiles[0][1] == 5 or self.tiles[1][0] == 5 \
               or self.tiles[2][1] == 5:
                count += 2
            else:
                count += 3
        if self.tiles[2][0] != 6:
            if self.tiles[1][0] == 6 or self.tiles[2][1] == 6:
                count += 1
            elif self.tiles[0][0] == 6 or self.tiles[1][1] == 6 \
                 or self.tiles[2][2] == 6:
                count += 2
            elif self.tiles[0][1] == 6 or self.tiles[1][2] == 6:
                count += 3
            else:
                count += 4
        if self.tiles[2][1] != 7:
            if self.tiles[1][1] == 7 or self.tiles[2][0] == 7 \
               or self.tiles[2][2] == 7:
                count += 1
            elif self.tiles[0][1] == 7 or self.tiles[1][0] == 7 \
                 or self.tiles[1][2] == 7:
                count += 2
            else:
                count += 3
        if self.tiles[2][2] != 8:
            if self.tiles[1][2] == 8 or self.tiles[2][1] == 8:
                count += 1
            elif self.tiles[0][2] == 8 or self.tiles[1][1] == 8 \
                 or self.tiles[2][0] == 8:
                count += 2
            elif self.tiles[0][1] == 8 or self.tiles[1][0] == 8:
                count += 3
            else:
                count += 4
        return count
