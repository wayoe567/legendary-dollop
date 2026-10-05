a = 10
b = 20 
print("Before swap: a =", a, ", b =", b)

t = a       # keep a's value safe in t
a = b       # copy b into a
b = t       # copy the save vaiue into b

print("After swap:  a =", a, ", b =", b)

