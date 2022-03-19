# zad 1 numerki d-_-b
# model 0 i 2, wariant b

#   TO DO LIST
# - bisekcja, sprawdzenie czy dobrze dziala
# - metoda siecznych, napisanie jej xd      CHECK
# - metoda siecznych, sprawdzenie czy dziala tak jak trzeba
# - wykresy
# - w metodzie menu() problem z przekazaniem funkcji funX() [X = 1, 2, ..., 5]

from choice import fun_choice, met_choice, przedzial, condition
from algorithms import bisekcja, sieczne
from functions import arr_fn, fun1, fun2, fun3, fun4, fun5
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
    graph(func, p, k, x, met, arr_fn[fn - 1])
else:
    print("Podany przedzial jest bledny!")