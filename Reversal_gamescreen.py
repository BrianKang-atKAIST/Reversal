import pygame
import time
from Reversal_embedded import *

# 객체 생성
Reversalgame = Reversal(80)

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen = pygame.display.set_mode((Reversalgame.screen_width, Reversalgame.screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Reversal')

# 함수 정의
def draw_background():
  pygame.draw.rect(screen, color_dict['GREEN'], [0, 0, Reversalgame.screen_width, Reversalgame.screen_height])

def draw_board(origin=tuple):
  origin_x = origin[0]
  origin_y = origin[1]
  for (coord, info) in Reversalgame.board.items():
    if info//10 == 1:
      stone = 'BLACK'
    elif info//10 == 2:
      stone = 'WHITE'
    else:
      continue
    x = origin_x + (coord[0]+0.5)* Reversalgame.blockpixel
    y = origin_y + (coord[1]+0.5) * Reversalgame.blockpixel
    pygame.draw.circle(screen, color_dict[stone], (x, y), 30)
# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가? 를 체크
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
      running = False # 게임이 진행중이 아님

  draw_background()
  draw_board(origin=origin)
  # print(pygame.mouse.get_pressed())

  if pygame.mouse.get_pressed() == (True, False, False):
    click_x, click_y = pygame.mouse.get_pos()
    click_x -= origin[0]
    click_y -= origin[1]
    click_x //= Reversalgame.blockpixel
    click_y //= Reversalgame.blockpixel
    if Reversalgame.board[(click_x, click_y)]//10 == 0:
      Reversalgame.move((click_x, click_y))
      Reversalgame.turn_change()


  pygame.display.update()

# pygame 종료
pygame.quit()