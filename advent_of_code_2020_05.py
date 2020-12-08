def find_empty_seat(seat_ids, max_id):
	min_id = max_id - len(seat_ids)
	sum_to_reach = (min_id + max_id) / 2 * (len(seat_ids) + 1)
	return sum_to_reach - sum(seat_ids)

with open("input_5.txt", "r") as f:
	seat_ids = []
	for line in f:
		binary = line.strip().replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
		seat_ids.append(int(binary, 2))
	
	max_id = max(seat_ids)
	print("Part 1:", max_id)
	print("Part 2:", find_empty_seat(seat_ids, max_id))
	
