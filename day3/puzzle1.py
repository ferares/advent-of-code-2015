from day3.helpers import move, visit

def solution(input: str):
  x, y = 0, 0
  visited = [[0, 0]]
  for instruction in input:
    x, y = move(instruction, x, y)
    visit(x, y, visited)
  return len(visited)
