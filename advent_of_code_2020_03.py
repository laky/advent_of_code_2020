from functools import reduce

def count_trees_on_way(x_diff, y_diff, tobbogan_map):
	count = 0
	x, y = 0, 0
	while y < len(tobbogan_map):
		if tobbogan_map[y][x % len(tobbogan_map[0])] == "#":
			count += 1
		x += x_diff
		y += y_diff
	return count

with open("input 3.txt", "r") as f:
	tobbogan_map = [line.strip() for line in f]
	slopes = [(1, 1), (3, 1), (5, 1), (7,1), (1,2)]
	trees_hit = [count_trees_on_way(x_diff, y_diff, tobbogan_map) for (x_diff, y_diff) in slopes]
	print(reduce((lambda x, y: x * y), trees_hit))
	
