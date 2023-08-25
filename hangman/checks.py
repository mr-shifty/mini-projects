from colorama import Fore, Style


def check_letter(word: str, guessed_letters: str) -> str:
    """Проверяет букву в слове."""

    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')


def is_valid(letter: str) -> bool:
    """Проверка корректности ввода."""

    if not letter.isalpha():
        print(
            f'{Fore.RED}\nВвод некорректен, введите букву или слово целиком'
            f'{Style.RESET_ALL}')
        return False
    return True


def is_valid_answer(answer: str) -> None:
    """Проверка на правильность ответа."""

    return answer.isalpha() and answer == 'д' or answer == 'н'
