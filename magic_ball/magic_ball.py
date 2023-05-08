from random import choice


answers = [
    "Бесспорно", "Мне кажется - да",
    "Пока неясно, попробуй снова", "Даже не думай",
    "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
    "Никаких сомнений", "Хорошие перспективы",
    "Лучше не рассказывать", "По моим данным - нет",
    "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять",
    "Весьма сомнительно"
    ]


def is_valid_answer(answer):
    return answer.isalpha() and answer == 'хочу' or answer == 'не хочу'


def answer_the_questions(name):
    print("Задайте ваш вопрос")
    while True:
        answer = input()
        print(choice(answers))
        print(f"{name}, Хотите задать еще вопрос?")
        answer = input()
        if is_valid_answer(answer):
            if answer == "хочу":
                return answer_the_questions(name)
            elif answer == "не хочу":
                return ('Возвращайся если возникнут вопросы!')
        while is_valid_answer(answer) is False:
            print('Некорректный ответ')
            answer = input()
            if is_valid_answer(answer):
                if answer == "хочу":
                    return answer_the_questions(name)
                elif answer == "не хочу":
                    return ('Возвращайся если возникнут вопросы!')


def read_input():
    name: str = input()
    return name


def main():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Как вас зовут?')
    name = read_input()
    print(f'Привет, {name}')
    print(answer_the_questions(name))


if __name__ == '__main__':
    main()
