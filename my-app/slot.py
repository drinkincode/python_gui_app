# import asyncio
# import flet as ft

# class SlotHandler(ft.Container):
#     def __init__(self, text, left, top):
        
#         self.slot = ft.Container(
#             content=ft.Text(text),
#             top=top, 
#             bgcolor='red',
#             ink = False,
#             animate=ft.animation.Animation(1000, "bounceOut"),
#             # on_tap_down = on_tap_down(),
#             left=left, 
#             width=50, 
#             height=50, 
#             border=ft.border.all(1)
#         )
#         async def animate_container(e):
#             self.slot.bgcolor = "blue" if self.slot.bgcolor == "red" else "red"
#             await self.slot.update_async()
           
import flet as ft

name = "Animate container"


def example():
    c = ft.Container(
        width=200,
        height=200,
        bgcolor="red",
        animate=ft.animation.Animation(1000, "bounceOut"),
    )

    async def animate_container(e):
        c.width = 100 if c.width == 200 else 200
        c.height = 100 if c.height == 200 else 200
        c.bgcolor = "blue" if c.bgcolor == "red" else "red"
        await c.update_async()

    return ft.Column(
        controls=[c, ft.ElevatedButton("Animate container", on_click=animate_container)]
    )