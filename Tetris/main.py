# 1일차 목표: 블럭 생성후 화살표로 이동
# 2일차 목표: 테트리스 틀, 격자 생성 + 키 한번에 한칸씩 이동하게 설정하기
import pygame
import os

xPos = 900
yPos = 70
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{xPos},{yPos}"

pygame.init() # 초기화
screen = pygame.display.set_mode((460, 740))
clock = pygame.time.Clock()
running = True

# Settings
defRect = (100, 100, 100, 100)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
gravity = 0.8

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    screen.fill("white")
    pygame.draw.rect(screen, "black", (player_pos.x, player_pos.y, 30, 30))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not player_pos.y < 10:
        player_pos.y -= 30 
    if keys[pygame.K_DOWN] and not player_pos.y > 720:
        player_pos.y += 30
    if keys[pygame.K_LEFT] and not player_pos.x < 10:
        player_pos.x -= 30
    if keys[pygame.K_RIGHT] and not player_pos.x > 430:
        player_pos.x += 30
    if keys[pygame.K_r]:
        pygame.init()
        print("Sdf")

    pygame.display.flip() # 화면업데이트트
    clock.tick(20)  # limits FPS to 60

pygame.quit()