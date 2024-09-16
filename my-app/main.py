import flet as ft
from bingo import Bingo
from chat import *
from settings import settings_menu
from new_game import new_game_menu

def main(page: ft.Page):
    page.adaptive = True
    
    bingo_game = Bingo(page)
    
    nav_bar = ft.Row(
        controls=[
            ft.ElevatedButton(text="Settings", on_click=lambda e: settings_menu(page, bingo_game)),
            ft.ElevatedButton(text="New Game", on_click=lambda e: new_game_menu(page, bingo_game))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(nav_bar)
    
    layout = ft.Column(controls = [ft.Column(controls=[bingo_game])])
    chat = player_chat(page)
    layout.controls.append(chat)
    
    page.add(layout)
    
# ft.app(target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)