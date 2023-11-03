# Переписать алгоритм в процедурном стиле
# Структурное программирование
# Определение функции merge_sort, которая выполняет сортировку методом слияния.

def merge_sort(arr):
    if len(arr) > 1:  # Проверка, что длина массива больше 1 (иначе сортировка не нужна).
        left_half, right_half = method_name3(arr)

        i = j = k = 0  # Инициализация индексов для объединения двух половин.

        # Объединение левой и правой половин в один отсортированный массив.
        i, j, k = method_name2(arr, i, j, k, left_half, right_half)

        # Добавление оставшихся элементов из левой и правой половин (если такие есть).
        method_name1(arr, i, k, left_half)

        method_name1(arr, j, k, right_half)


def method_name3(arr):
    mid = len(arr) // 2  # Вычисление середины массива.
    left_half = arr[:mid]  # Создание левой половины массива.
    right_half = arr[mid:]  # Создание правой половины массива.
    # Рекурсивный вызов merge_sort для левой и правой половин массива.
    merge_sort(left_half)
    merge_sort(right_half)
    return left_half, right_half


def method_name2(arr, i, j, k, left_half, right_half):
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
            arr[k] = left_half[i]  # Если элемент из левой меньше, помещаем его в исходный массив.
            i += 1
        else:
            arr[k] = right_half[j]  # Если элемент из правой меньше, помещаем его в исходный массив.
            j += 1
        k += 1
    return i, j, k


def method_name1(arr, j, k, right_half):
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


my_array = [64, 34, 25, 12, 22, 11, 90]  # Создание неотсортированного массива.
merge_sort(my_array)  # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", my_array)  # Вывод отсортированного массива.

# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.

n = int(input("Введите n: "))

print('\n'.join([''.join([f'{i} * {j} = {i * j}\n' for j in range(1, 10)]) for i in range(1, n + 1)]))
