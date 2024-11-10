a = input()
b = ''
for i in range(len(a)):
    if i < len(a)//2:
        if a[i] == 'п':
            b = b + '*'
        else:
            b = b + a[i]
    else:
        b = b + a[i]
print(b)