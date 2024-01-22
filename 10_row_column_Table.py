import flet as ft 
import time
def main(pg:ft.Page):
    pg.title="TABLE"

    # alignment=ft.MainAxisAlignment.CENTER/ END/ SACE_BETWEEN/ SPACE_AROUND/ START/ SPACE_EVENLY
    pg.add(ft.Row(controls=[ft.Text("Name"),ft.Text("University"), ft.Text("Department"),ft.Text("Major"),],alignment=ft.MainAxisAlignment.SPACE_AROUND))
    pg.add(ft.Row(controls=[ft.Text("A"),ft.Text("NSU"), ft.Text("ECE"),ft.Text("CSE"),],alignment=ft.MainAxisAlignment.SPACE_AROUND))
    pg.add(ft.Row(controls=[ft.Text("B"),ft.Text("AIUB"), ft.Text("CSE"),ft.Text("Software Engineering"),],alignment=ft.MainAxisAlignment.SPACE_AROUND))
    pg.add(ft.Row(controls=[ft.Text("C"),ft.Text("IUB"), ft.Text("ECE"),ft.Text("EEE"),],alignment=ft.MainAxisAlignment.SPACE_AROUND))
    pg.add(ft.Row(controls=[ft.Text("D"),ft.Text("Brac"), ft.Text("ECE"),ft.Text("EEE"),],alignment=ft.MainAxisAlignment.SPACE_AROUND))
    pg.add(ft.Row(controls=[ft.Text("E"),ft.Text("UIU"), ft.Text("DMP"),ft.Text("IT"),],alignment=ft.MainAxisAlignment.SPACE_AROUND))
ft.app(target=main)