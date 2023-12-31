# # 【TA2-1 練習 99乘法表】
#
# # 請使用while迴圈，印出指定數乘法表
#
# # 輸入為兩個數字(x,y)，每個數字以一個空白隔開，請印出此x×y乘法表
#
# # 輸入：2 2
# # 輸出：1x1=1
# #      1x2=2
# #      2x1=2
# #      2x2=4
#
# # 輸入：3 4
# # 輸出：1x1=1
# #      1x2=2
# #      1x3=3
# #      1x4=4
# #      2x1=2
# #      2x2=4
# #      2x3=6
# #      2x4=8
# #      3x1=3
# #      3x2=6
# #      3x4=12
#
# # ---------------------------
#
# # 九九乘法表
# num = input().split()  # 輸入(字串)，拆開成兩組
# x = int(num[0])  # 第一組轉為整數
# y = int(num[1])  # 第二組轉為整數
#
# i = 1  # i從1開始
#
# while i <= x:                      # i到x結束
#     k = 1                          # k從1開始
#
#     while k <= y:                  # k到y結束
#         print(f"{i}x{k}={i * k}")  # 列印i*k
#
#         k += 1                     # 相乘後，k+1
#
#     i += 1                         # 相乘後，i+1
#
# # 九九乘法表(不包含相同相乘)
# num = input().split()              # 輸入(字串)，拆開成兩組
# x = int(num[0])                    # 第一組轉為整數
# y = int(num[1])                    # 第二組轉為整數
# i = 1                              # i從1開始
# while i <= x:                      # i到x結束
#     k = 1                          # k從1開始
#     while k <= y:                  # k到y結束
#         if i == k:                 # 如果相乘數字相同
#             k += 1                 # k+1
#             continue               # 直接跳到下一圈
#         print(f'{i}x{k}={i*k}')    # 列印i*k
#         k += 1                     # k+1
#     i += 1                         # i+1