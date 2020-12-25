class Cup:
  
  def __init__(self, cup_number):
    self.number = cup_number
    self.next = None

class CrabCupsGame:
  
  def __init__(self, sequence):
    self.sequence = sequence
    self.selected = sequence[0]
    self.cup_numbers_to_cups = { cup.number : cup for cup in self.sequence }
    self.min = min([cup.number for cup in sequence])
    self.max = max([cup.number for cup in sequence])
    print("Initialised")
    
  def next_state(self):
    picked_up = []
    cup = self.selected
    for i in range(3):
      cup = cup.next
      picked_up.append(cup)
    self.selected.next = cup.next
    
    new_number = self._subtract_one(self.selected.number)
    picked_up_list = [cup.number for cup in picked_up]
    while new_number in picked_up_list:
      new_number = self._subtract_one(new_number)
      
    insert_after = self.cup_numbers_to_cups[new_number]
    picked_up[-1].next = insert_after.next
    insert_after.next = picked_up[0]
    self.selected = self.selected.next
      
  def _subtract_one(self, number):
    number = number - 1
    if number < self.min:
      number = self.max
    return number
    
  def print_state(self):
    cup = self.cup_numbers_to_cups[1].next
    string = ""
    while (cup.number != 1):
      string += str(cup.number)
      cup = cup.next
    return string
    
  def get_two_after_one(self):
    cup = self.cup_numbers_to_cups[1].next
    return (cup.number, cup.next.number)
    
input = "193467258"
test = "389125467"

starting_sequence = [Cup(int(c)) for c in input]
print(len(starting_sequence))
for i, c in enumerate(starting_sequence):
  c.next = starting_sequence[(i+1)%len(starting_sequence)]
game = CrabCupsGame(starting_sequence)
for i in range(100):
  game.next_state()
print("Part 1:", game.print_state())
  
starting_sequence = [Cup(int(c)) for c in input]
max_number = max([c.number for c in starting_sequence])
starting_sequence += [Cup(n) for n in range(max_number+1, 1000001)]
for i, c in enumerate(starting_sequence):
  c.next = starting_sequence[(i+1)%len(starting_sequence)]
game = CrabCupsGame(starting_sequence)
counter = 0
for i in range(10000000):
  game.next_state()
  counter += 1
  if counter % 1000000 == 0:
    print("Step:", counter, "/ 10000000")
number_1, number_2 = game.get_two_after_one()
print("Part 2:", number_1 * number_2)

