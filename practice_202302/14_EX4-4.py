# # 【EX4-4 走回原位的機器人】
#
# # 機器人行走一步的指令包括 U、D、L、R 的 4 種內容（均為半型字），
# # 分別代表機器人向上一步（U）, 向下一步（D）, 向左一步（L）, 向右一步（R）。
# # 請判斷機器人走完輸入字串中的所有指令後，是否會正好回到出發點？
#
# # 如果機器人回到原位，輸出「Y」，否則輸出「N」。（均為大寫半型字）
#
# # 輸入：UD            輸出：Y
# # 輸入：LDRRLRUULR    輸出：N
#
# # ---------------------------
#
# # 簡單算法
# word = input()
#
# sum_x = 0
# sum_y = 0
#
# U = word.count('U')
# D = word.count('D')
# L = word.count('L')
# R = word.count('R')
#
# sum_y = U - D
# sum_x = R - L
#
# if sum_x == 0 and sum_y == 0:
#   print('Y')
# else:
#   print('N')
#
# # # 迴歸
# x = 0
# y = 0
# actions = 'UDLR'
#
# for action in actions:
#     if action == 'U':
#         y += 1
#     elif action == 'D':
#         y -= 1
#     elif action == 'L':
#         x -= 1
#     else:
#         x += 1
#
# print(x, y)
#
# # ------------------------------------------
#
# # 方法二
# class Robot:
#   def __init__(self, x: int, y: int, actions: str) -> None:
#     self.x = x
#     self.y = y
#     self.origin_x = x
#     self.origin_y = y
#
#     for action in actions:  # 使用迴圈抓字
#       if action == 'U':
#         self.up()
#       elif action == 'D':
#         self.down()
#       elif action == 'L':
#         self.left()
#       else:
#         self.right()
#
#   def is_origin(self) -> bool:
#     return self.x == self.origin_x and self.y == self.origin_y
#
#   def up(self) -> None:
#     self.y += 1
#
#   def down(self) -> None:
#     self.y -= 1
#
#   def left(self) -> None:
#     self.x -= 1
#
#   def right(self) -> None:
#     self.x += 1
#
#   def __str__(self) -> str:
#     return f'{self.x}, {self.y}'
#
#   def get_location(self) -> str:
#     return f'{self.x}, {self.y}'
#
# # 求出位置_方法1
# print(Robot(0, 0, 'LLLLDDDD'))  # 印出 -4, -4
#
# # 求出位置_方法2
# r = Robot(0, 0, 'LLLLDDDD')
#
# print(r.get_location())  # 印出 -4, -4
#
# # 求出是否回到原點
# print(r.is_origin())  # 印出 False