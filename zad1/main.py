# zad 1 numerki d-_-b
# model 0 i 2, wariant b

from choice import fun_choice, met_choice, przedzial, condition
from algorithms import bisekcja, sieczne
from functions import fun1, fun2, fun3, fun4, fun5
from graphs import graph

fn = fun_choice()
func = locals()[f"fun{fn}"]
met = met_choice()
p, k = przedzial()
cond, limiter = condition()

if met == 1:
    x, i = bisekcja(func, p, k, cond, limiter)
else:
    x, i = sieczne(func, p, k, cond, limiter)

if x != 'err':
    print("Liczba wykonanych iteracji: ", i)
    print("x: ", x)
    graph(func, p, k, x, met)
else:
    print("Podany przedzial jest bledny!")