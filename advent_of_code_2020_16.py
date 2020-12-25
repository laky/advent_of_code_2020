def read_rules(lines):
  rules = dict()
  for line in lines:
    name = line.split(": ")[0]
    intervals = line.split(": ")[1]
    interval_1 = intervals.split(" or ")[0]
    interval_2 = intervals.split(" or ")[1]
    rules[name] = [
        (int(interval_1.split("-")[0]), int(interval_1.split("-")[1])),
        (int(interval_2.split("-")[0]), int(interval_2.split("-")[1])),
      ]    
  return rules

def read_tickets(lines):
  result = []
  for line in lines:
    numbers = [int(n) for n in line.split(",")]
    result.append(numbers)
  return result
  
def is_condition_valid(number, intervals):
  return any([number >= interval[0] and number <= interval[1] for interval in intervals])
  
def validate_ticket_1(ticket, rules):
  invalid_numbers = []
  for number in ticket:
     # Check the intervalsp
    condition_applies = []
    for intervals in rules.values():
      condition_applies.append(
        is_condition_valid(number, intervals)
      )
    if not any(condition_applies):
      invalid_numbers.append(number)
    if not any(condition_applies):
      invalid_numbers.append(number)
  return invalid_numbers
  
def match_rules(valid_tickets, rules):
  rules_to_indices = dict()
  
  valid_tickets_columns = [[valid_tickets[t][c] for t in range(len(valid_tickets))] for c in range(len(valid_tickets[0]))]
  
  for name, intervals in rules.items():
    rules_to_indices[name] = []
    for i, column in enumerate(valid_tickets_columns):
      if all([is_condition_valid(n, intervals) for n in column]):
        rules_to_indices[name].append(i)
  return rules_to_indices

def assign(rules_to_indices, rules_to_unique_index):
  names_to_delete = []
  for name, indices in rules_to_indices.items():
    if len(indices) == 1:
      rules_to_unique_index[name] = indices[0]
      names_to_delete.append(name)
  for name in names_to_delete:
    del rules_to_indices[name]
  return rules_to_indices, rules_to_unique_index

def remove(rules_to_indices, rules_to_unique_index):
  for _, index in rules_to_unique_index.items():
    for name, indices in rules_to_indices.items():
      try: 
        indices.remove(index)
      except:
        1+1
  return rules_to_indices, rules_to_unique_index
             

with open("input_16.txt", "r") as f:
  lines = [line.strip() for line in f]
  rules_end = lines.index("your ticket:") - 1
  my_ticket_line = lines.index("your ticket:") + 1
  other_tickets_lines_start = lines.index("nearby tickets:") + 1
  
  rules = read_rules(lines[:rules_end])
  my_ticket = read_tickets(lines[my_ticket_line:my_ticket_line+1])[0]
  other_tickets = read_tickets(lines[other_tickets_lines_start:])  
  
  invalid_numbers = [n for ticket in other_tickets for n in validate_ticket_1(ticket, rules)]
  print("Part 1:", sum(invalid_numbers))
  
  valid_tickets = []
  for ticket in other_tickets:
    if validate_ticket_1(ticket, rules) == []:
      valid_tickets.append(ticket)
  valid_tickets.append(my_ticket)
  
  rules_to_indices = match_rules(valid_tickets, rules)
  rules_to_unique_index = dict()

  # Assume we can always pick at least 1 rule that becomes unique.
  while len(rules_to_indices.keys()) > 0:
    rules_to_indices, rules_to_unique_index = assign(rules_to_indices, rules_to_unique_index)
    rules_to_indices, rules_to_unique_index = remove(rules_to_indices, rules_to_unique_index)
    
  print(rules_to_unique_index)
    
  result = 1
  for name, index in rules_to_unique_index.items():
    if "departure" in name:
      result *= my_ticket[index]
  print("Part 2:", result)
    
