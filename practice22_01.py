

# import flet as ft 
# def main(pg:ft.Page):
#     pg.title="Practice"
#     pg.theme_mode="light"

#     textName=ft.Text(value="Shahan Ahmed",color="green", size=30)
#     textDept=ft.Text(value="Department of Electrical & Computer Engineering",color="blue", size=30)
#     textUni=ft.Text(value="North South University, Dhaka, Bangladesh",color="blue", size=30)
#     textEmail=ft.Text(value="Email: shahan.ahmed@northsouth.edu",color="blue", size=30)
#     pg.add(textName)
#     pg.add(textDept)
#     pg.add(textUni)
#     pg.add(textEmail)
# ft.app(main)


# import flet as ft 
# import time
# def main(pg:ft.Page):
#     pg.title="Counter 1"
#     pg.theme_mode="light"
#     pg.horizontal_alignment="CENTER"
#     pg.vertical_alignment="CENTER"

#     text=ft.Text(color="red", size=50)
#     pg.add(text)

#     for i in range(11):
#         text.value="Count: "+ str(i)
#         pg.update()
#         time.sleep(1)
# ft.app(main)


import flet as ft 
import time
def main(pg:ft.Page):
    pg.title="TABLE"
    pg.theme_mode="light"
    pg.horizontal_alignment="CENTER"
    pg.add(ft.Text(value="Table Making", size=40))
    
    pg.add(
        ft.Row([
        ft.Text("Name of The Student")]),
        ft.Column([
        ft.Text("A")])

    )
        # ft.Text("Name of The University"),
        # ft.Text("Department"),
        # ft.Text("Major"),
        # ]),

        # ft.Column([
        # ft.Text("A"),
        # ft.Text("NSU"),
        # ft.Text("ECE"),
        # ft.Text("CSE"),
        # ]),
    
    
    
    # )
ft.app(main)