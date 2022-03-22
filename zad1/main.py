# zad 1 numerki
# model 0 i 2, wariant b

from choice import *
from algorithms import bisekcja, sieczne
from functions import *
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
    print("f(x) =", func(x))
    graph(func, p, k, x, met)
elif i == 0:
    print("Dzielenie przez 0!")
elif i == 'outofrange':
    print("W danym przedziale nie ma miejsca zerowego!")
else:
    print("Podany przedzial jest bledny!")