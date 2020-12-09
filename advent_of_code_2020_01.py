def find_numbers_summing_to(sorted_input_array, number):
	start = 0
	end = len(sorted_input_array)-1
	
	while start < end:
		sum = sorted_input_array[start] + sorted_input_array[end]
		if sum == number:
			 return (start, end)
		elif sum < number:
			start += 1
		else:
			end -= 1	
	return None


if __name__ == "__main__":
  with open("input.txt", "r") as f:
  	input_array = [int(line) for line in f.readlines()]
  	
  	input_array.sort()
  	print(len(input_array))
  	for i1 in range(len(input_array)):
  		ans = find_numbers_summing_to(input_array, 2020-input_array[i1])
  		if ans != None:
  			i2, i3 = ans
  			print(i1, i2, i3)
  			print(input_array[i1], input_array[i2], input_array[i3])
  			print(input_array[i1] * input_array[i2] * input_array[i3])
  			exit(0)
