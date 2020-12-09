from advent_of_code_2020_01 import find_numbers_summing_to

def find_non_sum(numbers):
  window = numbers[:25]
  for n in numbers[25:]:
    sorted_window = window.copy()
    sorted_window.sort()
    if find_numbers_summing_to(sorted_window, n) == None:
      return n
    window.pop(0)
    window.append(n)

def find_contiguous_sum(sum, numbers):
  window_sum = 0
  start_index = 0
  for i, n in enumerate(numbers):
    if window_sum == sum:
      return numbers[start_index:i]
    
    window_sum += n      
    while window_sum > sum:  
      window_sum -= numbers[start_index]
      start_index += 1 
  
    

with open("input_9.txt", "r") as f:
  input_numbers = [int(line) for line in f]
  print(len(input_numbers))
  
  outlier_number = find_non_sum(input_numbers)
  print("Part 1:", outlier_number)
  
  subsum = find_contiguous_sum(outlier_number, input_numbers)
  print("Part 2:", min(subsum) + max(subsum))
