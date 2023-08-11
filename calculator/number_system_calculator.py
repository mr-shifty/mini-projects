from colorama import init, Fore, Style

init()


def convert_to_decimal():
    num_set = '0123456789abcdef'
    result = 0
    base = int(input(
        'Введите систему счисления, '
        'из которой нужно перевести (от 2-ой до 16-ой)\n'
        )
    )

    number = input(f'Введите ваше число в {base}-ой системе счисления\n')[::-1]

    for i in range(len(number)):
        result += num_set.find(number[i].lower()) * (base ** i)

    return (
        f'Выполнен перевод из {base}-ой системы счисления.'
        f'\nРезультат:\n{result}'
    )


def convert_from_decimal() -> str:
    num_set = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        "A", "B", "C", "D", "E", "F"
    ]
    final_result = ""
    base = int(input(
        f'{Fore.BLUE}Введите систему счисления, '
        f'в которую нужно перевести (от 2 до 16){Style.RESET_ALL}\n'))
    number = int(input(f'{Fore.BLUE}Введите число, '
                       f'которое нужно перевести\n{Style.RESET_ALL}'))

    while number != 0:
        result = number % base
        final_result = str(num_set[result])+final_result
        number //= base

    return (
        f'{Fore.YELLOW}Выполнен перевод в {base}-ую систему '
        f'счисления\n'
        f'Результат:{Style.RESET_ALL}\n'
        f'{Fore.GREEN}{final_result}{Style.RESET_ALL}'
    )


def read_input():
    answer = input()
    return answer


def main():
    print('Добро пожаловать в калькулятор систем счисления.\n')
    while True:
        print(
            'Введите:\n'
            'in - для перевода в дясятичную систему,\n'
            'from - для перевода из десятичной системы,\n'
            'exit - для выхода'
        )

        decimal_answer = read_input()
        if decimal_answer == 'in':
            print(convert_to_decimal())
        elif decimal_answer == 'from':
            print(convert_from_decimal())
        elif decimal_answer == 'exit':
            break
        continue_answer = input('Выполнить еще перевод? д/н\n')
        if continue_answer == 'д'.lower():
            continue
        elif continue_answer == 'н'.lower():
            break


if __name__ == '__main__':
    main()
