import flet as ft
from bingo import Bingo
from utils.menu_utils import *


def new_game_menu(page: ft.Page, bingo_game: Bingo):
    slots_content = "\n".join(bingo_game.get_contents_list())
    text_field = ft.TextField(value=slots_content, multiline=True)

    def save_changes(e):
        new_contents = text_field.value.split("\n")
        
        if len(new_contents) != 25:
            show_notification(page, "Error: The board must have exactly 25 slots.")
            return
        
        # Save the changes to the bingo game
        bingo_game.update_contents(new_contents)
        # Close the change board dialog
        change_board_dialog.open = False
        page.update()
        

    change_board_dialog = ft.AlertDialog(
        title=ft.Text("Change Board"),
        content=ft.ListView(
            controls=[text_field],
            height=200  # Set the height for the scrollable area
        ),
        actions=[
            ft.TextButton("Start New Game", on_click=save_changes)
        ]
    )
    page.dialog = change_board_dialog
    change_board_dialog.open = True
    page.update()
