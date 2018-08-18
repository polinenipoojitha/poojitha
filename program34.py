string = raw_input()
num_lines = 1
for i in string:
	if(i=='.'):
		num_lines = num_lines+1
		print(num_lines)
