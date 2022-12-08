import re

def getMemoryLength(line: str):
  line = line[1:-1]
  regex = r"\\\"|\\\\|\\x[a-f0-9]{2}"
  line = re.sub(regex, ' ', line)
  return len(line)

def solution(input: str):
  lines = input.split('\n')
  total = 0
  for line in lines:
    codeLength = len(line)
    memoryLength = getMemoryLength(line)
    total += codeLength - memoryLength
  return total
