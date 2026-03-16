# Ходы: +1, *2. Прийти в 50 из 2, притом пройти через 36, но не проходить через 17
def f(start, end):
    if start > end or start == 17:
        return 0
    if start == end:
        return 1
    return f(start + 1, end) + f(start * 2, end)
print(f(2, 36)*f(36, 50))
