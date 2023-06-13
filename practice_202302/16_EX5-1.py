# # 【EX5-1 重複文字只保留一個】
#
# # 在輸入字串中，有些英文字母僅出現一次，也有些出現多次。
# # 你的程式會保留所有在輸入字串中僅出現一次的字母，
# # 但對於多次出現的字母將只保留「最後一個」，其他相同者均捨棄。
# # 你保留下來的字母之先後順序應與原字串的順序相同。
#
# # 依照題目說明輸出指定輸出。
#
# # 輸入：ABACDEAD      輸出：BCEAD
# # 輸入：ABCDE         輸出：ABCDE
#
# # ---------------------------

x = input()[::-1]          # 輸入後先顛倒

list = []                  # 空清單

for i in range(len(x)):
    if x[i] not in list:   # 如果數字不在清單中
        list.append(x[i])  # 加到清單中

new = list[::-1]           # 將清單顛倒

fin = ''.join(new)         # 將清單內資料連結為字串
print(fin)