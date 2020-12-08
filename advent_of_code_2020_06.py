def read_strings_separated_by_blank_lines(f):
  groups = []
  group = []
  for line in f:
    line = line.strip()
    if line == "":
      groups.append(group)
      group = []
    else:
      group.append(line)
  if group != []:
    groups.append(group)
  return groups

def count_different_letters(group):
  unique_letters = set()
  for string in group:
    letters_in_string = set([letter for letter in string])
    unique_letters = unique_letters.union(letters_in_string)
      
  return len(unique_letters)

def count_intersection_letters(group):
  intersection_letters = set([letter for letter in group[0]])
  if len(group) > 1:
    for string in group[1:]:
      letters_in_string = set([letter for letter in string])
      intersection_letters = intersection_letters.intersection(letters_in_string)
    
  return len(intersection_letters)

with open("input_6.txt", "r") as f:
  groups = read_strings_separated_by_blank_lines(f)
  print("Groups", len(groups))    
  print("Part 1:", sum([count_different_letters(group) for group in groups]))
  print("Part 2:", sum([count_intersection_letters(group) for group in groups]))
