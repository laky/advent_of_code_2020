from collections import namedtuple
from copy import deepcopy
from functools import reduce
from math import sqrt


TOP = 0
LEFT = 1
BOTTOM = 2
RIGHT = 3
EDGES = [TOP, LEFT, BOTTOM, RIGHT]

class Tile:
  def __init__(self, id, tile):
    self.id = id
    self.tile = tile
  
  def __str__(self):
    string = str(self.id) + "\n"
    for row in self.tile:
      string += row + "\n"
    string += "\n"
    return string
    
  def get_all_orientations(self):
    tile_size = len(self.tile)
    
    return [
      Tile(self.id, [ "".join([self.tile[r][c] for c in range(tile_size)]) for r in range(tile_size) ]),
      Tile(self.id, [ "".join([self.tile[tile_size - 1 - r][c] for c in range(tile_size)]) for r in 
      range(tile_size) ]),
      
      Tile(self.id, [ "".join([self.tile[r][tile_size - 1 - c] for c in range(tile_size)]) for r in range(tile_size) ]),
      Tile(self.id, [ "".join([self.tile[tile_size - 1 - r][tile_size - 1 - c] for c in range(tile_size)]) for r in 
      range(tile_size) ]),
      
      
      Tile(self.id, [ "".join([self.tile[c][r] for c in range(tile_size)]) for r in range(tile_size) ]),
      Tile(self.id, [ "".join([self.tile[tile_size - 1 - c][r] for c in range(tile_size)]) for r in range(tile_size) ]),
      Tile(self.id, [ "".join([self.tile[c][tile_size - 1 - r] for c in range(tile_size)]) for r in range(tile_size) ]),
      Tile(self.id, [ "".join([self.tile[tile_size - 1 - c][tile_size - 1 - r] for c in range(tile_size)]) for r in range(tile_size) ]),
    ]
    
class AssembledTiles:
  def __init__(self, tiles_to_use, tiles_used, max_size):
    self.tiles_to_use = tiles_to_use
    self.tiles_used = tiles_used
    self.max_size = max_size
    
  def get_possible_next_states(self):
    possible_next_states = []
 
    for tile_index, tile_to_try in enumerate(self.tiles_to_use):
     for possible_tile_orientation in tile_to_try.get_all_orientations():
       for ((r, c), tile) in self.tiles_used.items():
         for position in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
           if position not in self.tiles_used:
             if check_tile_fits(possible_tile_orientation, position, self.tiles_used): 
               new_tiles_to_use = self.tiles_to_use[:tile_index] + self.tiles_to_use[tile_index+1:]
               #print(new_tiles_to_use)
               new_tiles_used = self.tiles_used.copy()
               new_tiles_used[position] = possible_tile_orientation
               xs = [x for (x, y) in new_tiles_used.keys()]
               ys = [y for (x, y) in new_tiles_used.keys()]
               if max(xs) - min(xs) < self.max_size and max(ys) - min(ys) < self.max_size:
                 possible_next_states.append(AssembledTiles(new_tiles_to_use, new_tiles_used, self.max_size))
               # Add a check for dimensions.
    #print(len(possible_next_states))
    return possible_next_states
    
  def get_corner_ids(self):
    xs = [x for (x, y) in self.tiles_used.keys()]
    ys = [y for (x, y) in self.tiles_used.keys()]
    
    return [
      self.tiles_used[min(xs), min(ys)].id,
      self.tiles_used[min(xs), max(ys)].id,
      self.tiles_used[max(xs), min(ys)].id,
      self.tiles_used[max(xs), max(ys)].id,
    ]
    
  def get_map(self):
    rs = [r for (r, c) in self.tiles_used.keys()]
    cs = [c for (r, c) in self.tiles_used.keys()]
    
    # print([ [self.tiles_used[(r, c)].id for c in range(min(cs), max(cs) + 1)] for r in range(min(rs), max(rs) + 1)])
    #for r in range(min(rs), max(rs) + 1):
    #  for c in range(min(cs), max(cs) + 1):    
    #    print(self.tiles_used[(r, c)])
    map = [ [cut_tile(self.tiles_used[(r, c)].tile) for c in range(min(cs), max(cs) + 1)] for r in range(min(rs), max(rs) + 1)]
    
    merged_map = []
    for tile_row in map:
      tile_1 = tile_row[0]
      for tile_2 in tile_row[1:]:
        tile_1 = merge_tiles(tile_1, tile_2)
      for row in tile_1:
        merged_map.append(row)
        
    return merged_map

def cut_tile(tile):
  return [ "".join([ tile[r][c] for c in range(1, len(tile) - 1) ]) for r in range(1, len(tile) - 1) ] 
  
def merge_tiles(tile_1, tile_2):
  return [ tile_1[r] + tile_2[r] for r in range(len(tile_1)) ]
        
def parse_tile(tile_lines):
  tile_id = int(tile_lines[0].replace("Tile ", "").replace(":", ""))
  tile = tile_lines[1:]
  return Tile(tile_id, tile)
    
def get_edge(e, tile):
  if e == TOP:
    return tile.tile[0]
  if e == LEFT:
    return "".join([tile.tile[i][0] for i in range(len(tile.tile))])
  if e == BOTTOM:
    return tile.tile[-1]
  if e == RIGHT:
    return "".join([tile.tile[i][-1] for i in range(len(tile.tile))])

def check_tile_fits(tile, position, tiles_dict):
  fits = True
  r, c = position
  
  if (r-1, c) in tiles_dict:
    fits = fits and get_edge(TOP, tile) == get_edge(BOTTOM, tiles_dict[(r-1, c)])  
  if (r, c-1) in tiles_dict:
    fits = fits and get_edge(LEFT, tile) == get_edge(RIGHT, tiles_dict[(r, c-1)])  
  if (r+1, c) in tiles_dict:
    fits = fits and get_edge(BOTTOM, tile) == get_edge(TOP, tiles_dict[(r+1, c)])  
  if (r, c+1) in tiles_dict:
    fits = fits and get_edge(RIGHT, tile) == get_edge(LEFT, tiles_dict[(r, c+1)])  
    
  return fits    

"""
                  #  - (0, 18)
#    ##    ##    ### - (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19)
 #  #  #  #  #  #    - (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
"""
def check_monster(tile, r, c):
  places_to_check = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
  
  for pr, pc in places_to_check:
    if r+pr >= len(tile) or c+pc >= len(tile) or tile[r+pr][c+pc] != "#":
      return False
  return True
  
def count_monsters_in_map(map):
  return sum([check_monster(map, r, c) for r in range(len(map)) for c in range(len(map))])

test = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...""".split("\n")

"""
Test solution:
1951    2311    3079
2729    1427    2473
2971    1489    1171

20899048083289
"""

with open("input_20.txt", "r") as f:
  tiles = []
  
  tile_lines = []
  for line in f:
    line = line.strip()
    
    if line != "":
      tile_lines.append(line)
      
    else:
      tiles.append(parse_tile(tile_lines))
      tile_lines = []
  if len(tile_lines) != 0:
    tiles.append(parse_tile(tile_lines))
    
        
  assembled_tiles = AssembledTiles(tiles[1:], {(0,0): tiles[0]}, int(sqrt(len(tiles))))
  states = [assembled_tiles]
  
  while len(states) > 0:
    state = states.pop()
    # print([tile.id for tile in state.tiles_to_use])
    # print([(pos, tile.id) for pos, tile in state.tiles_used.items()])
    if len(state.tiles_to_use) == 0:
      break
    states.extend(state.get_possible_next_states())
  # Loop until we find a good state or run out of options.

  print([tile.id for tile in state.tiles_to_use])
  print([(pos, tile.id) for pos, tile in state.tiles_used.items()])  
  print("Part 1:", reduce((lambda x, y: x * y), state.get_corner_ids()))
  
  map = state.get_map()
  map_tile = Tile(0, map)
  print(map_tile)
  monsters = max([count_monsters_in_map(map_orientation.tile) for map_orientation in map_tile.get_all_orientations()])
  print("Part 2:", sum([ map_tile.tile[r][c] == "#" for c in range(len(map_tile.tile)) for r in range(len(map_tile.tile)) ]) - monsters * 15)
  
