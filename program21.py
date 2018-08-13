def sumofAP(n,a,d):
    sum = 0
    i = 0
    while i < n:
          sum = sum + a
          a = a + d
          i = i + 1
    return sum
n = 3
a = 1
d = 1
print(sumofAP(n,a,d))
