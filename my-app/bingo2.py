import flet as ft
from utils.csv_utils import write_csv, read_csv
from utils.bingo_utils import chunks


ALIGHMENT = ft.alignment.center
SQUARE_SIZE = 50
COLOR = ft.colors.AMBER
COLOR_CLICKED = ft.colors.CYAN
BORDER_RADIUS = 1

class Card_Square(ft.Container):
    def __init__(self, text: str, dyn_square_size=SQUARE_SIZE):
        self.clicked = False
        super().__init__(
            content=[ft.Text(text)],
            alignment=ALIGHMENT,
            width=dyn_square_size,
            height=dyn_square_size,
            bgcolor='amber',
            border_radius=ft.border_radius.all(BORDER_RADIUS)
        )
    
    def update_content(self, text: str) -> bool:
        self.content.value = text
        return True
    


class BingoRow(ft.Row):   
    def __init__(self, page: ft.Page, csv_path: str='bingo_words.csv', spacing=0, run_spacing=10):
        self.text_list = read_csv(csv_path)
        
        # dyn_square_size = page.window_width / 5
        def on_click(e):
            
            if e.control.bgcolor == "cyan":
                e.control.bgcolor = "amber"
            else:
                e.control.bgcolor = "cyan"
            
            page.update()
            
        content = []
        
        for text in range(len(self.text_list)):
            content.append(Card_Square(str(text)))
            content[-1].on_click = on_click
        
        super().__init__(
            wrap=True,
            spacing=0,
            run_spacing = 0,
            # run_spacing=SQUARE_SIZE + 10,
            tight=True,
            controls=content,
            width=SQUARE_SIZE * 5,
            height=SQUARE_SIZE* 5
        )
    
    def update_content(self, new_text_list: list[str]) -> bool:
        i = 0
        for square in self.controls:
            square.update_content(new_text_list[i])
            i+=1
        self.text_list = new_text_list
        write_csv(new_text_list)
        self.update()
        return True
    



# class Bingo(ft.Container):
#     def __init__(self, text_list: list[str]):
#         self.text_list =text_list
        
#         row_2d_list = chunks(text_list, 5)
        
#         bingo_controls = []
#         for row in row_2d_list:
#             bingo_controls.append(BingoRow(row))
            
#         super().__init__(
#             content=bingo_controls
#         )

#     def get_content(self):
#         return self.text_list
    
#     def update_content(self, new_contents: list):
#         write_csv(new_contents)
#         for i in range(len(self.stack)):
#             self.stack[i].content.value = new_contents[i]
#         return True