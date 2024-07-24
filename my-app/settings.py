import flet as ft
class Settings(ft.Column):
    def __init__(page: ft.Page):
        super.__init__(
            controls=ft.Text('settings')
        )
        page.controls.pop()
        page.controls.append()