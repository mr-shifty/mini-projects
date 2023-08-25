from checks import check_letter, is_valid, is_valid_answer
from utils import display_hangman, get_word
from colorama import init, Fore, Style

init()

count_victory: int = 0
count_defeat: int = 0


def play(word, name):
    """Основная логика программы."""

    global count_victory
    global count_defeat

    word_completion = f"{word[0]} {'_ ' * (len(word)-2)}{word[-1]}"
    guessed: bool = False
    guessed_letters: list = []
    # guessed_word = []
    tries = 6
    attempt = 1

    # print(f'{word}')
    print(f'{Fore.GREEN}{Style.BRIGHT}'
          f'{display_hangman(tries)}\n\n{Style.RESET_ALL}'
          f'{Fore.BLUE}Я загадал слово, '
          f'нужно его угадать{Style.RESET_ALL}\n{word_completion}\n'
          )
    print(f'{Fore.BLUE}Итак, начнем.{Style.RESET_ALL}\n\n'
          f'{Fore.GREEN}Введите букву или слово.'
          f'\n{Fore.RED}Для выхода введите stop{Style.RESET_ALL}')
    while True:
        input_letter = input(f'{Fore.CYAN}\n\nВвод: {Style.RESET_ALL}').upper()
        if input_letter == 'STOP':
            exit()
        if is_valid(input_letter):
            if input_letter in guessed_letters:
                print(f'\n{Fore.YELLOW}{" " * 15}'
                      f'Буква уже была использована,'
                      f'введите другую.{Style.RESET_ALL}\n')
                check_letter(word, guessed_letters)
                continue
            if len(input_letter) > 1:
                if input_letter == word:
                    print(
                        f"{Fore.GREEN}{Style.BRIGHT}\n"
                        f"{' ' * 20}Угадал(а) слово с "
                        f"{Fore.YELLOW}{attempt} {Fore.GREEN}"
                        f"попытки из {Fore.YELLOW}6\n")
                    print(f"{' ' * 30}{Fore.GREEN}Молодец 🥳{Style.RESET_ALL}")
                    count_victory += 1
                    play_again(name)

            if input_letter in word:
                guessed_letters.append(input_letter)
                for letter in word:
                    if letter not in guessed_letters:
                        print(f'{Fore.GREEN}\n{" " * 20}'
                              f'Угадал букву. '
                              f'Какая следующая?\n{Style.RESET_ALL}')
                        check_letter(word, guessed_letters)
                        guessed = False
                        break
                    guessed = True

                if guessed:
                    check_letter(word, guessed_letters)
                    print(
                        f'{Fore.GREEN}{Style.BRIGHT}\n\n{" " * 25}'
                        f'Ты победил, красавец 🎉🎊\n{Style.RESET_ALL}')
                    print(
                        f'{Fore.GREEN}{" " * 25}'
                        f'Угадал(а) с {Fore.YELLOW}'
                        f'{attempt} {Fore.GREEN}попытки из {Fore.YELLOW}6')
                    count_victory += 1
                    play_again(name)

            else:
                if tries > 1:
                    tries -= 1
                    print(
                        f'{Fore.YELLOW}{Style.BRIGHT}'
                        f'{display_hangman(tries)}{Style.RESET_ALL}')
                    print(f"{Fore.RED}\n{' ' * 25}"
                          f"Не угадал, попробуй еще{Style.RESET_ALL}\n")
                    check_letter(word, guessed_letters)
                    attempt += 1
                else:
                    tries -= 1
                    print(
                        f'{Fore.RED}{Style.BRIGHT}'
                        f'{display_hangman(tries)}{Style.RESET_ALL}'
                    )
                    print(
                        f"{Fore.RED}{Style.BRIGHT} "
                        f"{' ' * 10}Ты проиграл. К сожелению, "
                        f"без жертв не обошлось\n\n{Style.RESET_ALL}")
                    print(
                        f'{Fore.BLUE}Загаданное слово: '
                        f'{Fore.LIGHTMAGENTA_EX}{word}{Style.RESET_ALL}')
                    count_defeat += 1
                    play_again(name)


def play_again(name: str):
    """Отвечает за повтор игры."""

    print(
        f'\n{Fore.BLUE}Твоя статистика, {name}:\n\n'
        f'{Fore.GREEN}Победы: {Fore.YELLOW}{count_victory}\n'
        f'{Fore.RED}Поражения: {Fore.YELLOW}{count_defeat}\n{Style.RESET_ALL}')

    answer = input(
        f'\n{Fore.LIGHTGREEN_EX}Хотите сыграть еще?'
        f'{Fore.YELLOW} д/н\n\n{Fore.CYAN}'
        f'Ваш ответ: {Style.RESET_ALL}').lower()
    if is_valid_answer(answer):
        play_again_answer(answer, name)
    else:
        while is_valid_answer(answer) is False:
            answer = input(
                f'\n{Fore.RED}Введите корректный ответ {Fore.YELLOW}д/н\n\n'
                f'{Fore.CYAN}Ваш ответ: {Style.RESET_ALL}').lower()
            if is_valid_answer(answer):
                play_again_answer(answer, name)


def play_again_answer(answer: str, name: str) -> str:
    """Варианты ответов для повтора игры."""

    if answer == 'д':
        return play(get_word().upper(), name)
    elif answer == 'н':
        print(
            f"\n{Fore.MAGENTA}"
            f"Заходите снова, вам обязательно повезет 😌\n{Style.RESET_ALL}")
        exit()


def main():
    """Главная исполняющая функция."""

    name: str = input(f"\n{Fore.MAGENTA}Привет, как тебя зовут?\n\n{Fore.CYAN}"
                      f"Ваше имя: {Style.RESET_ALL}").title()
    print(
        f'{Fore.BLUE}\nПривет, {name}. Давай сыграем с тобой в виселицу.\n'
        f'\n{Fore.MAGENTA}Не переживай, никто не умрет,'
        f'{Style.BRIGHT}но это не точно 😈\n\n{Style.RESET_ALL}'
    )
    # hints = input('Использовать подсказки? д/н')
    print(play(get_word().upper(), name))


if __name__ == '__main__':
    main()
