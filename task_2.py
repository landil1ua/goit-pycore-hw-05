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
    for i in re.findall(r' \d+\.\d+ | \d+ ', text):
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
