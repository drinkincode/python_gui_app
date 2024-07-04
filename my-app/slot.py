import flet as ft
class Slot(ft.Container):
    def __init__(self, text, left, top):
        self.peice = ft.Container(
            content=ft.Text(text),
            top=top, 
            left=left, 
            width=50, 
            height=50, 
            border=ft.border.all(1)
        )