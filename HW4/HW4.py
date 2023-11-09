from functools import reduce

'''Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.'''

numbers1 = [1, 2, 3, 4, 5]
'''среднее от первого списка reduce(lambda x, y: x + y, numbers1) / reduce(lambda x, y: x + (y / y), numbers1)'''

numbers2 = [5, 4, 3, 2, 1]
'''среднее от второго списка reduce(lambda x, y: x + y, numbers2) / reduce(lambda x, y: x + 1, numbers2)'''

if __name__ == '__main__':
    print(*map(lambda x, y: x / y, [(sum((xi - reduce(lambda x, y: x + y, numbers1) / 
        reduce(lambda x, y: x + 1, numbers1)) * (yi - reduce(lambda x, y: x + y, numbers2) / 
        reduce(lambda x, y: x + 1, numbers2)) for xi, yi in zip(numbers1, numbers2)))], 
        [(sum((xi - reduce(lambda x, y: x + y, numbers1) / reduce(lambda x, y: x + 1, numbers1))
        ** 2 for xi in numbers1) ** 0.5 * (sum((yi - reduce(lambda x, y: x + y, numbers2) /
        reduce(lambda x, y: x + 1, numbers1)) ** 2 for yi in numbers2) ** 0.5))]))
