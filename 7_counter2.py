import flet as ft
import time
def main(page: ft.Page):
    page.title="Counter"

    text=ft.Text(color="white", size=50)
    page.add(text)

    for i in range(11):
        text.value="Counter : "+str(i)
        page.update()
        time.sleep(1)
ft.app(main)