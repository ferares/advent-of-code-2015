from day7.helpers import parseInput, getValueOn

def solution(input: str):
  circuit = parseInput(input)
  # Get value on cable a
  aValue = getValueOn('a', circuit)
  # Override b with value on a
  circuit['b'] = { 'operand': str(aValue) }
  # Reset the circuit
  for cableName in circuit:
    circuit[cableName].pop('value', None)
  # Get new a value
  return getValueOn('a', circuit)
