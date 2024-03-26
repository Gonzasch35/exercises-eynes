import random


def simple_list():
    alumnos = []

    for n in range(10):


        alumnos.append({'id': n + 1, 'age': random.randint(1, 100)})
    
    return alumnos


def sort_list():
    pass
