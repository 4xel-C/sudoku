#sudoku resolver
grid =   [[6, 8, 0, 0, 0, 0, 0, 1, 7],
          [0, 0, 4, 0, 0, 2, 0, 0, 0],
          [0, 0, 0, 0, 7, 0, 6, 5, 0],
          [0, 0, 0, 4, 3, 0, 0, 0, 8],
          [3, 9, 8, 7, 2, 0, 4, 6, 0],
          [0, 6, 7, 5, 9, 0, 1, 2, 3],
          [5, 3, 0, 0, 0, 7, 2, 0, 0],
          [0, 0, 0, 0, 6, 0, 0, 0, 1],
          [0, 4, 6, 0, 8, 2, 0, 0, 0],]

def display(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0 :
            print("-----------------------")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" |", end=" ")
            if j == len(grid)-1:
                print(grid[i][j])
            else:
                print(grid[i][j], end=" ")

display(grid)

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0 :
                return (i, j)
       

def is_valid(grid, num, pos):
    #check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and i != pos[0]:
            return False
        
    #check row
    for j in range(len(grid[0])):
        if grid[pos[0]][j] == num and j != pos[1]:
            return False

    #check square
    box_i = pos[0] // 3
    box_j = pos[1] // 3 

    for i in range(box_i*3, box_i*3+3):
        for j in range(box_j*3, box_j*3+3):
            if grid[i][j] == num and (i, j) != pos:
                return False
            
    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find
    for num in range(len(grid)+1):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve(grid):
                return True
            

    return False

solve(grid)
print("###############")
display(grid)



