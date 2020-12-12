headings = [(1,0), (0, -1), (-1, 0), (0, 1)]

def follow_instruction(x, y, h, instruction):
  v = int(instruction[1:])
  
  if instruction[0] == "N":
    return x, y + v, h
  if instruction[0] == "E":
    return x + v, y, h
  if instruction[0] == "S":
    return x, y - v, h
  if instruction[0] == "W":
    return x - v, y, h
  
  if instruction[0] == "F":
    return x + v * headings[h][0], y + v * headings[h][1], h
  
  if instruction[0] == "R":
    if v % 90 != 0:
      print("o-oh", v)
    return x, y, (h + v // 90) % 4
  if instruction[0] == "L":
    if v % 90 != 0:
      print("o-oh", v)
    new_h = (h - v // 90)
    if new_h < 0:
      new_h += 4
    return x, y, new_h
  
def follow_instruction_2(x, y, w_x, w_y, instruction):
  v = int(instruction[1:])
  
  if instruction[0] == "N":
    return x, y, w_x, w_y + v
  if instruction[0] == "E":
    return x, y, w_x + v, w_y
  if instruction[0] == "S":
    return x, y, w_x, w_y - v
  if instruction[0] == "W":
    return x, y, w_x - v, w_y
  
  if instruction[0] == "F":
    return x + v * w_x, y + v * w_y, w_x, w_y
  
  if instruction[0] == "R":
    if v % 90 != 0:
      print("o-oh", v)
    for i in range(v // 90):
      w_x, w_y = w_y, -w_x
    return x, y, w_x, w_y
  if instruction[0] == "L":
    if v % 90 != 0:
      print("o-oh", v)
    for i in range(v // 90):
      w_x, w_y = -w_y, w_x
    return x, y, w_x, w_y

def follow_instructions(instructions, start_state, follow_instruction_method):
  state = start_state
  for instruction in instructions:
    state = follow_instruction_method(*state, instruction)
  return state

with open("input_12.txt", "r") as f:
  instructions = [line.strip() for line in f]
    
  x, y, _ = follow_instructions(instructions, (0, 0, 0), follow_instruction)
  print("Part 1:", abs(x) + abs(y))
  
  x, y, *_ = follow_instructions(instructions, (0, 0, 10, 1), follow_instruction_2)
  print("Part 2:", abs(x) + abs(y))

