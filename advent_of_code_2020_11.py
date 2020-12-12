import copy

def count_occupied_neighbours(layout, row_i, column_i):
  rows_to_check = range(max(row_i-1, 0), min(row_i+2, len(layout)))
  columns_to_check = range(max(column_i-1, 0), min(column_i+2, len(layout[0])))
  taken_seats = sum([layout[r][c] == "#" for r in rows_to_check for c in columns_to_check])
  selected = 1 if layout[row_i][column_i] == "#" else 0
  return taken_seats - selected

def count_visible_neighbours_in_ray(layout, r, c, r_diff, c_diff):
  r += r_diff
  c += c_diff
  while r >= 0 and r < len(layout) and c >= 0 and c < len(layout[0]):
    if layout[r][c] == "#":
      return 1
    if layout[r][c] == "L":
      return 0
    r += r_diff
    c += c_diff
  return 0

def count_visible_neighbours(layout, r, c):
  return sum([
    count_visible_neighbours_in_ray(layout, r, c, -1, -1),
    count_visible_neighbours_in_ray(layout, r, c, -1, 0),
    count_visible_neighbours_in_ray(layout, r, c, -1, 1),
    count_visible_neighbours_in_ray(layout, r, c, 0, -1),
    count_visible_neighbours_in_ray(layout, r, c, 0, 1),
    count_visible_neighbours_in_ray(layout, r, c, 1, -1),
    count_visible_neighbours_in_ray(layout, r, c, 1, 0),
    count_visible_neighbours_in_ray(layout, r, c, 1, 1),
  ])  

def next_state(layout):
  next_layout = copy.deepcopy(layout)
  for r, row in enumerate(layout):
    for c, item in enumerate(row):
      count = count_occupied_neighbours(layout, r, c)
      if count == 0 and item == "L":
        next_layout[r][c] = "#"
      elif count >= 4 and item == "#":
        next_layout[r][c] = "L"
  return next_layout

def next_state_2(layout):
  next_layout = copy.deepcopy(layout)
  for r, row in enumerate(layout):
    for c, item in enumerate(row):
      count = count_visible_neighbours(layout, r, c)
      if count == 0 and item == "L":
        next_layout[r][c] = "#"
      elif count >= 5 and item == "#":
        next_layout[r][c] = "L"
  return next_layout
                        
def states_equal(layout_1, layout_2):
  return all([layout_1[r][c] == layout_2[r][c] for r in range(len(layout_1)) for c in range(len(layout_1[0]))])

def get_converging_state(initial_layout, next_state):
  layout = initial_layout
  next_layout = next_state(layout)
  while not states_equal(next_layout, layout):
    layout = next_layout
    next_layout = next_state(layout)
  return layout
    
def count_taken_seats(layout):
  return sum([ layout[r][c] == "#" for r in range(len(layout)) for c in range(len(layout[0])) ])

with open("input_11.txt", "r") as f:
  initial_layout = [[character for character in line.strip()] for line in f]

  print("Part 1:", count_taken_seats(get_converging_state(initial_layout, next_state)))
  print("Part 2:", count_taken_seats(get_converging_state(initial_layout, next_state_2)))
