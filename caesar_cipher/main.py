class CaesarCiepher:
    def __init__(self, shift):
        self.shift = shift
        self.encrypted_message = ""

    def ru_encrypt(self, message):
        self.first_chr = 1072
        self.quantity_chrs = 32
        for chars in message:
            if chars.isalpha():
                encoded_char = chr((ord(chars) - self.first_chr + self.shift) % self.quantity_chrs + self.first_chr)
                self.encrypted_message += encoded_char
            else:
                self.encrypted_message += chars
        return self.encrypted_message
    

def main():
    message = "блажен, кто верует, тепло ему на свете!"
    shift = int(input())
    ciepher = CaesarCiepher(shift)
    encripted_message = ciepher.ru_encrypt(message)
    print(encripted_message)


main()
