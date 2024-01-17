import flet as ft
import time
def main(page: ft.Page):
    page.title="Counter"

    text=ft.Text()
    page.add(text)

    for i in range(11):
        text.value=i
        page.update()
        time.sleep(1)
ft.app(main)