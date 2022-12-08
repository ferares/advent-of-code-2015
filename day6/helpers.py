from re import findall

def parseInput(input: str):
  regex = r'(.*) (\d+),(\d+) through (\d+),(\d+)'
  return findall(regex, input)
