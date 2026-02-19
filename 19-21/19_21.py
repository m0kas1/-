"""решение 1 номера"""
def f(s, m):
    if s >= 125: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s + 4, m - 1), f(s * 2, m - 1)]
    # Если в 19 номере написано, что Ваня выиграл после НЕУДАЧНОГО ХОДА ПЕТИ, то меняем
    # all() на any() считаем результат ТОЛЬКО ДЛЯ 19 НОМЕРА. Записываем его где-то и ПОТОМ ОБРАТНО МЕНЯЕМ
    # any() на all()
    return any(h) if m % 2 != 0 else all(h)

# Перебираем все возможные исходы. Т. е. при каком кол-ве камней, кто выиграет.
# Первый ход по игре - это первый ход Пети. Второй ход по игре - это первый ход Вани.
# Четвертый ход по игре - это второй ход Вани.
print('19)', [s for s in range(1, 125) if not f(s, 1) and f(s, 2)])
print('20)', [s for s in range(1, 125) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 125) if not f(s, 2) and f(s, 4)])

"""решение 2 номера"""
# Все рассуждения аналогичны задаче выше
def f(a, b, m):
    if a + b <= 200: return m % 2 == 0
    if m == 0: return 0
    h = [f(a - 3, b - 4, m - 1), f (a - 8, b // 2, m - 1), f (a // 2, b - 10, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(100, 500) if not f(110, s, 1) and f(110, s, 2)])
print('20)', [s for s in range(100, 500) if not f(110, s, 1) and f(110, s, 3)])
print('21)', [s for s in range(100, 500) if not f(110, s, 2) and f(110, s, 4)])