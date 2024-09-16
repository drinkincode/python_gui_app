import flet as ft

def show_notification(page: ft.Page, message: str):
    snackbar = ft.SnackBar(
        content=ft.Text(message),
        action="OK"
    )
    page.snack_bar = snackbar
    snackbar.open = True
    page.update()

def close_menu(page: ft.Page, menu_dialog: ft.AlertDialog, confirm_dialog: ft.AlertDialog):
    confirm_dialog.open = False
    menu_dialog.open = False
    page.update()
    show_notification(page, "menu closed successfully.")

def confirm_close(page: ft.Page, menu_dialog: ft.AlertDialog):
    confirm_dialog = ft.AlertDialog(
        title=ft.Text("Confirm Close"),
        content=ft.Text("Are you sure you want to close the menu?"),
        actions=[
            ft.TextButton("Yes", on_click=lambda e: close_menu(page, menu_dialog, confirm_dialog)),
            ft.TextButton("No", on_click=lambda e: setattr(confirm_dialog, 'open', False))
        ]
    )
    page.dialog = confirm_dialog
    confirm_dialog.open = True
    page.update()
