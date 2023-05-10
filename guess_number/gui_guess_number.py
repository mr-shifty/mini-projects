import tkinter as tk
import random


class GuessNumber:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        self.number = random.randint(1, 100)
        self.guesses = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

        self.result = tk.Label(master, text="")
        self.result.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.guesses += 1

        if guess == self.number:
            self.result.config(
                text=("Congratulations! You guessed the number in {} guesses.".format(self.guesses))
                )
            self.button.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)
        elif guess < self.number:
            self.result.config(text="Too low. Guess again.")
        else:
            self.result.config(text="Too high. Guess again.")


root = tk.Tk()

h, w = 800, 300

root.geometry(f'{h}x{w}')
root.resizable(False, False)
root.title('Числовая угадайка')
game = GuessNumber(root)


root.mainloop()