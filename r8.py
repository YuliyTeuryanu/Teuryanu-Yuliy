x = int(input())
y = int(input())
z = int(input())
y = int(input())
print(x*y)
print((1/2)*x*y)

a = int(input())
b = oct(a)[2:]
while len(b) < 10:
    b = '0' + b 
print(b)