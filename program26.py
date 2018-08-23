size=int(input())
list2=[int(x) for x in raw_input().split()]
list2.sort()
print " ".join(map(str,list2))
