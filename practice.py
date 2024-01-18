# import flet as ft 


# def main(page:ft.Page):
#     page.title="Practice"

#     textName=ft.Text(value="Shahan Ahmed")
#     textDept=ft.Text(value="Department of Electrical & computer & Engineering")
#     textUni=ft.Text(value="North South University, Dhaka, Bangladesh")
#     textEmail=ft.Text(value="Email: shahan.ahmed@northsouth.edu")
#     page.controls.append(textName)
#     page.controls.append(textDept)
#     page.controls.append(textUni)
#     page.controls.append(textEmail)
#     page.update()
# ft.app(main)


### add function isnted of update
# import flet as ft 


# def main(page:ft.Page):
#     page.title="Practice"

#     textName=ft.Text(value="Shahan Ahmed")
#     textDept=ft.Text(value="Department of Electrical & computer & Engineering")
#     textUni=ft.Text(value="North South University, Dhaka, Bangladesh")
#     textEmail=ft.Text(value="Email: shahan.ahmed@northsouth.edu", color="red")
#     page.add(textName)
#     page.add(textDept)
#     page.add(textUni)
#     page.add(textEmail)
# ft.app(main)



##### Counter version 1
# import flet as ft 
# import time 

# def main(page:ft.Page):
#     page.title="Practice"

#     text=ft.Text(value="COUNTER VERSION 1", color="blue", size=40)
#     page.add(text)

#     for i in range(11):
#         text2=ft.Text(value=f"Count: {i}")
#         page.add(text2)
#         time.sleep(1)
# ft.app(main)



##### Counter version 2
import flet as ft 
import time 

def main(page:ft.Page):
    page.title="Practice"

    text=ft.Text(value="COUNTER VERSION 2", color="blue", size=40)
    page.add(text)
    text2=ft.Text(color="blue", size=40)
    page.add(text2)

    for i in range(11):
        text2.value="Count: "+ str(i)
        page.update()
        time.sleep(1)
ft.app(main)