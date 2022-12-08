from day7.helpers import parseInput, getValueOn

def solution(input: str):
  circuit = parseInput(input)
  return getValueOn('a', circuit)
