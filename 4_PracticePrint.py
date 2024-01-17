'''
Shahan Ahmed
Department of Electrical & Computer Engineering
North South University, Dhaka, Bangladesh
shahan.ahmed@northsouth.edu
'''

import flet as ft

def main(page:ft.Page):
    page.title="This is Title"
    textName=ft.Text(value="Shahan Ahmed")
    textDept=ft.Text(value="Department of Electrica & Computer Engineering")
    textUni=ft.Text(value="North South University, Dhaka, Bangladesh")
    textEmail=ft.Text(value="Email:shahan.ahmed@northsouth.edu")

    page.controls.append(textName)
    page.controls.append(textDept)
    page.controls.append(textUni)
    page.controls.append(textEmail)
    page.update()

ft.app(main)