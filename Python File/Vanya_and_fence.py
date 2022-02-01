n,f = [int(x) for x in input().split()]

height=[int(i) for i in input().split()]
width = len(height)
for i in height:
    if (i>f):
        width+=1
    else:
        continue
print(width)
