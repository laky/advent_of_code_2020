def validate_string(string, rules):
  possible_matches = [["0"]]
  
  while len(possible_matches) > 0:
    possible_match = possible_matches.pop(0)
    
    if len(possible_match) > len(string):
      continue
      
    if "".join(possible_match) == string:
      return True
      
    i = 0
    while i < len(possible_match) and (possible_match[i] == "a" or possible_match[i] == "b"):
      i += 1
    
    if i >= len(possible_match) or "".join(possible_match[:i]) != string[:i]:
      continue 
      
    c = possible_match[i]    
    for rule in rules[c]:
      possible_matches.append(possible_match[:i] + rule + possible_match[i+1:])
      
  return False

test = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".split("\n")

test_2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".split("\n")

with open("input_19.txt", "r") as f:
  rules = dict()
  strings = []
  processing_rules_done = False
  for line in f:
    line = line.strip()
    
    if line == "":
      processing_rules_done = True
      continue
      
    if not processing_rules_done:
      rule_id, rule = line.split(": ")
      if "|" not in rule:
        rule = rule.replace('"', "")
        rules[rule_id] = [rule.split(" ")]
      else:
        rules[rule_id] = [r.split(" ") for r in rule.split(" | ")]
      
    else:
      strings.append(line)

  print("Part 1:", sum([validate_string(string, rules) for string in strings]))
  
  rules["8"] = [["42"], ["42", "8"]]
  rules["11"] = [["42", "31"], ["42", "11", "31"]]
  print("Part 2:", sum([validate_string(string, rules) for string in strings]))
