from day6.helpers import parseInput

def initGrid(width: int = 1000, height: int = 1000):
  return [[0 for _ in range(width)] for _ in range(height)]

def solution(input: str):
  instructions = parseInput(input)
  grid = initGrid()
  brightness = 0
  for instruction in instructions:
    [command, startRow, startColumn, endRow, endColumn] = instruction
    for rowIndex in range(int(startRow), int(endRow) + 1):
      row = grid[rowIndex]
      for columnIndex in range(int(startColumn), int(endColumn) + 1):
        currentState = row[columnIndex]
        if (command == 'turn on'): row[columnIndex] += 1
        elif (command == 'turn off') and (currentState > 0): row[columnIndex] -= 1
        elif (command == 'toggle'): row[columnIndex] += 2
        brightness += row[columnIndex] - currentState
  return brightness
