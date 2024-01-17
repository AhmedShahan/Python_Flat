import flet as ft 

def main(page: ft.Page):
    page.title="Basic Output"

    text=ft.Text(value="Shahan Ahmed", color="red")
    # page.controls.append(text)
    # page.update()

    # আমরা চাইলেই উপরের দি লাইনকে একটা লাইনে করে লিখতে পারি। 
    #     page.controls.append(text) page.update() এই দুইটা লাইনকে যদি সহজ করার জন্য 
    # page.add(text) তাহলে এটি page.controls.append করবে এবং page.update() করে দিবে। 
    page.add(text)
ft.app(main)
