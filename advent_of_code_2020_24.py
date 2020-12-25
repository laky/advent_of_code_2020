"""
Board coordinates are defined as follows:
   / \     / \     / \     / \
  /   \   /   \   /   \   /   \
 /     \ /     \ /     \ /     \
|       |       |       |       |
| -1,-3 | -1,-1 | -1,1  | -1,3  |
|       |       |       |       |
 \     / \     / \     / \      /
  \   /   \   /   \   /   \    /
   \ /     \ /     \ /     \ /
    |       |       |       |
    | 0,-2  |  0,0  |  0,2  |
    |       |       |       |
   / \     / \     / \     / \
  /   \   /   \   /   \   /   \
 /     \ /     \ /     \ /     \
|       |       |       |       |
| 1,-3  |  1,-1 |  1,1  |  1,3  |
|       |       |       |       |
 \     / \     / \     / \     /
  \   /   \   /   \   /   \   /
   \ /     \ /     \ /     \ /
"""

test="""sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split("\n")

class Board:
  
  def __init__(self):
    self.black = set()
    
  def follow_instructions(self, instructions):
    r, c = 0, 0
    for instr in instructions:
      if instr == "e":
        c -= 2
      elif instr == "w":
        c += 2
      elif instr == "ne":
        r -= 1
        c -= 1
      elif instr == "se":
        r += 1
        c -= 1
      elif instr == "nw":
        r -= 1
        c += 1
      elif instr == "sw":
        r += 1
        c += 1
    if (r,c) in self.black:
      self.black.remove((r,c))
    else:
      self.black.add((r,c))
      
  def day_flip(self):
    # Get all relevant tiles (black and neighbours).
    tiles_to_check = set()
    for b in self.black:
      tiles_to_check.add(b)
      for n in self._get_neighbours(*b):
        tiles_to_check.add(n)
        
    # Flip accordingly.
    new_black = set()
    for t in tiles_to_check:
      count = self._count_neighbours(*t)
      if t in self.black and count > 0 and count <= 2:
        new_black.add(t)
      elif t not in self.black and count == 2:
        new_black.add(t)
    
    self.black = new_black
    
  def _get_neighbours(self, r, c):
    return [(r-1, c-1), (r, c-2), (r+1, c-1), (r+1, c+1), (r, c+2), (r-1, c+1)]
    
  def _count_neighbours(self, r, c):
    return sum([n in self.black for n in self._get_neighbours(r, c)])
      

def parse_instructions(string):
  instructions = []
  string_list = list(string)
  while len(string_list) > 0:
    c = string_list.pop(0)
    
    if c == "e" or c == "w":
      instructions.append(c)
    
    else:
      c += string_list.pop(0)
      instructions.append(c)
  return instructions

with open("input_24.txt", "r") as f:
  instructions = [parse_instructions(line.strip()) for line in f]
  
  board = Board()
  for instruction in instructions:
    board.follow_instructions(instruction)
  
  print("Part 1:", len(board.black))
  
  for i in range(100):
    board.day_flip()
  print("Part 2:", len(board.black))
   
