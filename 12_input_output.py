import flet as ft 
import time



def main(pg:ft.Page):
    pg.title="USER INPUT"


    def printText(e):
        print(inPutText.value)
        # pg.add(ft.Text(value=inPutText.value))
        HelloText.value=inPutText.value
        pg.update()
        


    inPutText=ft.TextField()
    pg.add(inPutText)  # Input Text filed
    Enter=ft.ElevatedButton(text="Enter", on_click=printText)
    pg.add(Enter)

    HelloText=ft.Text()
    pg.add(HelloText)
    
ft.app(main)