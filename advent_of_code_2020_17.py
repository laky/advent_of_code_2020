from collections import deque
import copy 

class ConwayCube:
 
  def __init__(self, starting_grid):
    self.grid = deque([starting_grid])
    self._pad_grid()
    
  def _pad_grid(self):
    levels = len(self.grid)
    rows = len(self.grid[0])
    columns = len(self.grid[0][0])
    
    if self._active_cell_in_level(0):
      self.grid.appendleft(self._get_new_empty_level(rows, columns))
      levels += 1
    if self._active_cell_in_level(levels - 1):
      self.grid.append(self._get_new_empty_level(rows, columns))
      levels += 1
      
    if self._active_cell_in_row(0):
      for level in self.grid:
        level.appendleft( deque(["." for i in range(columns)]) )
      rows += 1
    if self._active_cell_in_row(rows - 1):
      for level in self.grid:
        level.append( deque(["." for i in range(columns)]) )
      rows += 1
        
    if self._active_cell_in_column(0):
      for level in self.grid:
        for row in level:
          row.appendleft(".")
      columns += 1
    if self._active_cell_in_column(columns - 1):
      for level in self.grid:
        for row in level:
          row.append(".")
      columns += 1
      
  def _active_cell_in_level(self, l):
    return any([item == "#" for row in self.grid[l] for item in row])
    
  def _active_cell_in_row(self, r):
    return any([item == "#" for level in self.grid for item in level[r]])
    
  def _active_cell_in_column(self, c):
    return any([row[c] == "#" for level in self.grid for row in level])
  
  def _get_new_empty_level(self, rows, columns):
    return deque([ deque(["." for i in range(columns)]) for j in range(rows) ])

  def _count_active_neighbours(self, l, r, c):
    levels_to_check = range(max(l - 1, 0), min(l + 2, len(self.grid)))
    rows_to_check = range(max(r - 1, 0), min(r + 2, len(self.grid[0])))
    columns_to_check = range(max(c - 1, 0), min(c + 2, len(self.grid[0][0])))
    active_cells = sum([self.grid[l][r][c] == "#" for l in levels_to_check for r in rows_to_check for c in columns_to_check])
    current_cell = 1 if self.grid[l][r][c] == "#" else 0
    return active_cells - current_cell
  
  def next_state(self):
    next_grid = copy.deepcopy(self.grid)
    
    for l, level in enumerate(self.grid):
      for r, row in enumerate(level):
        for c, item in enumerate(row):
          active_neighbours = self._count_active_neighbours(l, r, c)
          if item == "#" and (active_neighbours < 2 or active_neighbours > 3):
            next_grid[l][r][c] = "."
          if item == "." and active_neighbours == 3:
            next_grid[l][r][c] = "#"
    self.grid = next_grid
    self._pad_grid()
    
  def count_active(self):
    return sum(
      [item == "#" for level in self.grid for row in level for item in row]
    )
    
  def __str__(self):
    string = ""
    for level in self.grid:
      for row in level:
        for item in row:
          string += str(item)
        string += "\n"
      string += "\n"
    string += "---\n"
    return string
      

test = """.#.
..#
###""".split("\n")

with open("input_17.txt", "r") as f:
  starting_grid = deque([deque([ c for c in line.strip()]) for line in test])

  cube = ConwayCube(starting_grid)
  print(cube)
  for i in range(6):
    cube.next_state()
    print(cube)
    
  print("Part 1:", cube.count_active())
