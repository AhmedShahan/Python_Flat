import flet as ft 

def main(pg:ft.Page):
    pg.title="To Do List"
    pg.theme_mode="dark"
    pg.window_height="500"
    pg.window_width="500"
    pg.horizontal_alignment="CENTER"

    def buttonClick(e):
        text=ft.Text(value=textInput.value)
        pg.add(text)
        # text=textInput.value
        print(text)


    pg.add(ft.Text("TO DO LIST",size=40, color="BLUE"))

    textInput=ft.TextField(border_color="white")
    # pg.add(textInput)

    addButton=ft.ElevatedButton(text="ADD", on_click=buttonClick)
    # pg.add(addButton)

    pg.add(ft.Row(controls=[textInput,addButton],alignment=ft.MainAxisAlignment.SPACE_BETWEEN))

    pg.add(ft.Text("\nYour Listed Items Are", color="Green",size=30))
    


ft.app(target=main)
