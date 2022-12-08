def move(instruction, x, y):
  if (instruction == '<'): x -= 1
  elif (instruction == '>'): x += 1
  elif (instruction == '^'): y -= 1
  elif (instruction == 'v'): y += 1
  return x, y

def visit(x, y, visited):
    if [x, y] not in visited:
      visited.append([x, y])