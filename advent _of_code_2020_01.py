def find_numbers_summing_to(sorted_input_array, number):
	start = 0
	end = len(input_array)-1
	
	while start < end:
		sum = input_array[start] + input_array[end]
		if sum == number:
			 return (start, end)
		elif sum < number:
			start += 1
		else:
			end -= 1	
	return (-1, -1)

with open("input.txt", "r") as f:
	input_array = [int(line) for line in f.readlines()]
	
	input_array.sort()
	print(len(input_array))
	for i1 in range(len(input_array)):
		i2, i3 = find_numbers_summing_to(input_array, 2020-input_array[i1])
		if i2 != -1:
			print(i1, i2, i3)
			print(input_array[i1], input_array[i2], input_array[i3])
			print(input_array[i1] * input_array[i2] * input_array[i3])
			exit(0)
