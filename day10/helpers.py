def play(input: str, iterations: int):
  newInput = input
  for _ in range(iterations):
    repeats = 1
    lastDigit = ''
    currentInput = newInput
    newInput = ''
    for digit in currentInput:
      if (lastDigit):
        if (lastDigit == digit): repeats += 1
        else:
          newInput += str(repeats) + lastDigit
          lastDigit = digit
          repeats = 1
      else: lastDigit = digit
    newInput += str(repeats) + lastDigit
  return newInput