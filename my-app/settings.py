import flet as ft
from bingo import Bingo
def show_notification(page: ft.Page, message: str):
    snackbar = ft.SnackBar(
        content=ft.Text(message),
        action="OK"
    )
    page.snack_bar = snackbar
    snackbar.open = True
    page.update()

def close_settings(page: ft.Page, settings_dialog: ft.AlertDialog, confirm_dialog: ft.AlertDialog):
    confirm_dialog.open = False
    settings_dialog.open = False
    page.update()
    show_notification(page, "Settings menu closed successfully.")

def confirm_close(page: ft.Page, settings_dialog: ft.AlertDialog):
    confirm_dialog = ft.AlertDialog(
        title=ft.Text("Confirm Close"),
        content=ft.Text("Are you sure you want to close the settings menu?"),
        actions=[
            ft.TextButton("Yes", on_click=lambda e: close_settings(page, settings_dialog, confirm_dialog)),
            ft.TextButton("No", on_click=lambda e: setattr(confirm_dialog, 'open', False))
        ]
    )
    page.dialog = confirm_dialog
    confirm_dialog.open = True
    page.update()


def show_change_board_dialog(page: ft.Page, bingo_game: Bingo):
    slots_content = "\n".join(bingo_game.contents_list)
    text_field = ft.TextField(value=slots_content, multiline=True)

    def save_changes(e):
        new_contents = text_field.value.split("\n")
        if len(new_contents) != 25:
            show_notification(page, "Error: The board must have exactly 24 slots.")
            return
        # Save the changes to the bingo game
        bingo_game.contents_list = new_contents
        # Close the change board dialog
        change_board_dialog.open = False
        page.update()
        # Reopen the settings menu
        settings_menu(page, bingo_game)

    change_board_dialog = ft.AlertDialog(
        title=ft.Text("Change Board"),
        content=ft.ListView(
            controls=[text_field],
            height=200  # Set the height for the scrollable area
        ),
        actions=[
            ft.TextButton("Save and Close", on_click=save_changes)
        ]
    )
    page.dialog = change_board_dialog
    change_board_dialog.open = True
    page.update()


def settings_menu(page: ft.Page, bingo_game: Bingo):
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
                ), 
                ft.Text("Slots Content"),
                # ft.Container(
                #     content=ft.ListView(
                #         controls=[
                #             ft.TextField(value="\n".join(bingo_game.contents_list), multiline=True)
                #         ],
                #         height=200  # Set the height for the scrollable area
                #     )
                # ),
                ft.TextButton("Change Board", on_click=lambda e: show_change_board_dialog(page, bingo_game))
            ]
        ),
        actions=[
            ft.TextButton("Close", on_click=lambda e: confirm_close(page, settings_dialog))
        ]
    )
    page.dialog = settings_dialog
    settings_dialog.open = True
    page.update()