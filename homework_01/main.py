"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = [n**2 for n in numbers]

    print(result)


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_odd_numbers(number_):
    if (number_ % 2) != 0:
        return True
    else:
        return False
    

def filter_even_numbers(number_):
    if (number_ % 2) == 0:
        return True
    else:
        return False
    

def is_prime(number_):
    k = 0
    for i in range(2, number_ // 2+1):
        if (number_ % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False


def filter_numbers(numbers_, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    numbers = list(numbers_)
    if filter_type == ODD:
        result_filter = filter(filter_odd_numbers, numbers)
        print(list(result_filter))
        
    elif filter_type == EVEN:
        result_filter = filter(filter_even_numbers, numbers)
        print(list(result_filter))

    elif filter_type == PRIME:
        result_filter = filter(is_prime, numbers)
        print(list(result_filter))
    
    else:
        print("no such filter")

    



if __name__ == "__main__":
    filter_numbers([1, 2, 3], ODD)
    filter_numbers([2, 3, 4, 5], EVEN)
