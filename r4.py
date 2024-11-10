n = int(input())
s = 0 
for x in range(n+1):
    f = 1
    for h in range(1,x+1):
        f = h * f
    s = s + f
print(s-1)