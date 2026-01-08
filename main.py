import flet as ft
from datetime import datetime
def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.DARK


    text_hello = ft.Text(value='Hello world')

    def on_button_click(_):
        name = (name_input.value or "").strip()
        print(name)

        if name:
            if len(name) < 3:
                text_hello.value = 'Имя слишком короткое'
                text_hello.color = ft.Colors.RED
                name_input.value = None
            elif len(name) > 15:
                text_hello.value = 'Имя слишком длинное'
                text_hello.color = ft.Colors.RED
                name_input.value = None
            else:
                now = datetime.now()
                formatted_time = now.strftime("%Y-%m-%d / %H:%M:%S")

                text_hello.color = None
                text_hello.value = f"Привет,{name}!n/Время ввода: {formatted_time}"
                name_input.value = None
        else:
            text_hello.value = 'Введите корректное имя'
            text_hello.color = ft.Colors.RED



    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)

    name_input = ft.TextField(label='Введите имя', max_length=20,on_submit=on_button_click)

    page.add(text_hello, name_input, elevated_button)



ft.app(target=main)