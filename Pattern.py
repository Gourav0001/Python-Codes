n = int (input())
print ("Type 1 for True and 0 for False")

y = int (input())

if y == 1:
    i = 1
    while i <= n:
        print ("*" * i)
        i += 1
else:
    i = n
    while i >= 1:
        print ("*" * i)
        i -= 1

