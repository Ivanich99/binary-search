import random


def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
    midle = len(arr) // 2
    while arr[midle] != value and left <= right:
        if value > arr[midle]:
            left = midle + 1
        else:
            right = midle - 1

        midle = (left + right) // 2
    return -1 if left > right else midle


mass = [random.randint(0, 100) for _ in range(100)]
mass.sort()
print(mass)

searching_element = int(input('ВВедите число для поиска: '))
print(binary_search(mass, searching_element))
