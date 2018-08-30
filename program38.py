q,w=map(int,raw_input().split())
q = q ^ w
w = q ^ w
q = q ^ w
print q,w
