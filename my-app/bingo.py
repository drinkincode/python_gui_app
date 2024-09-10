import flet as ft
import csv
class Bingo(ft.Stack):
    # auto sizing branch init
    def __init__(self, page: ft.Page):
        
        CHIP_TOTAL = 25
        CONTAINER_LENGTH = 50
        
        CONTAINER_LEFT = 50
        
        container_top = 50
        curr_container_left = CONTAINER_LEFT
        
        stack = []
        
        text_list = []
        with open('bingo_words.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                    text_list.append(line)
        
        def on_click(e):
            
            if e.control.bgcolor == "cyan":
                e.control.bgcolor = "amber"
            else:
                e.control.bgcolor = "cyan"
                
            page.update()
            
        count = 0
        
        for i in range(CHIP_TOTAL//5):
            for j in range(CHIP_TOTAL//5):
                slot = ft.Container(
                    content=ft.Text(text_list[count][0]),
                    top=container_top, 
                    bgcolor='cyan',
                    on_click = on_click,
                    left=curr_container_left, 
                    width=CONTAINER_LENGTH,
                    height=CONTAINER_LENGTH, 
                    border=ft.border.all(1)
                )
                stack.append(slot)
                curr_container_left += CONTAINER_LENGTH
                count+=1
            curr_container_left = CONTAINER_LEFT
            container_top += CONTAINER_LENGTH    
        
        super().__init__(stack, width=300, height=300)