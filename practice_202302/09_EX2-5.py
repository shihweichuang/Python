# # 【EX2-5 翻轉數字】
#
# # 輸入為一個正整數N
#
# # 輸出翻轉過的數字，若前面有0則應該消除。
#
# # 輸入：123456     輸出：654321
# # 輸入：12345      輸出：54321
# # 輸入：230400     輸出：4032
#
# # ---------------------------

x = input()     # 輸入(為字串)
y = x[::-1]     # 將輸入字串顛倒
print(int(y))   # 將字串轉為數字，若前面為0會自動消除