"""1 варик"""
def f(x, A):
    return (x % 21 == 0) <= ((x%A != 0) <= (x%77 != 0))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)

"""2 варик"""
# Наименьшую длину
otvet = []
i = [i/4 for i in range(1, 20000)]
for x in i:
    P = 66 <= x <= 67
    O = 32 <= x <= 125
    T = 30 <= x <= 491
    A = False
    F = (not A) <= (P or (not O) or (not T))
    if F == 0:
        otvet.append(x)
print(otvet[-1] - otvet[0])

# Наибольшую длину
otvet = []
for x in range(1, 200):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = True
    F = C <= (((not A) and B) <= (not C))
    if F == 1:
        otvet.append(x)
print(otvet[-1] - otvet[0])

"""3 варик"""
def f(A, x, y):
    return (x + 2*y > A) or (y < x) or (x < 30)

for A in range(0, 1000):
    if all(f(A, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)

"""4 варик"""
def F(A, x):
     return (x & 39 == 0) or ((x & 11 == 0) <= (not (x & A == 0)))

for A in range(0, 1000):
     if all(F(A, x) for x in range(0, 1000)):
         print(A)

"""5 варик"""
for x in range(100):
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    A = True
    F = (A <= P) and ((not Q) <= (not A))
    if F == 1:
        print(x)