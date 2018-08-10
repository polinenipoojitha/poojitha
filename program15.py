lower_limit = int(raw_input("Enter the lower limit : "))
upper_limit = int(raw_input("Enter the upper limit : "))
for i in range(lower_limit,upper_limit+1):
	if(i%2 == 0):
		break
		print(i)
