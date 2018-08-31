nterms = int(raw_input())
n1 = 1
n2 = 1
count = 0
if nterms == 1:
	print(n1)
else:
	while count < nterms:
		print n1,
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count += 1
