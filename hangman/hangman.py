from checks import check_letter, is_valid
from utils import display_hangman, get_word


def play(word):
    """Основная логика программы."""

    word_completion = '_ ' * len(word)
    guessed = False
    guessed_letters = []
    # guessed_word = []
    tries = 6
    print(f'{display_hangman(tries)}\n\n'
          f'Я загадал слово, нужно его угадать\n{word}\n{word_completion}\n'
          )
    print('Итак, начнем. Введите букву или слово')
    while True:
        input_letter = input('\n\nВвод: ').upper()
        is_valid(input_letter)
        if input_letter in guessed_letters:
            print('Буква уже была использована, введите другую.')
            check_letter(word, guessed_letters)
            continue
        if len(input_letter) > 1:
            if input_letter == word:
                print("Угадал слово, молодец")
                break
        if input_letter in word:
            guessed_letters.append(input_letter)
            for letter in word:
                if letter not in guessed_letters:
                    print('Вы угадали букву. Какая следующая?')
                    check_letter(word, guessed_letters)
                    guessed = False
                    break
                guessed = True

            if guessed:
                check_letter(word, guessed_letters)
                print('\nТы победил, красавец')
                break
        else:
            if tries > 1:
                tries -= 1
                print(display_hangman(tries))
                print("Не угадал, попробуй еще")
                check_letter(word, guessed_letters)
            else:
                tries -= 1
                print(display_hangman(tries))
                print("Ты проиграл, отдавай все деньги")
                break


def main():
    """Главная исполняющая функция."""

    print(
        'Привет. Давай сыграем с тобой в виселицу.\n'
        'Не переживай, никто не умрет, но это не точно😈\n\n'
    )
    play(get_word().upper())


if __name__ == '__main__':
    main()
