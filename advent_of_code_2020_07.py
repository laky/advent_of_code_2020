from collections import namedtuple
import re

def process_bag(string):
  reg_exp_bag = r"^([0-9]*)(\s)?([a-zA-Z\s]+)\sbag(s)?$"
  m = re.match(reg_exp_bag, string.strip())
  name = m.group(3)
  count = int(m.group(1)) if m.group(1) != "" else 1
  return name, count
  
def find_all_containing(bag_name, bags):
  previous_count = 0
  bags_containing = bags[bag_name].contained_in
  while (len(bags_containing) > previous_count):
    # We added a bag last time round.
    previous_count = len(bags_containing)
    for bag_to_check in bags_containing.copy():
      bags_containing = bags_containing.union(bags[bag_to_check].contained_in)

  return bags_containing

def count_all_bags_inside(bag_name, bags):
  if len(bags[bag_name].contains.items()) == 0:
    return 0
  bags_to_count = [count*count_all_bags_inside(name, bags) for name, count in bags[bag_name].contains.items()]
  return 1 + sum(bags_to_count)

with open("input_7.txt", "r") as f:
  bags = dict()
  Bag = namedtuple('Bag', 'name contained_in contains')
  for line in f:
    line = line.strip()[:-1]
    bag_name,_ = process_bag(line.split("contain")[0])
    bags_contained = dict([process_bag(bag) for bag in line.split("contain")[1].split(",")])
    if bag_name not in bags:
      bags[bag_name] = Bag(bag_name, set(), bags_contained)
    else:
      bags[bag_name] = Bag(bag_name, bags[bag_name].contained_in, bags_contained)
    
    for contained_bag_name in bags_contained:
      if contained_bag_name not in bags:
        bags[contained_bag_name] = Bag(contained_bag_name, set([bag_name]), dict())
      else:
        bags[contained_bag_name].contained_in.add(bag_name)

  print("Part 1:", len(find_all_containing("shiny gold", bags)))
  print("Part 2:", count_all_bags_inside("shiny gold", bags) - 1)
