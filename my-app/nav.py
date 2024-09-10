import flet as ft
from settings import Settings
class Nav(ft.CupertinoNavigationBar):
        def __init__(self):
            super().__init__(
                bgcolor=ft.colors.AMBER_100,
                inactive_color=ft.colors.GREY,
                active_color=ft.colors.BLACK,
                on_change=lambda e: print("Selected tab:", e.control.selected_index),
                destinations=[
                    # ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
                    # ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
                    # ft.NavigationBarDestination(
                    #     icon=ft.icons.SETTINGS,
                    #     selected_icon=ft.icons.BOOKMARK,
                    #     label="Settings",
                    # ),
                ]
            )
       
            