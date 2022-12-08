import re

def getNewLength(line: str):
  length = len(line)
  for char in line:
    if (char == '"') or (char == '\\'): length += 1
  return length + 2

def solution(input: str):
  lines = input.split('\n')
  total = 0
  for line in lines:
    codeLength = len(line)
    newLength = getNewLength(line)
    total += newLength - codeLength
  return total
