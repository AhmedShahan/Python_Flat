import flet as ft 
import time



def main(pg:ft.Page):
    def printText(e):
        print(inPutText.value)
    pg.title="USER INPUT"
    inPutText=ft.TextField()
    pg.add(inPutText)  # Input Text filed
    Enter=ft.ElevatedButton(text="Enter", on_click=printText)
    pg.add(Enter)
ft.app(main)