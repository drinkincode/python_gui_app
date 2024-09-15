import flet as ft

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