# # 【EX4-3 範圍內最大質數】
#
# # 讓使用者輸入一個大於等於 2 的正整數後，程式輸出小於或等於該數的「最⼤質數」
#
# # 質數的定義：除了1跟他自己本身，沒有其他因數。
#
# # 依照題目說明輸出指定輸字。
#
# # 輸入：10    輸出：7
# # 輸入：101   輸出：101
# # 輸入：40    輸出：37
#
# # ---------------------------
#
# # 範圍內最大質數(含輸入內容)
# x = int(input())         # 輸入(字串)轉整數
# num=[]                   # 新增一空白清單
# for i in range(2,x+1):   # 要被檢查的數字(從2開始，直到x)
#    for j in range(2,i):  # 用於除的數字(從2開始，直到i)
#       if(i%j==0):        # 如果能整除就停下
#          break
#    else:                 # 是質數，加入清單
#       num.append(i)
# print(max(num))          # 列印清單中最大值
#
# # --------------------------
#
# # 利用函數，計算範圍內最大質數(含輸入內容)
# # 方法一
# def is_prime_number(n: int) -> bool:  # 定義：是否為質數
#    if n == 2:                         # 如果n等於2，回傳True
#       return True
#    for i in range(2, n // 2 + 1):     # 從2開始算到數值一半就好
#       if n % i == 0:                  # 如果n可以被i整除，就回傳False
#          return False
#    return True                        # 如果n不被i整除，就回傳True
#
#
# a = list(range(1, int(input()) + 1))  # 設定一範圍(從1到輸入值+1)，再轉為list
# print(max(list(filter(is_prime_number, a))))
# # 利用filter函式，放入is_prime_number及a，進行質數篩選
# # 因filter後為c語言格式，所以需要再用list轉換
# # 利用max找出list中的最大值，即為範圍內最大質數
#
# # --------------------------
#
# # 方法二
# def is_prime_number(n: int) -> bool:
#    if n == 2:                      # 如果是2就回傳True
#       return True
#    for i in range(2, n // 2 + 1):  # i從2算到數值一半就好
#       if n % i == 0:               # 如果n被i整除，就回傳False
#          return False
#    return True                     # 如果n無法被i整除，就回傳True
#
# q = int(input())                   # 輸入(字串)轉為整數
#
# for i in range(q, 1, -1):          # 從q倒著數到1，每次往後數1
#    if is_prime_number(i) == True:  # 如果i套用公式後等於True，就列印i，並停止
#       print(i)                     # 該數即為範圍內最大質數
#       break