def count_letter(letter, string):
	count = 0
	for char in string:
		if letter == char:
			count += 1
	return count	
	
def check_count(condition_min, condition_max, condition_letter, string):
	count = count_letter(condition_letter, string)
	return count >= condition_min and count <= condition_max
	
def check_letter(i1, i2, letter, string):
	string = string.strip()
	print(string[i1-1], string[i2-1], letter)
	if string[i1-1] == letter and string[i2-1] != letter:
		return True
	if string[i1-1] != letter and string[i2-1] == letter:
		return True
	return False

with open("input 2.txt", "r") as f:
	correct_count = 0
	for line in f:
		condition, string = line.split(":")
		condition_numbers, condition_letter = condition.split(" ")
		condition_min, condition_max = map(int, condition_numbers.split("-"))
		condition_true = check_letter(condition_min, condition_max, condition_letter, string)
		print(condition_min, condition_max, condition_letter, string, condition_true)
		if condition_true:
			correct_count += 1
	print(correct_count)

