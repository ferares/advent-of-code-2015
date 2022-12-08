def solution(input: str):
  presents = input.split('\n')
  totalWrap = 0
  for present in presents:
    dimensions = list(map(int, present.split('x')))
    dimensions.sort()
    totalWrap += dimensions[0] * dimensions[1]
    totalWrap += 2 * dimensions[0] * dimensions[1]
    totalWrap += 2 * dimensions[0] * dimensions[2]
    totalWrap += 2 * dimensions[1] * dimensions[2]
  return totalWrap
