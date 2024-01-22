import flet as ft 
import time 
from flet import colors

def main(page:ft.Page):
    page.title="Design in Flet"
    text=ft.Text("Row & Column", color="red", size=40, bgcolor="green")
    page.add(text)

    page.add(ft.Row(
        [ft.Text("Heading 1"),
        ft.Text("Heading 2"),
        ft.Text("Heading 3"),
        ft.Text("Heading 4"),
        ft.Text("Heading 5"),
        ]
    ))
    page.add(ft.Row(
    [ft.Text("Heading 1"),
    ft.Text("Heading 2"),
    ft.Text("Heading 3"),
    ft.Text("Heading 4"),
    ft.Text("Heading 5"),
    ]
    ))
ft.app(main)