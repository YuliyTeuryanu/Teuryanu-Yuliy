n = int(input())
b = []
for i in range(n):
    a = int(input())
    b.append(a)
s = 0 
p = 1 
for i in range(len(b)):
    if i % 2 == 0:
        s = s + b[i]
    else:
        p = p * b[i]
print(s,p)
print(min(b),max(b))