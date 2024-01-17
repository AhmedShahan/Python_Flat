'''
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
'''

import flet as ft
import time

def main(page:ft.Page):
    page.title="Counter App"

    for i in range(10):
        text1=ft.Text(value=f"Count: {i}", color="white", size=40)
        page.add(text1)
        time.sleep(1)

    # for i in range(10):
    #     text=ft.Text(i)
    #     page.add(text)
    #     time.sleep(2)
    # for i in range(10):
    #     page.add(i)

ft.app(main)