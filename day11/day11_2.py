import time
from copy import deepcopy

def processGrid(grid):
   newGrid = deepcopy(grid)
   for i in range(len(grid)):
      for j in range(len(grid[0])):
         lowI = max(0,i-1)
         highI = min(len(grid),i+2)
         lowJ = max(0,j-1)
         highJ = min(len(grid[0]),j+2)
         occupied = 0
         #print(i,j,lowI, highI, list(range(lowI, highI)), lowJ, highJ, list(range(lowJ,highJ)))
         if grid[i][j] == "L" or grid[i][j] == '#':
            for ii in range(lowI, highI):
               for jj in range(lowJ, highJ):
                     #print("--",i,j,ii,jj,grid[ii][jj])
                     if grid[ii][jj] == '#' and (ii != i or jj != j):
                        occupied += 1
            #print(i,j,occupied)
            if occupied == 0 and grid[i][j] == "L":
                     newGrid[i][j] = '#'
            elif occupied >= 4 and grid[i][j] == '#':
                     newGrid[i][j] = 'L'
   return newGrid

def processGridSightlines(grid):
   newGrid = deepcopy(grid)
   directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
   for i in range(len(grid)):
      for j in range(len(grid[0])):
         if grid[i][j] == "L" or grid[i][j] == '#':
            occupied = 0
            for direction in directions:
               n = 1
               ii = n*direction[0] + i
               jj = n*direction[1] + j
               #print(i,j,n,ii,jj,direction)
               while (ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid[0])) :
                  if grid[ii][jj] == '#':
                     occupied += 1
                     break
                  elif grid[ii][jj] == 'L':
                     break
                  elif grid[ii][jj] != '.':
                     print("Unexpected Character: ", grid[ii][jj])
                  n += 1
                  ii = n*direction[0] + i
                  jj = n*direction[1] + j

            #print(i,j,occupied)
            if occupied == 0 and grid[i][j] == "L":
                     newGrid[i][j] = '#'
            elif occupied >= 5 and grid[i][j] == '#':
                     newGrid[i][j] = 'L'
   return newGrid

def printGrid(grid):
   for row in grid:
      rowStr = ""
      for character in row:
         rowStr += character
      print(rowStr)
   print()
         
def compareGrids(grid1, grid2):
   for i in range(len(grid1)):
      for j in range(len(grid1[0])):
         if grid1[i][j] != grid2[i][j]:
            return False
   return True

start = time.perf_counter()
with open("input.txt") as file:
   source = file.readlines()

grid = []
for line in source:
   row = []
   for character in line.strip():
      row.append(character)
   grid.append(row)

#printGrid(grid)
newGrid = processGridSightlines(grid)
cycles = 1
while compareGrids(grid, newGrid) == False:
   #printGrid(newGrid)
   cycles += 1
   grid = newGrid
   newGrid = processGridSightlines(grid)
      
occupied = 0
for row in newGrid:
   for seat in row:
      if seat == '#':
         occupied += 1

print("OCCUPIED: ", occupied, "CYCLES: ", cycles)
stop = time.perf_counter()
print("TIME: ", stop-start)



