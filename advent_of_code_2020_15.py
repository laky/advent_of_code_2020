input = [8,0,17,4,1,12]

def playout(start_sequence, end_at_step):
  numbers_used = dict()
  
  for i, n in enumerate(start_sequence):
    numbers_used[n] = i + 1
    
  step = len(start_sequence) + 1
  previous_number = start_sequence[-1]
  
  while step < end_at_step + 1:
    if previous_number not in numbers_used:
      numbers_used[previous_number], previous_number = step - 1, 0
    else:
      numbers_used[previous_number], previous_number = step - 1, step - 1 - numbers_used[previous_number]
    step += 1

  return previous_number
      
      
    
print("Part 1:", playout(input, 2020))
print("Part 2:", playout(input, 30000000))
