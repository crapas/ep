from numpy import zeros
from urllib.request import urlopen


grid = zeros(shape=(9, 9))

def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

def isValid(grid, i, j, n):
    if all([n != grid[i][x] for x in range(9)]):
        if all([n != grid[x][j] for x in range(9)]):
            X0, Y0 = 3 * (i // 3), 3 * (j // 3)
            for x in range(X0, X0 + 3):
                for y in range(Y0, Y0 + 3):
                    if grid[x][y] == n:
                        return False
            return True
    return False

def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True # If there is no next cell.
    for n in range(1, 10):
        if isValid(grid, i, j, n):
            grid[i][j] = n
            if solveSudoku(grid):
                return True # If Su Doku is solved.
            grid[i][j] = 0
    return False # This is were recursion happens.

file = urlopen("https://projecteuler.net/project/resources/p096_sudoku.txt")
count, result = 0, 0
cnt = 1
for line in file:
    line = line.decode('utf-8')
    if line[0] == 'G':
        print(cnt)
        cnt += 1
        if count != 0: # It doesn't allow for line "Grid 01" to calculate a grid.
            count = 0 # It resets every time a grid is calculated.
            solveSudoku(grid)
            result += 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]
    else:
        for i in range(9):
            grid[count][i] = int(line[i]) # In order to solve the grid, it must contain integers and not characters.
        count += 1
        if line == "000008006": # The last line of the file.
            solveSudoku(grid)
            result += 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]
            break
file.close()
print(result)

