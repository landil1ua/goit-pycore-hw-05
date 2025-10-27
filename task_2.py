import re
from typing import Callable


def generator_numbers(text: str):
    '''
    Функція яка шукає дійсні числа у тексті та повертає генератор
    Args:
        text(str): текст, в якому слід шукати дійсні числа
    Returns:
        generator: генератор зі знайденими числами
    '''
    for i in re.findall(r' \d+\.\d+|\d+ ', text):
        yield float(i)


def sum_profit(text: str, func: Callable):
    '''
    Функція яка розраховує загальну суму доходів клієнта із "відомості"
    Args:
        text(str): текст, в якому слід шукати дійсні числа
        func(Callable): функція, яка шукає числа в тексті
    Returns:
        sum_(float): загальна сума доходів
    '''
    sum_ = 0
    for i in func(text):
        sum_ += i
    return sum_


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
