#  У вас есть список чисел, и ваша задача - отсортировать его по убыванию.

# В императивном стиле
numbers = [9, 5, 3, 4, 1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[i]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)

# В декларативном стиле
numbers = [9, 5, 3, 4, 1]

print(sorted(numbers, reverse=True))