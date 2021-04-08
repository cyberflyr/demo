def twice(n):
    n *= 2
    return n

a = int(input("a:"))
b = int(input("b:"))
print(a)
if a > 3:
    b += 4
    if b > 5:
        c = a + twice(b)
    else:
        c = twice(a) + b
else:
    b -= 2
    if b < 1:
        c = a - twice(b)
    else:
        c = twice(a) - b
print(c)
