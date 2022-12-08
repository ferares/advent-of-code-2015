from day6.helpers import parseInput

def initGrid(width: int = 1000, height: int = 1000):
  return [[False for _ in range(width)] for _ in range(height)]

def solution(input: str):
  instructions = parseInput(input)
  grid = initGrid()
  lit = 0
  for instruction in instructions:
    [command, startRow, startColumn, endRow, endColumn] = instruction
    for rowIndex in range(int(startRow), int(endRow) + 1):
      row = grid[rowIndex]
      for columnIndex in range(int(startColumn), int(endColumn) + 1):
        currentState = row[columnIndex]
        if (command == 'turn on'): row[columnIndex] = True
        elif (command == 'turn off'): row[columnIndex] = False
        else: row[columnIndex] = not row[columnIndex]
        if (currentState != row[columnIndex]):
          if (currentState): lit -= 1
          else: lit += 1
        
  return lit
