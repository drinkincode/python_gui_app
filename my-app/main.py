import flet as ft
from chip import Chip
from slot import Slot


def main(page: ft.Page):
    CHIP_TOTAL = 25
    stack = []
    text_list = ['take a sip', 'take a sip', 'take a sip', 'take a sip', 'take a sip',
                 'take a sip', 'take a sip', 'take a sip', 'take a sip', 'take a sip', 
                 'take a sip', 'take a sip', 'Free', 'take a sip', 'take a sip', 
                 'take a sip', 'take a sip', 'take a sip', 'take a sip', 'take a sip',
                 'take a sip', 'take a sip', 'take a sip', 'take a sip', 'take a sip'
                ]
    
    board_top = 200
    board_left = 150
    count = 0
    for i in range(CHIP_TOTAL//5):
        for j in range(CHIP_TOTAL//5):
            slot = ft.Container(
                content=ft.Text(text_list[count]),
                top=board_top, 
                left=board_left, 
                width=50, 
                height=50, 
                border=ft.border.all(1)
            )
            stack.append(slot)
            board_left += 150
            count+=1
        board_top += 150    
        board_left = 150
        
    for i in range(CHIP_TOTAL):
        chip = Chip()
        stack.append(chip)
        
    page.add( ft.Stack(stack, width=1000, height=1000))

ft.app(target=main)