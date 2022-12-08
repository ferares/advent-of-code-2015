def solution(input: str):
  floor = 0
  for char in input:
    if (char == '('): floor += 1
    else: floor -= 1
  return floor
