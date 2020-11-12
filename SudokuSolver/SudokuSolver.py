import sys
import math

def gridUnfinished(grid):
    for column in grid:
        for num in column:
            if num == 0:
                return True
    return False

def printGrid(grid):
    rows = []
    for i in range(9):
        rows.append("")

    for column in grid:
        for num in range(len(column)):
            rows[num] += str(column[num])

    for row in rows:
        print(row)    


if len(sys.argv) < 2:
    print("Format for command is: \"python SudokuSolver.py [filename]\"")
    sys.exit(1)

if sys.argv[1][-4:] != ".txt":
    print("File provided is not a .txt file")
    sys.exit(1)

f = open(sys.argv[1])
grid = []

# Set up the grid itself
for i in range(9):
    grid.append([])

# Load in the sudoku
for row in range(9):
    linestring = f.readline()
    for column in range(9):
        if linestring[column].isdigit():
            grid[column].append(int(linestring[column]))
        else:
            grid[column].append(0)

# Our main loop which continues as long as we need to
while gridUnfinished(grid):
    # Make a copy of the grid before we begin so we know if we get stuck
    beginGrid = grid.copy()
    c = -1
    # Go through the entire grid
    for column in grid:
        c += 1
        r = -1
        for row in column:
            r += 1
            # Is the number set yet?
            if row != 0:
                continue
            
            # Make our options list
            options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            # Remove any option which is in the same column already
            for num in column:
                if num in options:
                    options.remove(num)
            
            # Remove any option which is in the same row already
            for col in grid:
                if num in options:
                    options.remove(col[r])
            
            # Remove any options which is in the same square
            for col in grid[math.floor(c/3)*3:math.floor(c/3)*3+2]:
                for num in col[math.floor(r/3)*3:math.floor(r/3)*3+2]:
                    if num in options:
                        options.remove(num)

            

            #TODO: MAKE THIS MORE PRO-ACTIVE. IF THERE'S A 1 ON THE LEFT AND A 1 ON THE RIGHT WE NEED TO HAVE A 1
            
            # Somehow there's no available number, indicating we messed up
            if len(options) < 1:
                print("There is no available value for tile at column: {} row: {}!".format(c, r))
                printGrid(grid)
                sys.exit(2)

            # We can't determine which digit to use
            elif len(options) > 1:
                continue

            # We determined which digit to use
            else:
                column[r] = options[0]

    # Nothing changed in this cycle (and this programme is deterministic, so it won'te ver)
    if grid == beginGrid:
        print("Sudoku is not solveable!")
        printGrid(grid)
        sys.exit(2)

# We finished the sudoku!
print("Sudoku Finished:")
printGrid(grid)

f.close()