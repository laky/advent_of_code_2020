subject_number = 7
divisor = 20201227

def find_encryption_key(pk_1, pk_2):
  value = 1
  loop_count = 0
  while True:
    value = value * subject_number % divisor
    loop_count += 1
    if value == pk_1:
      return transform_pk(pk_2, loop_count)
    elif value == pk_2:
      return transform_pk(pk_1, loop_count)
        
def transform_pk(pk, loop_count):
  value = 1
  for i in range(loop_count):
    value = value * pk % divisor
  return value

test = ["5764801", "17807724"]

with open("input_25.txt", "r") as f:
  pk_1, pk_2 = [int(line.strip()) for line in f]

  print("Part 1:", find_encryption_key(pk_1, pk_2))
  
