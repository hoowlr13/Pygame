# 할일 목록
# drop구현 -> pygame에서 pg.event활용?
# 한번 움직일때마다 블럭 순회돌며 이동할수있는지 확인-> on_block에서 이동하기전 다음위치 확인하기
import pygame as pg
from pygame.locals import *
import os, time, random
from typing import List

# -- 테트리스 블럭 설정 -- 
BLOCK_SIZE = (20, 20)

# -- 테트리스 블럭 색깔 설정 --
BLOCK_COLOR = {
    "BLUE": (0,0,255),
    "YELLOW": (255,255,0),
    "PURPLE": (128,0,128),
    "RED": (255,0,0),
    "GREEN": (0,128,0)
}
BLOCK_COLOR_RANDOM = random.choice(list(BLOCK_COLOR))

# -- 테트리스 보드 설정 -- 
FILLED_SIZE = 10, 20
SCREEN_SIZE = 400, 800
SCREEN_POS = SCREEN_POS_X , SCREEN_POS_Y = 900, 50

class Tetrimino:
    def __init__(self, name:str, block:List[List], color:tuple):
        self.name = name
        self.block = block
        self.color = color
class App:
    def __init__(self): 
        # -- 게임시작 기본설정 --
        self._running = True
        self._display_surf = None
        self.SCREEN_SIZE = self.SCREEN_X, self.SCREEN_Y = SCREEN_SIZE

        # -- 필드 기본설정 --
        self.FILLED = self.FILLED_X, self.FILLED_Y = FILLED_SIZE
        self.FILLED_EMPTY = 0
        self.FILLED_FULL = 1
        self.board_state = [[self.FILLED_EMPTY for _ in range(self.FILLED_X)] for _ in range(self.FILLED_Y)] 

        # -- 블럭 기본설정 --
        self.BLOCK = self.BLOCK_X, self.BLOCK_Y = 20, 20
        self.BLOCK_CURRENT = None 
        self.mino = [
            Tetrimino("I", [[-2,0], [-1,0], [0,0], [1,0]], BLOCK_COLOR_RANDOM),
            Tetrimino("O", [[-1,-1], [0,-1], [-1,0], [0,0]], BLOCK_COLOR_RANDOM),
            Tetrimino("L", [[1,-1], [-1,0], [0,0], [1,0]], BLOCK_COLOR_RANDOM),
            Tetrimino("S", [[0,-1], [1,-1], [-1,0], [0,0]], BLOCK_COLOR_RANDOM),            
            Tetrimino("J", [[-1,-1], [-1,0], [0,0], [1,0]], BLOCK_COLOR_RANDOM),
            Tetrimino("Z", [[-1,-1], [0,-1], [0,0], [1,0]], BLOCK_COLOR_RANDOM),
            Tetrimino("T", [[0,-1], [-1,0], [0,0], [1,0]], BLOCK_COLOR_RANDOM)]
        

        self.BLOCK_MOVE = self.BLOCK_MOVE_X, self.BLOCK_MOVE_Y = 20, 20
    
        self.curren_piece = self.board_state[0][0]

        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{SCREEN_POS_X},{SCREEN_POS_Y}"

     

    def on_init(self):
        pg.init() # 초기화
        self._display_surf = pg.display.set_mode(self.SCREEN_SIZE, pg.HWSURFACE | pg.DOUBLEBUF, vsync=1)
        self._running = True

        

    def on_event(self, event): # 
        if event.type == pg.QUIT:
            self._running = False

        keys = pg.key.get_pressed()

        if event.type == pg.KEYDOWN: 
            if keys[pg.K_LEFT] and self.BLOCK_MOVE_X > 0:

                self.BLOCK_MOVE_X -= 20
            elif keys[pg.K_RIGHT] and self.BLOCK_MOVE_X < 180:
                self.BLOCK_MOVE_X += 20
                
            elif keys[pg.K_DOWN]:
                self.BLOCK_MOVE_Y += 20
        

    def on_filled(self, width = int, height = int): # 테트리스 보드 그리기 

        for i in range(width):
            for j in range(height):
                newRect = pg.Rect(i*self.BLOCK_X, j*self.BLOCK_Y, self.BLOCK_X, self.BLOCK_Y)   
                pg.draw.rect(self._display_surf, "black", newRect, 1) 


    def on_block(self, block_x, block_y): # 테트리스 이동시키는 함수
        if self.BLOCK_CURRENT is None:
            self.BLOCK_CURRENT = random.choice(self.mino)
        
        if self.BLOCK_CURRENT is not None: 
            for block_pos in self.BLOCK_CURRENT.block:
                x = (block_pos[0] + self.BLOCK_MOVE_X // self.BLOCK_X) * self.BLOCK_X
                y = (block_pos[1] + self.BLOCK_MOVE_Y // self.BLOCK_Y) * self.BLOCK_Y
                now_draw = pg.Rect(x, y, self.BLOCK_X, self.BLOCK_Y)
                pg.draw.rect(self._display_surf, self.BLOCK_CURRENT.color, now_draw)
   
        # if time.perf_counter() > self.block_down + 1: # 수정필요
        #     self.BLOCK_MOVE_Y += 20
        #     self.block_down = time.perf_counter()
    

    def on_loop(self):
        pass

    def on_render(self):
        if (self.BLOCK_MOVE_Y//20) > 20:
            self.BLOCK_MOVE_Y += 20
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
                
            self.on_filled(self.FILLED_X, self.FILLED_Y)
           
            self.on_block(self.BLOCK_X, self.BLOCK_Y)
    

            self.on_loop()
            self.on_render()
        self.on_cleanup()


    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()


