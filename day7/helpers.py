from typing import List

# cable = {
#   'command': '',
#   'operand/s': '' | ['', ''],
# }

def getValueOn(cableName: str, circuit: dict[str, dict]):
  value = None
  if (cableName.isnumeric()): return int(cableName)
  cable = circuit[cableName]
  if ('value' in cable):
    value = cable['value']
  elif ('command' in cable):
    if (cable['command'] == 'NOT'):
      value = ~ getValueOn(cable['operand'], circuit) & 0xffff
    else:
      value1 = getValueOn(cable['operands'][0], circuit)
      value2 = getValueOn(cable['operands'][1], circuit)
      if (cable['command'] == 'AND'):
        value = value1 & value2
      elif (cable['command'] == 'OR'):
        value = value1 | value2
      elif (cable['command'] == 'LSHIFT'):
        value = value1 << value2
      elif (cable['command'] == 'RSHIFT'):
        value = value1 >> value2
  else:
    value = getValueOn(cable['operand'], circuit)

  circuit[cableName]['value'] = value
  return value

def parseInput(input: str):
  lines = input.split('\n')
  circuit = {}
  for line in lines:
    [instruction, cableName] = line.split(' -> ')
    cable = {}
    instructionParts = instruction.split(' ')
    if len(instructionParts) == 2: # NOT command
      [command, operand] = instructionParts
      cable['command'] = command
      cable['operand'] = operand
    elif len(instructionParts) == 3: # Any other command
      [operand1, command, operand2] = instructionParts
      cable['command'] = command
      cable['operands'] = [operand1, operand2]
    else: # Direct value assignment
      [operand] = instructionParts
      cable['operand'] = operand
    circuit[cableName] = cable
  return circuit