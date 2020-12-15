def execute_instruction(instruction, mask, mem):
  command = instruction.split(" = ")[0]
  value = instruction.split(" = ")[1]
  
  if command == "mask":
    return value, mem

  else:  
    mask_or = int(mask.replace("X", "0"), 2)
    mask_and = int(mask.replace("X", "1"), 2)
    
    key = int(command[4:-1])
    mem[key] = int(value) & mask_and | mask_or
    return mask, mem
    
def overwrite_indices(indices, string_1, string_2):
  result = list(string_1)
  counter = 0
  for index in indices:
    result[index] = string_2[counter]
    counter += 1
  return "".join(result)

def execute_instruction_2(instruction, mask, mem):
  command = instruction.split(" = ")[0]
  value = instruction.split(" = ")[1]
  
  if command == "mask":
    return value, mem

  else:
    key = int(command[4:-1])
    x_indices = [i for i, c in enumerate(mask) if c == "X"]
    one_indices = [i for i, c in enumerate(mask) if c != "X" and c != "0"]
    starting_key = format(key, '036b')
    starting_key = overwrite_indices(one_indices, starting_key, mask.replace("X", "").replace("0", ""))
    for i in range(2 ** len(x_indices)):
      key_to_write = starting_key
      i_binary = format(i, '0{0}b'.format(len(x_indices)))
      key_to_write = overwrite_indices(x_indices, key_to_write, i_binary)
      mem[key_to_write] = int(value)
    return mask, mem

with open("input_14.txt", "r") as f:
  instructions = [line.strip() for line in f]
  print(instructions)

  mask = "X" * 36
  mem = dict()
  for instruction in instructions:
    mask, mem = execute_instruction(instruction, mask, mem)
  
  print("Part 1: ", sum(mem.values()))
  
  mask = "X" * 36
  mem = dict()
  for instruction in instructions:
    mask, mem = execute_instruction_2(instruction, mask, mem)
  
  print("Part 2: ", sum(mem.values()))
    
