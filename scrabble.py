letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter, point in zip(letters, points)}

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    cap_letter = letter.upper()
    point_total += letter_to_points.get(cap_letter, 0)
  print(point_total)
  return point_total

score_word("brownie")
print(letter_to_points)

player_to_words = {"Player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}


player_to_points = {}
for player in player_to_words.keys():
  print(player)
  score_total = 0
  for words in player_to_words[player]:
    player_to_points[player] = 0
    
    print(words)
    word_points =  score_word(words)
    score_total += word_points
    player_to_points[player] = score_total
  print(player +  " has " + str(player_to_points[player]))

def play_word(player, word):
  player_to_words[player].append(word)

play_word("Player1", "QUIZ")
print(player_to_points)

def update_points(player):
    score_total = 0
    for word in player_to_words[player]:
      player_to_points[player] = 0
      print(word)
      word_points =  score_word(word)
      score_total += word_points
      player_to_points[player] = score_total
    print(player +  " has " + str(player_to_points[player]))

update_points("Player1")
print(player_to_points)
