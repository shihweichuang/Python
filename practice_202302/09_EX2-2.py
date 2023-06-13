# # 【EX2-2 格式化輸出2】
#
# # 題目輸入一個文字，請完成指定格式化輸出
#
# # 請讀入文字後，並且計算文字長度，接著使用以下格式進行排版後輸出。
# # My name is ___, it is ___ characters.
#
# # 輸入：Lisa        輸出：My name is Lisa, it is 4 characters.
# # 輸入：Banana      輸出：My name is Banana, it is 6 characters.
#
# #---------------------------
#
# a = input()     # 輸入(為字串)
# b = len(a)      # 計算輸入(字串)長度
#
# # 方法一
# print("My name is {name}, it is {len} characters.".format(name = a, len = b))
# # 將輸入內容，代入預設字串
#
# # 方法二
# print("My name is {}, it is {} characters.".format(a, b))
# # 將輸入內容，代入預設字串
#
# # 方法三
# print(f"My name is {a}, it is {b} characters.")