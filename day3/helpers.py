from typing import List

def move(instruction: str, x: int, y: int):
  if (instruction == '<'): x -= 1
  elif (instruction == '>'): x += 1
  elif (instruction == '^'): y -= 1
  elif (instruction == 'v'): y += 1
  return x, y

def visit(x: int, y: int, visited: List[List[int]]):
    if [x, y] not in visited:
      visited.append([x, y])