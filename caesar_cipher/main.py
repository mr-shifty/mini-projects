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
                    decoded_char = chr((ord(chars) - self.ru_upper_first_chr
                                        - self.shift) % self.ru_quantity_chrs
                                       + self.ru_upper_first_chr)
                    self.decrypted_message += decoded_char
                elif chars.islower():
                    decoded_char = chr((ord(chars) - self.ru_lower_first_chr
                                        - self.shift) % self.ru_quantity_chrs
                                       + self.ru_lower_first_chr)
                    self.decrypted_message += decoded_char
            else:
                self.decrypted_message += chars
        return self.decrypted_message

    def en_encrypt(self, message):
        for chars in message:
            if chars.isalpha():
                if chars.islower():
                    encoded_char = chr((ord(chars) - self.en_lower_first_chr
                                        + self.shift)
                                       % self.en_quantity_chrs
                                       + self.en_lower_first_chr
                                       )
                    self.encrypted_message += encoded_char
                elif chars.isupper():
                    encoded_char = chr((ord(chars) - self.en_upper_first_chr
                                        + self.shift)
                                       % self.en_quantity_chrs
                                       + self.en_upper_first_chr
                                       )
                    self.encrypted_message += encoded_char
            else:
                self.encrypted_message += chars
        return self.encrypted_message

    def en_descript(self, message):
        for chars in message:
            if chars.isalpha():
                if chars.isupper():
                    decoded_char = chr((ord(chars) - self.en_upper_first_chr
                                        - self.shift) % self.en_quantity_chrs
                                       + self.en_upper_first_chr)
                    self.decrypted_message += decoded_char
                elif chars.islower():
                    decoded_char = chr((ord(chars) - self.en_lower_first_chr
                                        - self.shift) % self.en_quantity_chrs
                                       + self.en_lower_first_chr)
                    self.decrypted_message += decoded_char
            else:
                self.decrypted_message += chars
        return self.decrypted_message


def main():
    # ru_message = "Блажен, кто верует, тепло ему на свете!"
    # ru_encrypt_message = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
    en_message = 'my name is Python!'
    # en_encrypt_message = "Hawnj pk swhg xabkna ukq nqj."
    shift = len(en_message)
    # for shift in range(0, 26):
    ciepher = CaesarCiepher(shift)
    # ru_encripted_message = ciepher.ru_encrypt(ru_message)
    # ru_decrypted_message = ciepher.ru_descript(ru_encrypt_message)
    en_encripted_message = ciepher.en_encrypt(en_message)
    # en_decrypted_message = ciepher.en_descript(en_encrypt_message)
    # print(ru_encripted_message)
    # print(ru_decrypted_message)
    print(en_encripted_message)
    # print(en_decrypted_message)


if __name__ == "__main__":
    main()
