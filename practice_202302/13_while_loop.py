# # 【while迴圈的格式】
# # while 條件:
# #    pass
#
# # ---------------------------------------------------------
#
# # 【定義好要跑幾圈】
# # 1. 初始條件
# # 2. 判斷條件(是否要繼續跑)
# # 3. 更新條件
#
# i = 0                          # 1. 初始條件
#
# while i <=6:                   # 2. 判斷條件
#     print("Hello World")
#
#     i += 1                     # 3. 更新條件
#
# # 印出
# # Hello World
# # Hello World
# # Hello World
# # Hello World
# # Hello World
# # Hello World
# # Hello World
#
# # -----------------------------------------------------------
#
# # 【把編號也一起印出來】
#
# i = 0
#
# while i <= 6:
#     print(i, "Hello World")
#
#     i += 1                   # i每次+1
#
# # 印出
# # 0 Hello World
# # 1 Hello World
# # 2 Hello World
# # 3 Hello World
# # 4 Hello World
# #　5 Hello World
# # 6 Hello World
#
# # -----------------------------------------------------------
#
# i = 0
#
# while i < 3:
#     print(f"Hi {i}")
#
#     i += 1              # i每次+1
#
# # 印出
# # Hi 0
# # Hi 1
# # Hi 2
#
# # -----------------------------------------------------------
#
# i = 0
#
# while i <= 3:
#     print(f"Hi {i}")
#
#     i += 1              # i每次+1
#
# # 印出
# # Hi 0
# # Hi 1
# # Hi 2
# # Hi 3
#
# # -----------------------------------------------------------
#
# i = 1
#
# while i <= 5:
#     print(f"Hi {i}")
#
#     i += 2              # i每次加2
#
# # 印出
# # Hi 1
# # Hi 3
# # Hi 5
#
# # -----------------------------------------------------------
#
# i = 0
#
# while i < 3:
#     print(f"Hi {i * 2 + 1}")
#
#     i += 1              # i每次+1
#
# # 印出
# # Hi 1
# # Hi 3
# # Hi 5
# # """
#
# # -----------------------------------------------------------
#
# #【迴圈(迭代iterate)配合list】
#
# a = ["A", "B", "C", "D"]
# i = 0
# while i <= 3:
#     print(a[i])          # 字串中，從0取到3
#
#     i += 1
#
# # 印出
# # A
# # B
# # C
# # D
#
# # -----------------------------------------------------------
#
# a = ['A', 'B', 'C', 'D']
#
# i = 0
#
# while i < len(a):  # 從0到長度-1
#     print(a[i])    # 從清單第一個開始抓
#
#     i += 1         # i每次+1
#
# # 印出
# # A
# # B
# # C
# # D
#
# # -----------------------------------------------------------
#
# # 【print加上end = " "，可連接取出字串】
#
# a = ['A', 'B', 'C', 'D']
#
# i = 0
#
# while i < len(a):  # 從0到長度-1
#     print(a[i], end=" ")  # 從清單第一個開始抓，並用空格連接
#
#     i += 1  # i每次+1
#
# # 印出 A B C D
#
# # -----------------------------------------------------------
#
# # 【巢狀迴圈】
#
# i = 1
#
# while i < 4:        # 只要跑3圈，設小於4
#     k = 1           # 每一圈的k都要重算，如果放到最外圈，大於4後就不會再跑了
#
#     while k < 4:    # 從1到3，設小於4
#         print(k)    # 從1到3
#
#         k += 1      # k每次+1
#
#     i += 1          # i每次+1
#
# # 印出
# # 1
# # 2
# # 3
# # 1
# # 2
# # 3
# # 1
# # 2
# # 3
#
# # -----------------------------------------------------------
#
# i = 1
#
# while i < 4:                        # 只要跑3圈，設小於4
#
#     k = 1                           # 每一圈的k都要重算，如果放到最外圈，大於4後就不會再跑了
#
#     while k < 4:                    # 從1到3，設小於4
#         print(f"{i}x{k}={i*k}")     # 相乘公式
#
#         k += 1                      # k每次+1
#
#     i += 1                          # i每次+1
#
# # 印出
# # 1x1=1
# # 1x2=2
# # 1x3=3
# # 2x1=2
# # 2x2=4
# # 2x3=6
# # 3x1=3
# # 3x2=6
# # 3x3=9
#
# # -----------------------------------------------------------
#
# # 【break 結束整個迴圈】
#
# i = 0
#
# while i < 5:        # i從0到4
#     print(i)        # 列印i
#
#     if i == 2:      # 當i等於2，馬上停止
#         break
#
#     i += 1          # i每次+1
#
# # 印出
# # 0
# # 1
# # 2
#
# # -----------------------------------------------------------
#
# # 【continue 跳過下面的程式碼，直接進入下一圈】
#
# i = 0
#
# while i < 5:      # i從0到4
#     print(i)      # 列印i
#
#     if i == 2:    # 如果i等於2
#         continue  # 直接跳到下一圈，不往下跑
#
#     i += 1        # 因此不會跑到i+=1，i一直為2
#
# # 印出
# # 2
# # 2
# # ..(無限迴圈)
#
# # -----------------------------------------------------------
#
# i = 0
#
# while i < 5:        # i從0到4
#     if i == 2:      # 如果i等於2
#         i += 1      # i+1
#         continue    # 跳到下一圈，不往下繼續
#
#     print(i)        # 列印i
#
#     i += 1          # i每次+1
#
# # 印出
# # 0
# # 1
# # 3
# # 4