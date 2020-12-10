def get_stats(sorted_input_array):
  stats = {}
  previous = 0
  for n in sorted_input_array:
    diff = n - previous
    previous = n
    if diff in stats:
      stats[diff] += 1
    else:
      stats[diff] = 1
  return stats

def count_all_arrangements(sorted_input_array):
  counter = {0: 1}
  for i, n in enumerate(sorted_input_array):
    options = 0
    for j in range(1, 4):
      if n-j in counter:
        options += counter[n-j]
    counter[n] = options
  return options

with open("input_10.txt", "r") as f:
  input_array = [int(line.strip()) for line in f]
  
  input_array.sort()
  stats = get_stats(input_array)
  print("Part 1:", stats[1] * (stats[3] + 1))
  
  print("Part 2:", count_all_arrangements(input_array))
  
