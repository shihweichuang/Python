# # 【EX2-6 壞的遙控器】
#
# # 遙控器上所有按鍵全壞了，只剩下『下一個頻道』可以使用。
# # 目前電視有200個頻道，編號是0~199，
# # 給定目前現在正在看的頻道，
# # 請問使用者必須按下幾次『下一個頻道』，才能切換到指定的頻道
#
# # 用空格分開兩個整數，代表目前頻道以及目標頻道。
#
# # 輸出需按下的次數。
#
# # 輸入：5 11       輸出：6
# # 輸入：199 2      輸出：3
#
# -----------提示：取餘數-----------
# 1~10
#
# 1     2+10   11>1  %10
#
# 2     1+10     9>9
#
# 公式：第二個數，加200，減掉第一個數，除以200取餘數
#
# ---------------------------

a = input()                     # 輸入(為字串)
b = a.split()                   # 分隔字串
c = int(b[1]) + 200 - int(b[0]) # 將第二個數字+200，扣掉第一個數字
print(c % 200)                  # 除以200取餘數