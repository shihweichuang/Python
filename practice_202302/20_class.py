# # 【Class 物件導向】
#
# # 定義
# class Chair():
#     pass
#
# # 根據上面所定義的說明文件，真正的做出多個物件的實體
# a_chair = Chair()      # a_chair為一物件
# b_chair = Chair()      # b_chair為一物件
#
# print(a_chair)       # 印出 <__main__.Chair object at 0x000001C254F1B400>
# print(b_chair)       # 印出 <__main__.Chair object at 0x000001C254EF9640>
#
# # 只能列印出物件位置，沒有太大幫助
#
# # -------------------------------------------------
#
# # 【指定屬性(特色)】
#
# class Chair():
#     pass
#
# a_chair = Chair()
# a_chair.color = "Green"
#
# b_chair = Chair()
# b_chair.color = "Red"
#
# print(a_chair.color)    # 印出 Green
# print(b_chair.color)    # 印出 Red
#
# # --------------------------------------------------
#
# # 【初始化】
#
# # 【初始化的函式】
#
# def __init__(self):
#     pass
#
# class Chair():
#     def __init__(self):
#       pass
#
# # ---------------------------------------------------
#
# # 【指定想要初始化的屬性】
#
# class Chair():
#     def __init__(self, color):
#         self.color = color
#
# a_chair = Chair("Green")  # 將變數帶入至color
# b_chair = Chair("Red")
#
# print(a_chair.color)      # 印出 Green
# print(b_chair.color)      # 印出 Red
#
# # ---------------------------------------------------
#
# # 【物件的特有方法】
#
# class Chair():
#     def __init__(self, color: str) -> None:
#         self.color = color
#
#     def seat(self) -> None:
#         print(f"{self.color}椅子很好坐")
#
# a_chair = Chair("Green")
# b_chair = Chair("Red")
#
# a_chair.seat()           # 印出 Green 椅子很好坐
# b_chair.seat()           # 印出 Red 椅子很好坐
#
# # ---------------------------------------------------------
#
# class Chair():
#     def __init__(self, color: str) -> None:
#         self.color = color
#
#     def seat(self) -> None:
#         print(f'{self.color}椅子很好坐')
#
# a_chair = Chair("Green")
# b_chair = Chair("Red")
#
# print(a_chair) # 印出 <main.Chair object at 0x7f2fd00cae60>
# print(b_chair) # 印出 <main.Chair object at 0x7f2fd00cb790>
#
# # -----------------------------------------------------------
#
# # 【新增def __str__(self)：列印字串用】
#
# class Chair():
#     def __init__(self, color: str) -> None:
#       self.color = color
#
#     def seat(self) -> None:
#         print(f'{self.color}椅子很舒服')
#
#     def __str__(self) -> str:       #列印字串用
#         return f'{self.color}的椅子'
#
# chair_a = Chair('Green')
# chair_b = Chair('Yellow')
#
# print(chair_a)                      #return出 Green的椅子
# print(chair_b)                      #return出 Yellow的椅子
#
# # ---------------------------------------------------------
#
# # 【新增def __eq__(self, other)：比較使用】
#
# class Chair():
#     def __init__(self, color: str) -> None:
#       self.color = color
#
#     def seat(self) -> None:
#         print(f'{self.color}椅子很舒服')
#
#     def __eq__(self, other) -> bool:  # 比較使用
#         return True                   # 不管如何都為True
#
# chair_a = Chair('Green')
# chair_b = Chair('Yellow')
#
# print(chair_a == chair_b)             # return出 True
#
# # ----------------------------------------------------
#
# class Chair():
#     def __init__(self, color: str) -> None:
#       self.color = color
#
#     def seat(self) -> None:
#         print(f'{self.color}椅子很舒服')
#
#     def __eq__(self, other) -> bool:      # 比較使用
#         return self.color == other.color  # 設定比較條件
#
# chair_a = Chair('Green')
# chair_b = Chair('Yellow')
# chair_c = Chair('Green')
#
# print(chair_a == chair_b)                 # return出 False
# print(chair_a == chair_c)                 # return出 True
#
# # ------------------------------------------------------
#
# # 【物件繼承】
#
# # 【寫法】
#
# class Chair():
#     def __init__(self, color):
#         self.color = color
#
#     def seat(self):
#         print(self.color, "椅子很好坐")
#
# class Sofa(Chair):                 # 在括號中寫上父類別的名稱
#     pass
#
# a_sofa = Sofa("Black")
#
# a_sofa.seat()                      # 印出 Black 椅子很好坐
#
# # ---------------------------------------------------------
#
# # 【如果有自己獨特的屬性(繼承後要加新功能)】
#
# class Chair():
#     def __init__(self, color):
#         self.color = color
#
#     def seat(self):
#         print(self.color, '椅子很好坐')
#
# class Sofa(Chair):
#     def __init__(self, color, material):
#         super().__init__(color)    # super() 就是呼叫所繼承的父類別
#         self.material = material
#
# a_sofa = Sofa("Black", "牛皮")
#
# print(a_sofa.color)                # 印出 Black
# print(a_sofa.material)             # 印出 牛皮
#
# # ------------------------------------------------------------
#
# class Chair():
#     name = "椅子"
#
#     def __init__(self, c: str) -> None:
#         self.color = c
#
#     def seat(self) -> None:
#         print(f"{self.color}{self.name}很舒服")
#
#     def __str__(self) -> str:
#         return f"{self.color}的{self.name}"
#
#     def __eq__(self, other) -> bool:
#         return self.color == other.color
#
# class Sofa(Chair):
#     name = "沙發"
#
#     def lay(self) -> None:
#         print(f"{self.color}{self.name}可以躺~")
#
# sofa_a = Sofa('Black')
# sofa_b = Sofa('White')
#
# sofa_a.seat()  # 印出 Black沙發很舒服
# sofa_b.lay()   # 印出 White沙發可以躺~
#
# # ---------------------------------------------------------
#
# class Chair():
#     name = '椅子'
#
#     def __init__(self, color: str) -> None:
#         self.color = color
#
#     def seat(self) -> None:
#         print(f'{self.color}{self.name}很舒服')
#
#     def __str__(self) -> str:
#         return f'{self.color}的{self.name}'
#
#     def __eq__(self, other) -> bool:
#         return self.color == other.color
#
# class Sofa(Chair):
#     name = '沙發'
#
#     def lay(self) -> None:     # 新增定義項目
#         print(f'{self.color}{self.name}可以躺~')
#
#     def seat(self) -> None:    # 重新定義，即可蓋掉原繼承內容
#         print('zzzz')
#
# sofa_a = Sofa('Black')
# sofa_b = Sofa('White')
#
# sofa_a.seat()                  # 印出 zzzz
# sofa_a.lay()                   # 印出 Black沙發可以躺~
#
# # ----------------------------------------------------
#
# # 【繼承不能直接使用父類別的方法】
#
# class Chair():
#     def __init__(self, color):
#         self.color = color
#
#     def seat(self):
#         print(self.color, '椅子很好坐')
#
# class Sofa(Chair):
#     def seat(self):
#         print(self.color, '沙發很舒服!')  # 重新定義seat
#
# a_sofa = Sofa("Black")
#
# a_sofa.seat()                           # 印出 Black 沙發很舒服!
#
# # ------------------------------------------------------
#
# class Chair():
#     name = "椅子"                                # 把需要調整的部分另外設定
#
#     def __init__(self, color: str) -> None:
#         self.color = color
#
#     def seat(self) -> None:
#         print(f"{self.color}{self.name}很舒服")  # 把需要調整的部分另外設定
#
#     def __str__(self) -> str:
#         return f"{self.color}的{self.name}"     # 把需要調整的部分另外設定
#
#     def __eq__(self, other) -> bool:
#         return self.color == other.color
#
# class Sofa(Chair):                              # 把要繼承的放到小括號內
#     name = '沙發'                                # 不動就用預設值，要用就需要重新設定
#
# sofa_a = Sofa('Black')
# sofa_b = Sofa('White')
#
# sofa_a.seat()                                   # 印出 Black沙發很舒服
# print(sofa_b)                                   # 印出 White的沙發
# print(sofa_a == sofa_b)                         # 印出 False
#
# # -------------------------------------------------------------
#
# # 【我想要在呼叫沙發本身的seat之前，先呼叫一下椅子的seat】
#
# class Chair():
#     def __init__(self, color) -> None:
#         self.color = color
#
#     def seat(self) -> None:
#         print(self.color, '椅子很好坐')
#
# class Sofa(Chair):
#     def seat(self):
#         super().seat()                   # 以super()呼叫繼承的父類別
#         print(self.color, '沙發很舒服!')   # 新增內容
#
# a_sofa = Sofa("Black")
#
# a_sofa.seat()
#
# # 印出
# # Black 椅子很好坐
# # Black 沙發很舒服!
#
# # ----------------------------------------------------------
#
# # 【子類別可透過super()，使用父類別已寫好之內容】
#
# class Chair():
#     name = '椅子'
#
#     def __init__(self, c: str) -> None:
#         self.color = c
#
#     def seat(self) -> None:
#         print(f'{self.color}{self.name}很舒服')
#
#     def __str__(self) -> str:
#         return f'{self.color}的{self.name}'
#
#     def __eq__(self, other) -> bool:
#         return self.color == other.color
#
# class Sofa(Chair):
#     name = '沙發'
#
#     def lay(self) -> None:
#         print(f'{self.name}可以躺~')
#
#     def seat(self) -> None:
#         super().seat()        # 可使用super()呼叫，保留原有的內容
#         print('zzzz')         # 加上新內容
#
# sofa_a = Sofa('Black')
# sofa_b = Sofa('White')
#
# sofa_a.seat()
# # 印出
# # Black沙發很舒服
# # zzzz
#
# sofa_a.lay()  # 印出 沙發可以躺~
#
# # ----------------------------------------------------------
#
# class BaseCRUD:                                              # 定義資料庫
#     data = list(range(1, 51))                                # 正常情況應由資料庫拉入資料，因現無資料庫故自行產出
#
#     def read_data(self) -> list:                        # 定義(讀取資料)
#         return self.data                                     # 回傳數據
#
# class EvenCRUD(BaseCRUD):                                    # 繼承BaseCRUD
#     def read_data(self) -> list:
#         raw_data = super().read_data()
#         return list(filter(lambda x: x % 2 == 0, raw_data))  # 回傳偶數值
#
# print(EvenCRUD().read_data())
# # 印出
# # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]