import sys, os, shutil, importlib

def readInput(day):
  return open('./input/' + day + '.txt', 'r').read()

args = sys.argv[1:]

if (len(args) == 1):
  day = args[0]
  os.mkdir('./day' + day)
  shutil.copyfile('./template.py', './day' + day + '/puzzle1.py')
  shutil.copyfile('./template.py', './day' + day + '/puzzle2.py')
elif (len(args) == 2):
  day = args[0]
  puzzle = args[1]
  input = readInput(day)
  puzzle = importlib.import_module('day' + day + '.puzzle' + puzzle)
  print(puzzle.solution(input))