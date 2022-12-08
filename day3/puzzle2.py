from day3.helpers import move, visit

def solution(input: str):
  x, y, xr, yr = 0, 0, 0, 0
  visited = [[0, 0]]
  robotTurn = False
  for instruction in input:
    if (robotTurn):
      robotTurn = False
      xr, yr = move(instruction, xr, yr)
      visit(xr, yr, visited)
    else:
      robotTurn = True
      x, y = move(instruction, x, y)
      visit(x, y, visited)
  return len(visited)
