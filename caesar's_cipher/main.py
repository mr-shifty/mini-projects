eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


len_alfas = len(rus_lower_alphabet)
phrase = "блажен, кто верует, тепло ему на свете!"
step = 10


for indx in range(len(phrase)):
    if phrase[indx].isalpha():
        place = rus_lower_alphabet.index(phrase[indx])
        new_index = (place + step) % len_alfas
        if phrase[indx] == phrase[indx].lower():
            print(rus_lower_alphabet[new_index], end='')
    else:
        print(phrase[indx], end="")
