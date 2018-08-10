num = 11
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("no")
           print(i,"times",num//i,"is",num)
           break
   else:
       print("yes")
else:
   print("no")
