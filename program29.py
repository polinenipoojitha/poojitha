time = int(input())
hour = time // 3600
time %=3600
minutes = time // 60
time %=60
minutes = time
print("h:m-> %d:%d" %( hour,minutes))
