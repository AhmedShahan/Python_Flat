import flet as ft


def main(pg:ft.Page):
    pg.theme_mode="Dark"
    pg.title="To do List App"
    # pg.appbar=ft.AppBar(title=ft.Text("To Do list", size=30),center_title=True)
    # pg.window_max_height="700"
    # pg.window_max_width="500"
    pg.bgcolor="bluegrey900"
    pg.horizontal_alignment=ft.MainAxisAlignment.CENTER
    pg.vertical_alignment=ft.MainAxisAlignment.CENTER

    pg.add(ft.TextField("Shahan Ahmed"))

    ## Main Container
    # pg.add(
    #     ft.Container(
    #         width="300",
    #         height="500",
    #         bgcolor="black",
    #         # alignment=ft.MainAxisAlignment.CENTER
    #         # alignment=ft.MainAxisAlignment.CENTER
    #     )
    # )
    pg.update()

ft.app(target=main, view=ft.WEB_BROWSER)