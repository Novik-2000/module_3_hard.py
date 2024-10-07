from math import floor


def calculate_structure_sum(data) :
    summa = int()
    for elem in data:
        if isinstance(elem, (list, tuple, set)):
            summa += calculate_structure_sum(elem)
        elif isinstance(elem, dict):
            summa += calculate_structure_sum(elem.items())

        if isinstance(elem, (int, float)):
            summa += elem
        if isinstance(elem, str):
            summa += len(elem)
    return summa


data_structure = [
    [1, 2, 4],
    {'a': 4, 'b': 5},
    (6,),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
result = calculate_structure_sum(data_structure)
print(result)
