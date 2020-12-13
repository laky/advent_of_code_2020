def read_bus_schedule(f):
  lines = [line.strip() for line in f]
  timestamp = int(lines[0])
  all_bus_numbers = [int(n) if n != "x" else 1 for n in lines[1].split(",")]
  present_bus_numbers = [int(n) for n in all_bus_numbers if n != 1]
  return timestamp, present_bus_numbers, all_bus_numbers
  
def find_next_bus(timestamp, bus_numbers):
  earliest_time = float("inf")
  earliest_bus = None
  for n in present_bus_numbers:
    if timestamp % n == 0:
      earliest_time = 0
      earliest_bus = n
    next_bus = ((timestamp // n) + 1) * n
    if next_bus < earliest_time:
      earliest_time = next_bus
      earliest_bus = n
  return earliest_time, earliest_bus
  
def find_max_bus(bus_numbers):
  max = 0
  max_index = None
  for i, n in enumerate(bus_numbers):
    if n > max:
      max = n
      max_index = i
  return max, max_index
    
def check_timestamp(timestamp, bus_numbers):
  for i, n in enumerate(bus_numbers):
    if (timestamp + i) % n != 0:
      return False
  return True
    
def find_timestamp_for_buses(bus_numbers):
  print(bus_numbers)
  bus_numbers_copy = bus_numbers.copy()
  for i, n in enumerate(bus_numbers):
    for j in range(i+n, len(bus_numbers), n):
      bus_numbers_copy[j] *= n
  print(bus_numbers_copy)
    
  max_bus, max_bus_index = find_max_bus(bus_numbers_copy)
  
  timestamp = max_bus - max_bus_index
  counter = 0
  while not check_timestamp(timestamp, bus_numbers):
    timestamp += max_bus
    counter += 1
    if counter % 10000000 == 0:
      print(timestamp)
      print(100000000000000)
  return timestamp

with open("input_13.txt", "r") as f:
  test_1 = ["939", "7,13,x,x,59,x,31,19"] # 1068781
  test_2 = ["3417", "17,x,13,19"]
  test_3 = ["754018", "67,7,59,61"]
  test_4 = ["779210", "67,x,7,59,61"]
  test_5 = ["1261476", "67,7,x,59,61"]
  test_6 = ["1202161486", "1789,37,47,1889"]
  
  timestamp, present_bus_numbers, all_bus_numbers = read_bus_schedule(f)
  
  earliest_time, earliest_bus = find_next_bus(timestamp, present_bus_numbers)
  print("Part 1:", earliest_bus * (earliest_time - timestamp))
  print("Part 2:", find_timestamp_for_buses(all_bus_numbers))

