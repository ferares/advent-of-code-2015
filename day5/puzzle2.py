def solution(input: str):
  words = input.split('\n')
  niceWords = 0
  for word in words:
    substrings = []
    repeated = False
    hasPair = False
    previousSubstring = ''
    for index in range(len(word)):
      char = word[index]
      if (index > 0):
        substring = word[index - 1:index + 1]
        if (substring in substrings): hasPair = True
        elif (previousSubstring): substrings.append(previousSubstring)
        previousSubstring = substring
        if (index > 1):
          if (char == word[index - 2]): repeated = True
    if repeated and hasPair:
      niceWords += 1
  return niceWords
