from checks import check_letter, is_valid, is_valid_answer
from utils import display_hangman, get_word
from colorama import init, Fore, Style, Back

init()


def play(word):
    """Основная логика программы."""

    word_completion = '_ ' * len(word)
    guessed = False
    guessed_letters = []
    # guessed_word = []
    tries = 6
    print(f'{word}')
    print(f'{Fore.GREEN}{Style.BRIGHT}{display_hangman(tries)}\n\n{Style.RESET_ALL}'
          f'{Fore.BLUE}Я загадал слово, нужно его угадать{Style.RESET_ALL}\n{word_completion}\n'
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
                print(f'\n{Fore.YELLOW}{" " * 15}Буква уже была использована, введите другую.{Style.RESET_ALL}\n')
                check_letter(word, guessed_letters)
                continue
            if len(input_letter) > 1:
                if input_letter == word:
                    print(f"{Fore.GREEN}{Style.BRIGHT}\n{' ' * 20}Угадал слово, молодец 🥳{Style.RESET_ALL}")
                    play_again()

            if input_letter in word:
                guessed_letters.append(input_letter)
                for letter in word:
                    if letter not in guessed_letters:
                        print(f'{Fore.GREEN}\n{" " * 20}Угадал букву. Какая следующая?\n{Style.RESET_ALL}')
                        check_letter(word, guessed_letters)
                        guessed = False
                        break
                    guessed = True

                if guessed:
                    check_letter(word, guessed_letters)
                    print(f'{Fore.GREEN}{Style.BRIGHT}\n\n{" " * 25}Ты победил, красавец🎉🎊\n{Style.RESET_ALL}')
                    play_again()

            else:
                if tries > 1:
                    tries -= 1
                    print(
                        f'{Fore.YELLOW}{Style.BRIGHT}{display_hangman(tries)}{Style.RESET_ALL}')
                    print(f"{Fore.RED}\n{' ' * 25}Не угадал, попробуй еще{Style.RESET_ALL}\n")
                    check_letter(word, guessed_letters)
                else:
                    tries -= 1
                    print(
                        f'{Fore.RED}{Style.BRIGHT}{display_hangman(tries)}{Style.RESET_ALL}'
                    )
                    print(f"{Fore.RED}{Style.BRIGHT} {' ' * 10}Ты проиграл. К сожелению, без жертв не обошлось\n\n{Style.RESET_ALL}")
                    print(f'{Fore.BLUE}Загаданное слово: {Fore.LIGHTMAGENTA_EX}{word}{Style.RESET_ALL}')
                    play_again()


def play_again():
    """Отвечает за повтор игры."""

    answer = input(f'\n{Fore.LIGHTGREEN_EX}Хотите сыграть еще?{Fore.YELLOW} д/н\n\n{Fore.CYAN}Ваш ответ: {Style.RESET_ALL}').lower()
    if is_valid_answer(answer):
        play_again_answer(answer)
    else:
        while is_valid_answer(answer) is False:
            answer = input(
                f'\n{Fore.RED}Введите корректный ответ {Fore.YELLOW}д/н\n\n{Fore.CYAN}Ваш ответ: {Style.RESET_ALL}').lower()
            if is_valid_answer(answer):
                play_again_answer(answer)


def play_again_answer(answer: str) -> str:
    if answer == 'д':
        return play(get_word().upper())
    elif answer == 'н':
        print(f"\n{Fore.MAGENTA}Заходите снова, вам обязательно повезет 😌\n{Style.RESET_ALL}")
        exit()


def main():
    """Главная исполняющая функция."""
    name: str = input(f"\n{Fore.MAGENTA}Привет, как тебя зовут?\n\n{Fore.CYAN}Ваше имя: {Style.RESET_ALL}").capitalize()
    print(
        f'{Fore.BLUE}\nПривет, {name}. Давай сыграем с тобой в виселицу.\n'
        f'\n{Fore.MAGENTA}Не переживай, никто не умрет,'
        f'{Style.BRIGHT}но это не точно 😈\n\n{Style.RESET_ALL}'
    )
    print(play(get_word().upper()))


if __name__ == '__main__':
    main()
