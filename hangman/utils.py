from random import choice
from data import word_list, stages


def display_hangman(tries: int) -> int:
    """Показывает попытки"""

    return stages[tries]


def get_word() -> str:
    """Выводит рандомное слово"""

    return choice(word_list).upper()
