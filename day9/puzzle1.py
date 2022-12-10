from day9.helpers import parseData

def travel(edges: list[tuple], start: str, visited: list[str], distance: float):
  minDistance = float('inf')
  for edge in edges:
    next = None
    if (edge[0] == start and edge[1] not in visited): next = edge[1]
    elif (edge[1] == start and edge[0] not in visited): next = edge[0]
    if (next != None):
      nextVisited = visited.copy()
      nextVisited.append(next)
      travelDistnace = travel(edges, next, nextVisited, distance + edge[2])
      if (travelDistnace < minDistance): minDistance = travelDistnace
  if (minDistance == float('inf')): return distance
  return minDistance

def solution(input: str):
  nodes, edges = parseData(input)
  minDistance = float('inf')
  for node in nodes:
    travelDistnace = travel(edges, node, [node], 0)
    if (travelDistnace < minDistance): minDistance = travelDistnace
  return minDistance
