def solution(input):
  presents = input.split('\n')
  totalRibbon = 0
  for present in presents:
    dimensions = list(map(int, present.split('x')))
    dimensions.sort()
    totalRibbon += dimensions[0] + dimensions[0] + dimensions[1] + dimensions[1]
    totalRibbon += dimensions[0] * dimensions[1] * dimensions[2]
  return totalRibbon
