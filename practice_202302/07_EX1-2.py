# 【EX1-2 計算周長】
#
# 題目輸入一個數字代表圓半徑，請計算圓周長。
# 圓周率為3.14
#
# 圓周長公式如下：
# 周長 = 半徑×2×圓周率(3.14)
#
# 請輸出周長，並且無條件捨去至整數。
#
# 輸入：10     輸出：62
# 輸入：2      輸出：12
#
# ---------------------------

import math           # 載入math模組
r = int(input())      # 輸入半徑，字串轉為數字
a = r * 2 * 3.14      # 周長=半徑*2*3.14
print(math.floor(a))  # 周長採無條件捨去至整數