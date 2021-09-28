s1 = []
# Push function adds latest element on top of stack implemented by append() in Python
s1.append('a')
s1.append('b')
s1.append('c')
# Display function is simply the print function
print (s1)
# Pop function deletes the newest element in stack, implemented by pop() in Python

print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1)

s1.append('d')
s1.append('e')
s1.append('f')

print (s1)

import time
word = "test "
x = word*10000000000000000000
time.sleep(5)
print ("this message wont appear if stack overflow has occurred!")