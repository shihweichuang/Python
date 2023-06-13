# # 【EX4-1 反轉句子中的單字】
#
# # 保持英文句子中所有單字的順序, 也保留單字間的空白,
# # 但每個單字的所有字母及符號全部反轉.
#
# # 輸入只有⼀⾏，其中含有⼀個正整數，代表⻄元年份。
# # 每個輸入的測試檔案，只有⼀筆測試資料。
#
# # 反轉後的字串
#
# # 輸入：Let’s take LeetCode contest
# # 輸出：s’teL ekat edoCteeL tsetnoc
#
# # 輸入：God Ding
# # 輸出：doG gniD
#
# # ---------------------------

# # 方法一
a = input()                     # 輸入
b = a.split()                   # 分隔
c = 0                           # 從0開始算起
d = len(b)                      # 計算字串長度
while c < d:                    # 從0開始到長度-1
  print(b[c][::-1], end = " ")  # 取字串後顛倒，再連接起來(不換行)
  c += 1

# # 方法二
q = input()                        # 輸入(字串)
q_sp = q.split()                   # 將字串拆開
i = 0                              # i從0開始
answer = []                        # 設定一空白清單
while i < len(q_sp):               # 當i從0到字串長度-1
    answer.append(q_sp[i][::-1])   # 第i字串顛倒放，再加到空白清單
    i += 1                         # i每次+1
print(' '.join(answer))            # 將清單內字串連接