# # 【TA2-4 練習】
#
# # 在平台解題時，大部分都是一次讀多筆資料，
# # 試著用迴圈處理看看，一次處理多筆資料
# # 這次跟第一次題目一樣，請題目給你甚麼，
# # 你就回復甚麼，但是必須加個流水號，只是這次題目是多行
#
# # 使用splitlines()分隔換行
#
# # 輸入
# # Hello
# # World
# # This
# # is
# # a
# # question
#
# # 輸出
# # Hello1
# # World2
# # This3
# # is4
# # a5
# # question9
#
# # ---------------------------

import sys

lines = sys.stdin.read().splitlines()

for i, line in enumerate(lines):
    print(f"{line}{i+1}")