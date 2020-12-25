def calculate(a, b, op):
  if op == "+":
    return a + b
  if op == "*":
    return a * b

def evaluate_expression(expression_items):
  a, op = None, None
  i = 0
  while len(expression_items) > 0:
    item = expression_items.pop(0)
        
    if item == "+" or item == "*":
      op = item
      continue
    
    if item == "(":
      n = evaluate_expression(expression_items)
    elif item == ")":
      return a  
    else:
      # Item is a number
      n = int(item)
      
    if a is None:
      a = n
    else:
      a = calculate(a, n, op)
  return a

def evaluate_expression_2(expression_items):
  a, op = None, None
  i = 0
  while len(expression_items) > 0:
    item = expression_items.pop(0)
    
    if item == "*":
      op = item
      return a * evaluate_expression_2(expression_items)
      
    elif item == "+":
      op = item
      continue
    
    elif item == "(":
      n = evaluate_expression_2(expression_items)
    elif item == ")":
      return a  
    else:
      # Item is a number
      n = int(item)
      
    if a is None:
      a = n
    else:
      a = calculate(a, n, op)

  return a

test = ["1 + 2 * 3 + 4 * 5 + 6", "1 + (2 * 3) + (4 * (5 + 6))", "2 * 3 + (4 * 5)", 
  "5 + (8 * 3 + 9 + 3 * 4 * 3)",
  "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
  "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

with open("input_18.txt", "r") as f:
  lines = [line.strip() for line in f]

  expressions = [line.replace("(", " ( ").replace(")", " ) ").replace("  ", " ").strip().split(" ") for line in lines]  
  results = [evaluate_expression(expression) for expression in expressions]
  print(results)
  print("Part 1:", sum(results))
  
  expressions = [line.replace("(", " ( ").replace(")", " ) ").replace("  ", " ").strip().split(" ") for line in lines]  
  results = [evaluate_expression_2(expression) for expression in expressions]
  print(results)
  print("Part 2:", sum(results))
