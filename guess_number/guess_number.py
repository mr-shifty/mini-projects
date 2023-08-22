from random import choice, randint

answers = [
    "Сколько можно!!! Нажми блин д/н?",
    "Присмотрись, написано же нажми д/н"
    ]
answers_digit = [
    "Сказано же, нажми цифру от 1 до 100!",
    "Это игра про числа, которые загадываются от 1 до 100",
    "Эксперимент не удался. Нажми цифру от 1 до 100!"
    ]


def read_input() -> str:
    num: str = input()
    return num


def is_valid_num(num: int) -> bool:
    return num.isdigit() and 1 <= int(num) <= 100


def is_valid_answer(answer: str) -> bool:
    return answer.isalpha() and answer == 'д' or answer == 'н'


def game():
    rand_dig = randint(1, 100)
    count = 1
    count_answers = 0
    count_answers_digit = 0
    while True:
        num = read_input()
        if num == 'stop':
            break
        if is_valid_num(num):
            if int(num) < rand_dig:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
            elif int(num) > rand_dig:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
            else:
                print(f'Вы угадали c {count} попытки, поздравляем!')
                print('Хотите сыграть еще? д/н')
                answer = input()
                if is_valid_answer(answer):
                    if answer == "д":
                        print('Введите число от 1 до 100')
                        return game()
                    elif answer == 'н':
                        break
                else:
                    while is_valid_answer(answer) is False:
                        if count_answers < 2:
                            print("Не понимаю ваш ответ :(")
                            print("Нажмите д/н")
                            answer = input()
                        count_answers += 1
                        if count_answers >= 2:
                            print(choice(answers))
                            answer = input()
                        if is_valid_answer(answer):
                            if answer == "д":
                                print('Введите число от 1 до 100')
                                return game()
                            elif answer == 'н':
                                return ('Спасибо, что играли в'
                                        'числовую угадайку. Еще увидимся...')

        else:
            if count_answers_digit < 2:
                print('А может быть все-таки введем целое число от 1 до 100?')
            count_answers_digit += 1
            if count_answers_digit >= 2:
                print(choice(answers_digit))

    return ('Спасибо, что играли в числовую угадайку. Еще увидимся...')


def main():
    print("Добро пожаловать в числовую угадайку")
    print('Введите число от 1 до 100 или напишите stop, чтобы прекратить игру')
    print(game())


if __name__ == "__main__":
    main()
