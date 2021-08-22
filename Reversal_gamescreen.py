import pygame
import time
from Reversal_embedded import *

# 객체 생성
Reversalgame = Reversal(blockpixel, Info_height)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen = pygame.display.set_mode((Reversalgame.screen_width, Reversalgame.screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Reversal')

# 함수 정의
def draw_background():
  pygame.draw.rect(screen, color_dict['GREEN'], [0, 0, Reversalgame.screen_width, Reversalgame.screen_height])

def draw_stone(stone, coord, radius):
  pygame.draw.circle(screen, color_dict[stone], coord, radius)

def draw_block(color, coord, width, height):
  pygame.draw.rect(screen, color_dict[color], [coord[0], coord[1], width, height])

def draw_Word(font, word, color, center):
  text = font.render(word, True, color)
  text_rect =text.get_rect(center=center)
  screen.blit(text, text_rect)

def draw_Info():
  blackscore = Reversalgame.blackscore
  whitescore = Reversalgame.whitescore
  turn = Reversalgame.turn
  draw_Word(font_dict['BLACKSCORE'], str(blackscore), color_dict['RED'], (20, 30))
  draw_Word(font_dict['WHITESCORE'], str(whitescore), color_dict['BLUE'], (620, 30))
  draw_Word(font_dict['TURN'], str(turn)+"'s turn", color_dict[turn], (310, 30))


def draw_board(origin=tuple):
  origin_x = origin[0]
  origin_y = origin[1]
  for (coord, info) in Reversalgame.board.items():
    block_x = origin_x + coord[0] * blockpixel
    block_y = origin_y + coord[1] * blockpixel
    if info%1000 // 100 == 1:
      color = 'CREAMY_PURPLE'
    elif info%10000 // 1000 == 1:
      color = 'PALE_YELLOW'
    elif (coord[0]+coord[1]) % 2 == 0:
      color = 'BROWN'
    else:
      color = 'LT_BROWN'
    draw_block(color, (block_x, block_y), blockpixel, blockpixel)
    if (info%100)//10 == 1:
      stone = 'BLACK'
    elif (info%100)//10 == 2:
      stone = 'WHITE'
    else:
      continue
    circle_x = origin_x + (coord[0]+0.5) * blockpixel
    circle_y = origin_y + (coord[1]+0.5) * blockpixel
    draw_stone(stone, (circle_x, circle_y), 30)
  if Reversalgame.coord_out_of_range(Reversalgame.mouseon_coord):
    mouse_x = origin_x + (Reversalgame.mouseon_coord[0]+0.5) * blockpixel
    mouse_y = origin_y + (Reversalgame.mouseon_coord[1]+0.5) * blockpixel
    draw_stone('DIM_' + Reversalgame.turn, (mouse_x, mouse_y), 30)

# 상수 정의
font_dict = {
  'BLACKSCORE': pygame.font.Font(None, 40),
  'WHITESCORE': pygame.font.Font(None, 40),
  'TURN': pygame.font.Font(None, 40),
}

# 이벤트 루프
def main():
  running = True # 게임이 진행중인가?
  while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가? 를 체크
      if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
        running = False # 게임이 진행중이 아님

    draw_background()
    # print(pygame.mouse.get_pressed())

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x -= origin[0]
    mouse_y -= origin[1]
    mouse_x //= blockpixel
    mouse_y //= blockpixel
    try:
      Reversalgame.predict_result((mouse_x, mouse_y))
    except KeyError:
      pass

    if pygame.mouse.get_pressed() == (True, False, False):
      click_x, click_y = pygame.mouse.get_pos()
      click_x -= origin[0]
      click_y -= origin[1]
      click_x //= blockpixel
      click_y //= blockpixel
      try:
        if (Reversalgame.board[(click_x, click_y)]%100)//10 == 0:
          Reversalgame.move((click_x, click_y))
          Reversalgame.turn_change()
          # time.sleep(0.5)
      except KeyError:
        print('Out of board')
        time.sleep(0.5)
      else:
        # print(Reversalgame.board[(click_x, click_y)])
        pass

    if Reversalgame.moves == 64:
      if Reversalgame.blackscore > Reversalgame.whitescore:
        print('BLACK WIN')
      elif Reversalgame.blackscore < Reversalgame.whitescore:
        print('WHITE WIN')
      else:
        print('DRAW GAME')
      Reversalgame.moves = 0

    draw_board(origin=origin)
    draw_Info()


    pygame.display.update()

  # pygame 종료
  pygame.quit()

if __name__== '__main__':
  main()