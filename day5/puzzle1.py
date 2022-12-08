def solution(input: str):
  words = input.split('\n')
  badCombos = ['ab', 'cd', 'pq', 'xy']
  vowels = ['a', 'e', 'i', 'o', 'u']
  niceWords = 0
  for word in words:
    vowelCount = 0
    repeated = False
    hasBadCombos = False
    lastChar = ''
    for char in word:
      if (char in vowels): vowelCount += 1
      if (char == lastChar): repeated = True
      if (lastChar + char in badCombos): hasBadCombos = True
      lastChar = char
    if vowelCount > 2 and repeated and not hasBadCombos:
      niceWords += 1
  return niceWords
