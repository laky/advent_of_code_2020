from collections import namedtuple

Execution = namedtuple('Execution', 'acc executed_instructions instruction_pointer flipped')

def parse_line(line):
  command, number = line.split(" ")
  return command, int(number)
  
def execute_instruction(pointer, acc, instruction):
  if instruction[0] == "nop":
    return pointer+1, acc
  if instruction[0] == "acc":
    return pointer+1, acc+instruction[1]
  if instruction[0] == "jmp":
    return pointer+instruction[1], acc
    
def execute_instructions(instructions):
  acc = 0
  executed_instructions = set()
  instruction_pointer = 0
  while instruction_pointer not in executed_instructions and instruction_pointer < len(instructions):
    executed_instructions.add(instruction_pointer)
    instruction_pointer, acc = execute_instruction(instruction_pointer, acc, instructions[instruction_pointer])
  return acc, instruction_pointer == len(instructions)
  
def get_next_executions(execution, instructions):
  instruction_to_execute = instructions[execution.instruction_pointer]
  new_executed_instructions = execution.executed_instructions.union(set([execution.instruction_pointer]))
  if not execution.flipped and (instruction_to_execute[0] == "jmp" or instruction_to_execute[0] == "nop"):
    next_pointer_1, next_acc_1 = execute_instruction(execution.instruction_pointer, execution.acc, ("jmp", instruction_to_execute[1]))
    next_pointer_2, next_acc_2 = execute_instruction(execution.instruction_pointer, execution.acc, ("nop", instruction_to_execute[1]))
    return [
      Execution(next_acc_1, new_executed_instructions, next_pointer_1, instruction_to_execute[0] != "jmp"),
      Execution(next_acc_2, new_executed_instructions, next_pointer_2, instruction_to_execute[0] != "nop")
    ]
  else:
    next_pointer, next_acc = execute_instruction(execution.instruction_pointer, execution.acc, instruction_to_execute)
    return [Execution(next_acc, new_executed_instructions, next_pointer, execution.flipped)]

def fix_and_execute_instructions(instructions):
  executions_to_check = [Execution(0, set(), 0, False)]
  while True:
    execution = executions_to_check.pop()
    
    if execution.instruction_pointer == len(instructions):
      return execution.acc
    
    if execution.instruction_pointer in execution.executed_instructions:
      continue
          
    executions_to_check.extend(get_next_executions(execution, instructions))

with open("input_8.txt", "r") as f:
  instructions = [parse_line(line) for line in f]
  print(len(instructions))
  
  print("Part 1:", execute_instructions(instructions))
  print("Part 2:", fix_and_execute_instructions(instructions))
