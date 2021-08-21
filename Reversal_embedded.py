import pygame
import time

# 클래스 정의
class Reversal:
  def __init__(self, blockpixel, Info_height):
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

  def move(self, coord):
    if self.turn == 'BLACK':
      self.board[coord] %= 10 
      self.board[coord] += 10 
    else:
      self.board[coord] %= 10 
      self.board[coord] += 20 
    self.check_move(coord)

  def check_move(self, coord):
    x = temp_x = coord[0]
    y = temp_y = coord[1]
    to_reverse_set = set()
    # 검은색 돌을 놨다면
    if self.turn == 'BLACK':
      # 위로 검사
      while temp_y>0:
        temp_y -= 1
        if self.board[(x, temp_y)]//10==0:
          break
        elif self.board[(x, temp_y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((x, temp_y))
      # 아래로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_y<7:
        temp_y += 1
        if self.board[(x, temp_y)]//10==0:
          break
        elif self.board[(x, temp_y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((x, temp_y))
      # 왼쪽으로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_x>0:
        temp_x -= 1
        if self.board[(temp_x, y)]//10==0:
          break
        elif self.board[(temp_x, y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((temp_x, y))
      # 오른쪽으로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_x<7:
        temp_x += 1
        if self.board[(temp_x, y)]//10==0:
          break
        elif self.board[(temp_x, y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((temp_x, y))
      # 왼쪽 위로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while min(temp_x, temp_y)>0:
        temp_x -= 1
        temp_y -= 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((temp_x, temp_y))
      # 오른쪽 위로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_y>0 and temp_x<7:
        temp_x += 1
        temp_y -= 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((temp_x, temp_y))
      # 오른쪽 아래로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while max(temp_x, temp_y)<7:
        temp_x += 1
        temp_y += 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((temp_x, temp_y))
      # 왼쪽 아래로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_y<7 and temp_x>0:
        temp_x -= 1
        temp_y += 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==1:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 10
          break
        else:
          to_reverse_set.add((temp_x, temp_y))
        
    # 흰색 돌을 놨다면
    else:
      # 위로 검사
      while temp_y>0:
        temp_y -= 1
        if self.board[(x, temp_y)]//10==0:
          break
        elif self.board[(x, temp_y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((x, temp_y))
      # 아래로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_y<7:
        temp_y += 1
        if self.board[(x, temp_y)]//10==0:
          break
        elif self.board[(x, temp_y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((x, temp_y))
      # 왼쪽으로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_x>0:
        temp_x -= 1
        if self.board[(temp_x, y)]//10==0:
          break
        elif self.board[(temp_x, y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((temp_x, y))
      # 오른쪽으로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_x<7:
        temp_x += 1
        if self.board[(temp_x, y)]//10==0:
          break
        elif self.board[(temp_x, y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((temp_x, y))
      # 왼쪽 위로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while min(temp_x, temp_y)>0:
        temp_x -= 1
        temp_y -= 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((temp_x, temp_y))
      # 오른쪽 위로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_y>0 and temp_x<7:
        temp_x += 1
        temp_y -= 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((temp_x, temp_y))
      # 오른쪽 아래로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while max(temp_x, temp_y)<7:
        temp_x += 1
        temp_y += 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((temp_x, temp_y))
      # 왼쪽 아래로 검사
      temp_x = x
      temp_y = y
      to_reverse_set = set()
      while temp_y<7 and temp_x>0:
        temp_x -= 1
        temp_y += 1
        if self.board[(temp_x, temp_y)]//10==0:
          break
        elif self.board[(temp_x, temp_y)]//10==2:
          for blockcoord in to_reverse_set:
            self.board[blockcoord] = self.board[blockcoord] % 10 + 20
          break
        else:
          to_reverse_set.add((temp_x, temp_y))

  def turn_change(self):
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
  'LT_BROWN': (204, 153, 102)
}
Info_height = 150
origin = (0, Info_height)
blockpixel = 80