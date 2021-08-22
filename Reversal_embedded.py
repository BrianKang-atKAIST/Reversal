import pygame
import time

# 클래스 정의
class Reversal:
  def __init__(self, blockpixel, Info_height) -> None:
    '''Reversal 클래스의 init 함수'''
    self.board = {(x, y): 0 if (x+y)%2==1 else 1 for x in range(8) for y in range(8)}
    self.board[(3, 3)] += 10
    self.board[(3, 4)] += 20
    self.board[(4, 3)] += 20
    self.board[(4, 4)] += 10
    self.turn = 'BLACK'
    self.blockpixel = blockpixel
    self.screen_width = self.blockpixel * 8
    self.screen_height = self.blockpixel * 8 + Info_height
    self.Info_height = Info_height
    self.moves = 4
    self.blackscore = 2
    self.whitescore = 2
    # 마지막 수를 표현하기 위한 상수. 아직 수를 두지 않아 False 상태이다.
    self.last_move_coord = False
    # 마우스 위치에 두었을 때 뒤집히는 돌들을 표시하기 위한 상수
    self.mouseon_coord = (0, 0)
    self.predict_result_set = set()

  def move(self, coord) -> None:
    if self.turn == 'BLACK':
      self.board[coord] %= 10 
      self.board[coord] += 10 
    else:
      self.board[coord] %= 10 
      self.board[coord] += 20 
    to_reverse_set = self.check_move(coord)
    for blockcoord in to_reverse_set:
      self.reverse_stone(blockcoord)
    self.moves += 1
    if self.turn == 'BLACK':
      self.blackscore += 1
    else:
      self.whitescore += 1
    if self.last_move_coord:
      self.board[self.last_move_coord] -= 1000
    self.last_move_coord = coord
    self.board[self.last_move_coord] += 1000

  def check_move(self, coord) -> set:
    x = coord[0]
    y = coord[1]
    to_reverse_set = set()
    # 위로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_UP = set()
    while temp_y>0:
      temp_y -= 1
      if self.board[(x, temp_y)]//10==0:
        break
      elif self.board[(x, temp_y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_UP
        break
      else:
        to_reverse_set_UP.add((x, temp_y))
    # 아래로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_DOWN = set()
    while temp_y<7:
      temp_y += 1
      if self.board[(x, temp_y)]//10==0:
        break
      elif self.board[(x, temp_y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_DOWN
        break
      else:
        to_reverse_set_DOWN.add((x, temp_y))
    # 왼쪽으로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_LEFT = set()
    while temp_x>0:
      temp_x -= 1
      if self.board[(temp_x, y)]//10==0:
        break
      elif self.board[(temp_x, y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_LEFT
        break
      else:
        to_reverse_set_LEFT.add((temp_x, y))
    # 오른쪽으로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_RIGHT = set()
    while temp_x<7:
      temp_x += 1
      if self.board[(temp_x, y)]//10==0:
        break
      elif self.board[(temp_x, y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_RIGHT
        break
      else:
        to_reverse_set_RIGHT.add((temp_x, y))
    # 왼쪽 위로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_UPLEFT = set()
    while min(temp_x, temp_y)>0:
      temp_x -= 1
      temp_y -= 1
      if self.board[(temp_x, temp_y)]//10==0:
        break
      elif self.board[(temp_x, temp_y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_UPLEFT
        break
      else:
        to_reverse_set_UPLEFT.add((temp_x, temp_y))
    # 오른쪽 위로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_RIGHTUP = set()
    while temp_y>0 and temp_x<7:
      temp_x += 1
      temp_y -= 1
      if self.board[(temp_x, temp_y)]//10==0:
        break
      elif self.board[(temp_x, temp_y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_RIGHTUP
        break
      else:
        to_reverse_set_RIGHTUP.add((temp_x, temp_y))
    # 오른쪽 아래로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_DOWNRIGHT = set()
    while max(temp_x, temp_y)<7:
      temp_x += 1
      temp_y += 1
      if self.board[(temp_x, temp_y)]//10==0:
        break
      elif self.board[(temp_x, temp_y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_DOWNRIGHT
        break
      else:
        to_reverse_set_DOWNRIGHT.add((temp_x, temp_y))
    # 왼쪽 아래로 검사
    temp_x = x
    temp_y = y
    to_reverse_set_DOWNLEFT = set()
    while temp_y<7 and temp_x>0:
      temp_x -= 1
      temp_y += 1
      if self.board[(temp_x, temp_y)]//10==0:
        break
      elif self.board[(temp_x, temp_y)]//10==stone_dict[self.turn]:
        to_reverse_set |= to_reverse_set_DOWNLEFT
        break
      else:
        to_reverse_set_DOWNLEFT.add((temp_x, temp_y))

    return to_reverse_set

  def reverse_stone(self, coord) -> None:
    if self.turn == 'BLACK':
      self.board[coord] -= 10
      self.blackscore += 1
      self.whitescore -= 1
    else:
      self.board[coord] += 10
      self.whitescore += 1
      self.blackscore -= 1

  def predict_result(self, coord):
    if self.mouseon_coord == coord:
      return
    else:
      for predict_coord in self.predict_result_set:
        self.board[predict_coord] -= 100
      self.mouseon_coord = coord
      self.predict_result_set = set()
      if (self.board[self.mouseon_coord]%100)//10 != 0:
        return
      self.predict_result_set = self.check_move(coord)
      for predict_coord in self.predict_result_set:
        self.board[predict_coord] += 100

  def coord_out_of_range(self, coord) -> bool:
    if coord[0] < 0 or coord[1] < 0 or coord[0] > 7 or coord[1] > 7:
      return False
    if (self.board[coord]%100) // 10 != 0:
      return False
    return True
    
  def turn_change(self) -> None:
    if self.turn == 'BLACK':
      self.turn = 'WHITE'
    else:
      self.turn = 'BLACK'

# 함수 정의

# 상수 정의
color_dict = {
  'BLACK': (0, 0, 0),
  'WHITE': (255, 255, 255),
  'RED': (255, 0, 0),
  'GREEN': (0, 255, 0),
  'BLUE': (0, 0, 255),
  'BROWN': (153, 102, 000),
  'LT_BROWN': (204, 153, 102),
  'CREAMY_PURPLE': (204, 153, 255),
  'PALE_YELLOW': (255, 204, 102),
  'DIM_BLACK': (51, 51, 51),
  'DIM_WHITE': (204, 204, 204)
}
stone_dict = {'BLACK': 1, 'WHITE': 2, 'DIM_BLACK': 3, 'DIM_WHITE': 4}
Info_height = 150
origin = (0, Info_height)
blockpixel = 80