from hashlib import md5

def solution(input: str):
  hash = ''
  index = 0
  while (hash[0:5] != '00000'):
    index += 1
    hash = md5(bytes(input + str(index), 'UTF8')).hexdigest()
  return index
