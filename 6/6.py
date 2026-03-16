# commands
# forward(n)/fd(n) - вперед
# back(n)/bk(n) - назад
# right(m)/rt(m) - вправо
# left(m)/lt(m) - влево
# down() - опустить хвост
# up() - поднять хвость
# for i in range(n): - сколько раз выполняется что-то (повтори ...)
# from turtle import * - импортировать все функции из библиотеки
# tracer(0) - скорость отрисовки (моментально)
# done() - отрисовка + бесконечное окно
# screensize(10000, 10000) - разрешение окна
# goto(x, y) - переход в точку (чтобы нарисовать систему координат)
# dot(n, 'red') - отметить место точкой (n - ширина, "red" - цвет)

"""1 number"""
# По дефолту бошка черепахи смотрит вправо (->) и хвост опущен!
from turtle import *
tracer(0)
m = 20
screensize(10000, 10000)
left(90)
for i in range(2):
    fd(1*m); lt(270); fd(16*m); rt(90)
up()
bk(4*m); rt(90); fd(10*m); lt(90)
down()
for i in range(2):
    fd(17*m); rt(90); fd(7*m); rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, "blue")
done()