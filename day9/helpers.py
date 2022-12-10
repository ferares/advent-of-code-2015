def parseData(input: str):
  lines = input.split('\n')
  nodes = []
  edges = []
  for line in lines:
    [cities, distance] = line.split(' = ')
    [city1, city2] = cities.split(' to ')
    if city1 not in nodes: nodes.append(city1)
    if city2 not in nodes: nodes.append(city2)
    edges.append((city1, city2, int(distance)))
  return nodes, edges