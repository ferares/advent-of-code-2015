def isForbiddenLetter(letter: str):
  return (letter == 'i') or (letter == 'o') or (letter == 'l')

def incrementLetter(letter: str):
  newLetter = letter
  forbidden = True
  overflow = False
  while (forbidden):
    newLetter = chr(ord(newLetter) + 1)
    if (newLetter > 'z'):
      newLetter = 'a'
      overflow = True
    forbidden = isForbiddenLetter(newLetter)
  return (newLetter, overflow)

def validPassword(password: str):
  if (len(password) != 8): return False
  increasing = False
  previousCharCode = None
  increasingChainLength = 0
  pairs = (None, None)
  for char in password:
    # Check for forbidden letters
    if isForbiddenLetter(char): return False
    charCode = ord(char)
    # Check for non lowercase letters
    if (charCode > ord('z')) or (charCode < ord('a')): return False
    if (previousCharCode):
      # Check for increasing chain of letters of length 3
      if (charCode == previousCharCode + 1):
        increasingChainLength += 1
        if (increasingChainLength >= 2): increasing = True
      else:
        increasingChainLength = 0
        # Check for double letters
        if (charCode == previousCharCode):
          if (pairs[0] == None): pairs = (charCode, None)
          elif (pairs[0] != charCode): pairs = (pairs[0], charCode)
    previousCharCode = charCode
  return increasing and pairs[0] != None and pairs[1] != None

def incrementPassword(password: str):
  newPassword = password
  valid = False
  while (not valid):
    index = len(newPassword)
    overflow = True
    while (overflow):
      index -= 1
      (newLetter, overflow) = incrementLetter(newPassword[index])
      newPassword = newPassword[:index] + newLetter + newPassword[index + 1:]
    valid = validPassword(newPassword)
  return newPassword