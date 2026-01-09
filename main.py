import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.DARK

    greeting_history = []
    favorite_names = []

    greeting_text = ft.Text('История приветствий:')

    favorite_text = ft.Text('Избранные имена:')

    text_hello = ft.Text(value='Hello world')


    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
                hour = datetime.now().hour
                time_text = "утреннее время" if hour < 12 else "вечернее время"


                text_hello.color = None
                text_hello.value = f"Привет {name}! ({time_text})"
                name_input.value = None

                greeting_history.append(name)
                #print(greeting_history)
                greeting_text.value = 'История приветствий: \n' + "\n".join(greeting_history)

        else:
            text_hello.value = 'Введите корректное имя'
            text_hello.color = ft.Colors.RED

    def add_to_favorite(_):
        if not greeting_history:
            text_hello.value = 'Сначала добавьте имя'
            text_hello.color = ft.Colors.RED
        else: 
            last_name = greeting_history[-1]
            if last_name not in favorite_names:
                favorite_names.append(last_name)
                favorite_text.value = 'Избранные имена: \n' + "\n".join(favorite_names)
            text_hello.value = f"{last_name}  добавлено в избранное"
            text_hello.color = None


    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        greeting_text.value = 'История приветствий:' 


    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    favorite_button = ft.ElevatedButton("⭐ В избранное", on_click=add_to_favorite)

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    main_object = ft.Row([name_input, elevated_button, clear_button])

    text_row = ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER)

    header_row = ft.Row([greeting_text, favorite_text], alignment=ft.MainAxisAlignment.START)

    page.add(text_row, main_object, favorite_button, header_row)



ft.app(target=main)