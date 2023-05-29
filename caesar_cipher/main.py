class CaesarCiepher:
    def __init__(self, shift):
        self.shift = shift
        self.encrypted_message = ""
        self.decrypted_message = ""
        self.ru_lower_first_chr = ord("а")
        self.ru_upper_first_chr = ord("А")
        self.ru_quantity_chrs = len(range(ord("А"), ord("Я") + 1))
        self.en_lower_first_chr = ord("a")
        self.en_upper_first_chr = ord("A")
        self.en_quantity_chrs = len(range(ord("A"), ord("Z") + 1))

    def ru_encrypt(self, message):
        for chars in message:
            if chars.isalpha():
                if chars.islower():
                    encoded_char = chr((ord(chars) - self.ru_lower_first_chr
                                        + self.shift)
                                       % self.ru_quantity_chrs
                                       + self.ru_lower_first_chr
                                       )
                    self.encrypted_message += encoded_char
                elif chars.isupper():
                    encoded_char = chr((ord(chars) - self.ru_upper_first_chr
                                        + self.shift)
                                       % self.ru_quantity_chrs
                                       + self.ru_upper_first_chr
                                       )
                    self.encrypted_message += encoded_char
            else:
                self.encrypted_message += chars
        return self.encrypted_message

    def ru_descript(self, message):
        for chars in message:
            if chars.isalpha():
                if chars.isupper():
                    decoded_char = chr((ord(chars) - self.ru_upper_first_chr - self.shift) % self.ru_quantity_chrs + self.ru_upper_first_chr)
                    self.decrypted_message += decoded_char
                elif chars.islower():
                    decoded_char = chr((ord(chars) - self.ru_lower_first_chr
                                        - self.shift) % self.ru_quantity_chrs + self.ru_lower_first_chr)
                    self.decrypted_message += decoded_char
            else:
                self.decrypted_message += chars
        return self.decrypted_message


def main():
    message = "Блажен, кто верует, тепло ему на свете!"
    encrypt_message = "Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!"
    shift = 10
    ciepher = CaesarCiepher(shift)
    encripted_message = ciepher.ru_encrypt(message)
    decrypted_message = ciepher.ru_descript(encrypt_message)
    print(encripted_message)
    print(decrypted_message)


if __name__ == "__main__":
    main()
