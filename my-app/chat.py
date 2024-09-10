import flet as ft


class Message:
    def __init__(self, user: str, text: str, message_type: str):
        self.user = user
        self.text = text
        self.message_type = message_type



def player_chat(page: ft.Page):
    border = ft.Column(
        auto_scroll=True
    )
    chat = ft.ListView(expand=0, spacing=10, padding=20, auto_scroll=True, height=200)
    new_message = ft.TextField()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        elif message.message_type == "login_message":
            chat.controls.append(
                ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
            )
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(
            Message(
                user=page.session.get("user_name"),
                text=new_message.value,
                message_type="chat_message",
            )
        )
        new_message.value = ""
        page.update()

    user_name = ft.TextField(label="Enter your name")

    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Name cannot be blank!"
            user_name.update()
        else:
            page.session.set("user_name", user_name.value)
            page.dialog.open = False
            page.pubsub.send_all(
                Message(
                    user=user_name.value,
                    text=f"{user_name.value} has joined the chat.",
                    message_type="login_message",
                )
            )
            page.update()

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([user_name], tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end",
    )
    chat_bar = ft.Row(
        controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)],

    )
    border.controls.append(chat)
    player_chat = ft.Column(controls=[border, chat_bar])

    return player_chat
    


# ft.app(target=main)