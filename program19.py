num = int(raw_input())
factorial = 1
if num < 1:
	print("sorry,factorial does not exist for negative numbers")
elif num == 0:
	print("The factorial of 0 is 1")
else:
	for i in range(1,num + 1):
		factorial = factorial*i
	print(factorial)
