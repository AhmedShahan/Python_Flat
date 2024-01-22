

import flet as ft 

def main(pg:ft.Page):
    pg.title="Practice"
    pg.theme_mode="light"

    textName=ft.Text(value="Shahan Ahmed",color="green", size=30)
    textDept=ft.Text(value="Department of Electrical & Computer Engineering",color="blue", size=30)
    textUni=ft.Text(value="North South University, Dhaka, Bangladesh",color="blue", size=30)
    textEmail=ft.Text(value="Email: shahan.ahmed@northsouth.edu",color="blue", size=30)
    pg.add(textName)
    pg.add(textDept)
    pg.add(textUni)
    pg.add(textEmail)
ft.app(main)