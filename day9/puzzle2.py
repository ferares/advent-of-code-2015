from day9.helpers import parseData

def travel(edges: list[tuple], start: str, visited: list[str], distance: float):
  maxDistance = 0
  for edge in edges:
    next = None
    if (edge[0] == start and edge[1] not in visited): next = edge[1]
    elif (edge[1] == start and edge[0] not in visited): next = edge[0]
    if (next != None):
      nextVisited = visited.copy()
      nextVisited.append(next)
      travelDistnace = travel(edges, next, nextVisited, distance + edge[2])
      if (travelDistnace > maxDistance): maxDistance = travelDistnace
  if (maxDistance == 0): return distance
  return maxDistance

def solution(input: str):
  nodes, edges = parseData(input)
  maxDistance = 0
  for node in nodes:
    travelDistnace = travel(edges, node, [node], 0)
    if (travelDistnace > maxDistance): maxDistance = travelDistnace
  return maxDistance
