import flet as ft
from bingo import Bingo
# from nav import Nav
import csv
from chat import *
def confirm_close(page: ft.Page, settings_dialog: ft.AlertDialog):
    confirm_dialog = ft.AlertDialog(
        title=ft.Text("Confirm Close"),
        content=ft.Text("Are you sure you want to close the settings menu?"),
        actions=[
            ft.TextButton("Yes", on_click=lambda e: close_settings(page, settings_dialog, confirm_dialog)),
            ft.TextButton("No", on_click=lambda e: confirm_dialog.close())
        ]
    )
    page.dialog = confirm_dialog
    confirm_dialog.open = True
    page.update()

def close_settings(page: ft.Page, settings_dialog: ft.AlertDialog, confirm_dialog: ft.AlertDialog):
    confirm_dialog.close()
    settings_dialog.close()
    page.update()

def settings_menu(page: ft.Page):
    settings_dialog = ft.AlertDialog(
        title=ft.Text("Settings"),
        content=ft.Column(
            controls=[
                ft.Text("Option 1"),
                ft.Switch(label="Enable Option 1"),
                ft.Text("Option 2"),
                ft.Switch(label="Enable Option 2"),
                ft.Text("Select an option"),
                ft.Dropdown(
                    options=[
                        ft.dropdown.Option("Option A"),
                        ft.dropdown.Option("Option B"),
                        ft.dropdown.Option("Option C")
                    ],
                    label="Dropdown Menu"
                )
            ]
        ),
        actions=[
            ft.TextButton("Close", on_click=lambda e: confirm_close(page, settings_dialog))
        ]
    )
    page.dialog = settings_dialog
    settings_dialog.open = True
    page.update()

def main(page: ft.Page):
    page.adaptive = True

    nav_bar = ft.Row(
        controls=[
            ft.ElevatedButton(text="Settings", on_click=lambda e: settings_menu(page)),
            ft.ElevatedButton(text="New Game", on_click=lambda e: print("New Game clicked"))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(nav_bar)
    bingo_game = Bingo(page)
    layout = ft.Column(controls = [ft.Column(controls=[bingo_game])])
    chat = player_chat(page)
    layout.controls.append(chat)
    
    page.add(layout)
    
# ft.app(target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)