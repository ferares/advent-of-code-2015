from day11.helpers import incrementPassword

def solution(input: str):
  return incrementPassword(incrementPassword(input))
