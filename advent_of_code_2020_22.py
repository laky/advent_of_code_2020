class CombatCards:
  def __init__(self, player_1_cards, player_2_cards):
    self.player_1_cards = player_1_cards
    self.player_2_cards = player_2_cards
    
  def play_next_move(self):
    player_1_card = self.player_1_cards.pop(0)
    player_2_card = self.player_2_cards.pop(0)    
    if player_1_card > player_2_card:
      self.player_1_cards.append(player_1_card)
      self.player_1_cards.append(player_2_card)
    else:
      self.player_2_cards.append(player_2_card)
      self.player_2_cards.append(player_1_card)
    
  def play_out(self):
    while len(self.player_1_cards) > 0 and len(self.player_2_cards) > 0:
      self.play_next_move()

class RecursiveCombatCards:
  def __init__(self, player_1_cards, player_2_cards):
    self.player_1_cards = player_1_cards
    self.player_2_cards = player_2_cards
    self.player_1_history = set()
    self.player_2_history = set()
    self.game_winner = None
    
  def play_next_move(self):
    if len(self.player_1_cards) == 0:
      self.game_winner = 2
      return
      
    if len(self.player_2_cards) == 0:
      self.game_winner = 1
      return
    
    # Check rule 1.
    if self._get_hand_representation(self.player_1_cards) in self.player_1_history or self._get_hand_representation(self.player_2_cards) in self.player_2_history:
      self.game_winner = 1
      return
      
    # Add carsds to history.
    self.player_1_history.add(self._get_hand_representation(self.player_1_cards))
    self.player_2_history.add(self._get_hand_representation(self.player_2_cards))
      
    # Draw a card.
    player_1_card = self.player_1_cards.pop(0)
    player_2_card = self.player_2_cards.pop(0)    
    
    if player_1_card <= len(self.player_1_cards) and player_2_card <= len(self.player_2_cards):
      # Recurse.
      sub_game = RecursiveCombatCards(self.player_1_cards[:player_1_card], self.player_2_cards[:player_2_card])
      self._add_cards_to_winner(player_1_card, player_2_card, sub_game.play_out())
      
    else: 
      # Determine by higher card.  
      if player_1_card > player_2_card:
        self._add_cards_to_winner(player_1_card, player_2_card, 1)
      else:
        self._add_cards_to_winner(player_1_card, player_2_card, 2)
    
  def play_out(self):
    while self.game_winner == None:
      self.play_next_move()
    return self.game_winner
      
  def determine_winner(self, card_1, card_2):

    
    if player_1_card > player_2_card:
      return 1
      
  def _get_hand_representation(self, cards):
    return ",".join([str(c) for c in cards])
    
  def _add_cards_to_winner(self, player_1_card, player_2_card, winner):
    if winner == 1:
      self.player_1_cards.append(player_1_card)
      self.player_1_cards.append(player_2_card)
    else:
      self.player_2_cards.append(player_2_card)
      self.player_2_cards.append(player_1_card)
    
    

test = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".split("\n")

test_2 = """Player 1:
43
19

Player 2:
2
29
14""".split("\n")

with open("input_22.txt", "r") as f:
  player_1_cards = []
  player_2_cards = []
  
  parsing_player_1 = True
  for line in f:
    line = line.strip()
    if line == "Player 1:" or line == "":
      continue
    
    elif line == "Player 2:":
      parsing_player_1 = False
    
    else:
      if parsing_player_1:
        player_1_cards.append(int(line))
      else:
        player_2_cards.append(int(line))
                        
  print(player_1_cards)
  print(player_2_cards)
  
  game = CombatCards(player_1_cards.copy(), player_2_cards.copy())
  game.play_out()
  print(game.player_1_cards)
  print(game.player_2_cards)
  
  end_cards = game.player_1_cards + game.player_2_cards
  print("Part 1:", sum( [a * b for (a,b) in zip( end_cards, range(len(end_cards), 0, -1))] ))
  
  print(player_1_cards)
  print(player_2_cards)
  
  game = RecursiveCombatCards(player_1_cards.copy(), player_2_cards.copy())
  winner = game.play_out()
  print(game.player_1_cards)
  print(game.player_2_cards)
  print(winner)
  
  end_cards = game.player_1_cards if winner == 1 else game.player_2_cards
  print("Part 2:", sum( [a * b for (a,b) in zip( end_cards, range(len(end_cards), 0, -1))] ))
  
  
