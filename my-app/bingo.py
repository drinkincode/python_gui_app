import flet as ft
from utils.csv_utils import write_csv, read_csv
class Bingo(ft.Stack):
    def __init__(self, page: ft.Page):
        chat_bar_top = 800
        chat_bar_left = 1500
        
        self.page = page
        CHIP_TOTAL = 25
        CONTAINER_LENGTH = 75
        # CONTAINER_LENGTH = 50

        
        CONTAINER_LEFT = 10
        
        container_top = 20
        curr_container_left = CONTAINER_LEFT
        
        self.stack = []
        
        text_list = read_csv()[0:CHIP_TOTAL]
        # chip_top = 100
        # chip_left = (CONTAINER_LEFT + chip_top) * (CHIP_TOTAL // 5)    
        
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
                self.stack.append(slot)
                    
                curr_container_left += CONTAINER_LENGTH
                count+=1
            curr_container_left = CONTAINER_LEFT
            container_top += CONTAINER_LENGTH    
        
        super().__init__(self.stack, width=400, height=400)
        page.pubsub.subscribe(self.update_contents)
        
    def get_contents_list(self):
        contents_list = []
        
        for i in range(len(self.stack)):
            slot = self.stack[i]
            slot_text = slot.content.value
            contents_list.append(slot_text)
            
        return contents_list
    
    def update_contents(self, new_contents: list):
        write_csv(new_contents)
        for i in range(len(self.stack)):
            self.stack[i].content.value = new_contents[i]
        self.page.update()
        return True
    
