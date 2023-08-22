def check_letter(word: str, guessed_letters: str) -> str:
    """Проверяет букву в слове."""

    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')


def is_valid(letter: str) -> bool:
    """Проверка на букву в вводе"""

    if len(letter) == 0 or not letter.isalpha():
        print('Вы ввели не букву')
        return False
    return True
