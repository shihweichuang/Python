# # 【TA2-2 練習 型別轉換】
# #
# # 輸入為一串數字，每個數字間以一個空白隔開，
# # 數字長度不固定，請把這些數字每個各加1後輸出
# #
# # 使用int、str轉換型態
# # 使用len()計算長
# #
# # 輸入：1 2 3 4 5       輸出：2 3 4 5 6
# # 輸入：1 3 5 7 9 10    輸出：2 4 6 8 10 11
# # 輸入：4               輸出：5
# #
# # ---------------------------
#
# # 方法一
# x_sp = input().split(" ")               # 分開
#
# i = 0
# while i < len(x_sp):                    # 限制從0到長度-1
#     print(int(x_sp[i]) + 1, end = " ")  # 抓字元轉數字後+1，再用空白連接
#     i += 1
#
# # ---------------------------
#
# # 方法二
# q = "1 2 3 4 5"
# q_sp = q.split()
# answer = []
# for s in q_sp:
#     answer.append(str(int(s) + 1))      # 需要轉成字串才能用join
# print(" ".join(answer))
#
# # ---------------------------
#
# # 方法三、串列生成式(效果同上)
# print(' '.join([str(int(s) + 1) for s in input().split()]))
#
# # ---------------------------
#
# # 串列生成式介紹
# # input()
# # input().split
# # s for s in input().split
# # int(s) + 1 for s in input().split()
# # str(int(s) + 1) for s in input().split()
# # ‘ ‘.join([str(int(s) + 1) for s in input().split()])
# # print(‘ ‘.join([str(int(s) + 1) for s in input().split()]))