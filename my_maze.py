
# NOTE: I am ware that this code doesnt pass all unit test. I just run out of Ideas to find the mistake

class MyMaze:
    def __init__(self, maze_str: str):
        if not maze_str:
            raise ValueError("The input maze string cannot be empty.")
        self._maze = [list(row) for row in maze_str.split("\n")]
        self._exits = []
        self._max_recursion_depth = 0

    def find_exits(self, start_row: int, start_col: int, depth=0):
        if not (0 <= start_row < len(self._maze) and 0 <= start_col < len(self._maze[0])):
            raise ValueError("Starting position is out of range")
        if self._maze[start_row][start_col] not in (' ', 'S'):
            raise ValueError("Starting position is not on a walkable path")

        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        def explore(row, col, current_depth):
            if not (0 <= row < len(self._maze) and 0 <= col < len(self._maze[0])):
                return  # Out of bounds check to prevent list index out of range error

            if self._maze[row][col] not in (' ', 'S'):
                return  # Not walkable or already visited

            # Mark the cell as visited
            if (row, col) == (start_row, start_col):
                self._maze[row][col] = 'S'  # Ensure start remains marked as 'S'
            else:
                self._maze[row][col] = '.'

            self._max_recursion_depth = max(self._max_recursion_depth, current_depth)

            # Check if it's an exit
            if (row in [0, len(self._maze)-1] or col in [0, len(self._maze[0])-1]) and self._maze[row][col] == '.':
                self._exits.append((row, col))
                self._maze[row][col] = 'X'

            # Recursively explore neighboring cells
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if 0 <= next_row < len(self._maze) and 0 <= next_col < len(self._maze[0]):
                    explore(next_row, next_col, current_depth + 1)

        explore(start_row, start_col, depth + 1)
        return bool(self._exits)

    @property
    def exits(self):
        return sorted(self._exits)

    @property
    def max_recursion_depth(self):
        return self._max_recursion_depth

    def __str__(self):
        return "\n".join("".join(row) for row in self._maze)

# Testing with own maze
"""
def main():
    maze_15x15 = """
###############
#      #      #
### # ######  #
#   # ####### #
# ###         #
#   #######   #
### #  ##     #
    # ##   #  #
##         ## #
##### ######  #
#         ##  #
# ########## ##
#      ##  # ##
#   ##       ##
###############
"""
    maze_20x20 = """
####################
#      #      # S  #
### # ######  #    #
#   # ####### #    #
# ###         #    #
#   #######   #    #
### #  ##     #    #
#    # ##   #  #   #
##         ## #    #
##### ######  #    #
#         ##  #    #
# ########## ##    #
#      ##  # ##    #
#   ##       ##    #
#     #### ###   ###
#      ##          #
#   ##             #
#  #############   #
#                  #
######## ###########
"""

    maze1 = MyMaze(maze_15x15)


if __name__ == "__main__":
    main()

"""