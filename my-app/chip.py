import flet as ft
class Chip(ft.GestureDetector):
    def __init__(self, left, top):
        self.piece = super().__init__(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=10,
            on_vertical_drag_update=self.drag,
            left = left,
            top =  top,
            content=ft.Container(opacity=0.65, bgcolor=ft.colors.BLUE, width=50, height=50),
        )
    def drag(self, e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()