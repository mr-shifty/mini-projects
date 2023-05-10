import tkinter
import webbrowser
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import customtkinter as CTk
import password
from PIL import Image


class InfoWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        h, w = 300, 100
        self.title("Инфо")
        self.geometry(f'{h}x{w}')
        self.resizable(False, False)
        self.label = CTk.CTkLabel(
            self,
            text="Developed by Pavel Melnikov\nGitHub(mr-shifty)",
            text_color='blue',
            font=("arial", 16),
            cursor="hand2",

        )
        self.label.pack(
            padx=20,
            pady=20
        )
        self.label.bind('<Button-1>', self.open_website)

    def open_website(*args):
        webbrowser.open_new_tab('https://github.com/mr-shifty')


class App(CTk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Главное окно
        h, w = 475, 370
        self.title("Генератор паролей")
        self.geometry(f'{h}x{w}')
        self.resizable(False, False)
        CTk.set_default_color_theme("green")

        self.logo = CTk.CTkImage(
            light_image=Image.open("password_generator/media/main_pic.jpg"),
            size=(475, 150)
        )
        self.logo_label = CTk.CTkLabel(
            master=self,
            text="",
            image=self.logo
        )
        self.logo_label.grid(
            row=0,
            column=0
        )
        self.password_frame = CTk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.password_frame.grid(
            row=1,
            column=0,
            padx=(20, 20),
            pady=(20, 20),
            sticky="nsew"
        )
        # Окно ввода пароля
        self.entry_password = CTk.CTkEntry(
            master=self.password_frame,
            width=300
        )
        self.entry_password.grid(
            row=0,
            column=0,
            padx=(0, 20),
        )
        self.btn_generate = CTk.CTkButton(
            master=self.password_frame,
            text="Сгенерировать",
            width=100,
            command=self.set_password
        )
        self.btn_generate.grid(
            row=0,
            column=1
        )
        # Слайдер длинны пароля
        self.settings_frame = CTk.CTkFrame(
            master=self
        )
        self.settings_frame.grid(
            row=2,
            column=0,
            padx=(5, 5),
            sticky="nsew",
        )
        self.password_length_slider = CTk.CTkSlider(
            master=self.settings_frame,
            from_=0,
            to=100,
            number_of_steps=100,
            command=self.slider_event
        )
        self.password_length_slider.grid(
            row=1,
            column=0,
            columnspan=3,
            pady=(20, 20),
            sticky='ew'
        )
        # Ввод длинны пароля
        self.password_length_entry = CTk.CTkEntry(
           master=self.settings_frame,
           width=50,
        )

        self.password_length_entry.grid(
            row=1,
            column=3,
            padx=(20, 20),
            sticky='ew'
        )
        self.password_length_slider.set(15)
        self.password_length_entry.insert(0, 15)
        self.password_length_entry.bind('<KeyRelease>', self.update_slider)
        # Чекбокс чисел
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="0-9",
            variable=self.cb_digits_var,
            onvalue=digits,
            offvalue=""
        )
        self.cb_digits.grid(
            row=2,
            column=0,
            padx=10
        )
        # Чекбокс маленьких букв
        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="a-z",
            variable=self.cb_lower_var,
            onvalue=ascii_lowercase,
            offvalue=""
        )
        self.cb_lower.grid(
            row=2,
            column=1,
        )
        # Чекбокс больших букв
        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="A-Z",
            variable=self.cb_upper_var,
            onvalue=ascii_uppercase,
            offvalue=""
        )
        self.cb_upper.grid(
            row=2,
            column=2
        )
        # Чекбокс символов
        self.cb_symbols_var = tkinter.StringVar()
        self.cb_symbols = CTk.CTkCheckBox(
            master=self.settings_frame,
            text="@#$%",
            variable=self.cb_symbols_var,
            onvalue=punctuation,
            offvalue=""
        )
        self.cb_symbols.grid(
            row=2,
            column=3
        )
        # Выбор темы
        self.apperance_mode_option_menu = CTk.CTkOptionMenu(
            master=self.settings_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.apperance_mode_option_menu.grid(
            row=3,
            column=3,
            columnspan=4,
            pady=20,
            sticky="we"
        )
        self.apperance_mode_option_menu.set('System')

        # Информационная кнопка
        self.info_button = CTk.CTkButton(
            master=self.settings_frame,
            text="Инфо",
            width=100,
            command=self.press_info
        )
        self.info_button.grid(
            row=3,
            column=0,
            pady=20,
        )
        self.toplevel_window = None

    def set_password(self):
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password.create_new(
            length=int(self.password_length_slider.get()),
            characters=self.get_characters()
            )
        )

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))

    def update_slider(self, value):
        value = int(self.password_length_entry.get())
        self.password_length_slider.set(value)

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get()
                        + self.cb_upper_var.get() + self.cb_symbols_var.get())
        return chars

    def press_info(self):
        if self.toplevel_window is None or \
                not self.toplevel_window.winfo_exists():
            self.toplevel_window = InfoWindow(self)
        else:
            self.toplevel_window.focus()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
