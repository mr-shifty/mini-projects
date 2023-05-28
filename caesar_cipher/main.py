class CaesarCiepher:
    def __init__(self, shift):
        self.shift = shift
        self.encrypted_message = ""

    def ru_encrypt(self, message):
        self.lower_first_chr = 1072
        self.upper_first_chr = 1040
        self.quantity_chrs = 32
        for chars in message:
            if chars.isalpha():
                if chars.islower():
                    encoded_char = chr((ord(chars) - self.lower_first_chr
                                        + self.shift)
                                       % self.quantity_chrs
                                       + self.lower_first_chr
                                       )
                    self.encrypted_message += encoded_char
                elif chars.isupper():
                    encoded_char = chr((ord(chars) - self.upper_first_chr
                                        + self.shift)
                                       % self.quantity_chrs
                                       + self.upper_first_chr
                                       )
                    self.encrypted_message += encoded_char
            else:
                self.encrypted_message += chars
        return self.encrypted_message


def main():
    message = "Блажен, кто верует, тепло ему на свете!"
    shift = 10
    ciepher = CaesarCiepher(shift)
    encripted_message = ciepher.ru_encrypt(message)
    print(encripted_message)


main()
