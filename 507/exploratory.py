import functools


f1 = lambda x: x**2
f2 = lambda x: x**3

f3 = lambda x: f1(f2(x))

print(f3(4))
