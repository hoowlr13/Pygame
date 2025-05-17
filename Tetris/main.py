import pygame as pg
from pygame.locals import *
import os, time, random

# 테트리스는 가로 10 세로 40의 크기로 구성됨
# 한 칸의 크기는 가로 20 세로 20으로 구성됨
# 화면의 크기는 200, 800으로 구성
# 
class App:
    def __init__(self): # 여기에 사용할 변수, 함수등 다넣어놓고 사용
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 400, 800
        self.board_x, self.board_y = 10, 20
        self.EMPTY_board = 0
        self.FILL_board = 1
        self.board_state = [[self.EMPTY_board for _ in range(self.board_x)] for _ in range(self.board_y)] # 보드에있는 x, y를 격자 그리드로 설정하고 
        self.bweight, self.bheight = (20, 20)

        self.curren_piece = True # 나중에 블럭의 모양으로 변경경
        self.block_check = False
        # 보드의 상태를 나타내는 그리드 완성 후 키보드로 이동하며 블록이 격자안에 채워지면 상태 바꾸기
        
        self.move = self.moveX, self.moveY = (0, 0)
        self.curren_piece = self.board_state[0][0]

        xPos = 900
        yPos = 50
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{xPos},{yPos}"

     

    def on_init(self): #
        pg.init() # 초기화
        self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF, vsync=1)
        self._running = True

        

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False


        keys = pg.key.get_pressed()
        if event.type == pg.KEYDOWN: # 연속으로 입력되는 문제 o
            if keys[pg.K_LEFT] and self.moveX > 0:

                self.board_state[1][2] = self.FILL_board
                self.moveX -= 20
                print(f"{self.moveX} {self.moveY}")
            elif keys[pg.K_RIGHT] and self.moveX < 180:
                self.moveX += 20
                
            elif keys[pg.K_DOWN]:
                self.moveY += 20
                print(self.board_state[(self.moveY//20)-2][(self.moveX//20)-2])
            self.board_state[(self.moveY//20)-1][(self.moveX//20)-1] = self.FILL_board
        
        


# key값을 return받아서 on_block에서 블럭을 이동
# 리턴을 어떻게 받아야할까


    def on_board(self, width = int, height = int): # 테트리스 보드 그리기 
        self.bsize = self.bweight, self.bheight 

        for i in range(10):
            for j in range(20):
                newRect = pg.Rect(i*self.bweight, j*self.bheight, self.bweight, self.bheight)   
                pg.draw.rect(self._display_surf, "black", newRect, 1) # 그다음부터가 


    def on_block(self, event, bweight, bheight): # 테트리스 이동시키는 함수
        self.current_type_rect = None # 현재 출력할 블록저장
        block_type = ["I", "O"]
        
        """"Z": 3,
            "S": 4,
            "J": 5,
            "L": 6,
            "T": 7"""
        
        
        if not self.block_check:
            select = random.choice(block_type)
            self.block_check = True
            self.current_type = select
        

        if self.current_type == "I":
            self.current_type_rect = pg.Rect(self.moveX, self.moveY, bweight, bheight*4)
        elif self.current_type == "O":
            self.current_type_rect = pg.Rect(self.moveX, self.moveY, bweight*2, bheight*2)

        if self.current_type_rect: # draw
            pg.draw.rect(self._display_surf, "blue", self.current_type_rect)
            self.curren_piece = self.current_type

        # 이 height가 0이될때까지 아래로 이동
        # if not self.curren_piece:
         

    def on_loop(self):
        pass

    def on_render(self):
        if (self.moveY//20) > 20:
            self.moveY += 20
        pg.display.flip()

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self._display_surf.fill("white")
            
            for event in pg.event.get():
                self.on_event(event)
                
            self.on_board()
           
            self.on_block(event, self.bweight, self.bheight)
            self.curren_piece = True

            self.on_loop()
            self.on_render()
        self.on_cleanup()


    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()


