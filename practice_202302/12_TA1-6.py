# # 【TA1-6 練習 閏年】
#
# # 今天要設計一款判斷是否為閏年的程式
# # 是否為閏年，其條件為：
# # 西元年份除以4不可整除，為平年。
# # 西元年份除以4可整除，且除以100不可整除，為閏年。
# # 西元年份除以100可整除，且除以400不可整除，為平年
# # 西元年份除以400可整除，為閏年。
#
# # 輸入為一組西元年，請根據以上規則判斷是否為閏年，若為閏年請回傳True，否則False
#
# # 輸入：2000        輸出：True
# # 輸入：1900        輸出：False
# # 輸入：1996        輸出：True
# # 輸入：1999        輸出：False
# # 輸入：2002        輸出：False
#
# # ---------------------------

x = int(input())                      # 輸入(字串)，為後續計算，轉為整數

if x % 4 != 0:                        # 如果x不被4整除，則列印False
    print(False)
else:
  if x % 4 == 0 and x % 100 != 0:     # 如果X被4整除，且x不被100整除，則列印True
    print(True)
  else:
    if x % 100 == 0 and x % 400 != 0: # 如果x被100整除，且x不被400整除，則列印True
        print(False)
    else:
      if x % 400 == 0:                # 如果x被400整除，則列印True
          print(True)