def sumofAP(n,a,d):
    sum = 0
    p = 0
    while p < n:
          sum = sum + a
          a = a + d
          p = p + 1
    return sum
n = 3
a = 1
d = 1
print(sumofAP(n,a,d))
