import flet as ft
from bingo import Bingo
# from nav import Nav
import csv
from chat import *

def main(page: ft.Page):
    page.adaptive = True
    # page.navigation_bar = Nav()
    bingo_game = Bingo(page)
    layout = ft.Column(controls = [ft.Column(controls=[bingo_game])])
    chat = player_chat(page)
    layout.controls.append(chat)
    
    page.add(layout)
    
ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)