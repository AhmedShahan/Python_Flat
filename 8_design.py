import flet as ft 
import time 
from flet import colors

def main(page:ft.Page):
    page.title="Design in Flet"

    # theme change
    # page.theme_mode="dark"
    # page.theme_mode="light"

    # Align all the element into center
    page.vertical_alignment="CENTER" # All item in Left to Center
    page.horizontal_alignment="CENTER" # All item in Top to center
    # page.vertical_alignment=ft.MainAxisAlignment.CENTER 





    # text=ft.Text("Design in Flet")
    # Text Color change
    # text=ft.Text("Design in Flet", color="red")

    # Change Text size
    # text=ft.Text("Design in Flet", color="white", size=40)
    # text=ft.Text("Design in Flet", color=colors.BLUE_700, size=40)
    text=ft.Text("Design in Flet", color=colors.BLUE_700, size=40, bgcolor="white")




    page.add(text)

ft.app(main)