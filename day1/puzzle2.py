def solution(input: str):
  floor = 0
  for index in range(len(input)):
    char = input[index]
    if (char == '('): floor += 1
    else: floor -= 1
    if (floor == -1): break
  return index + 1
