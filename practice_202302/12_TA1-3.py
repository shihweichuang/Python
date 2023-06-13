# # 【TA1-3 練習 if】
#
# # 輸入會有三個值，
# # 第一個值是星期幾，
# # 第二個值是股票的單價，
# # 第三個值是今日成交總量，
# # 每個值之間用一個空白隔開，
# # 假設此股票在星期五、六、日是不開市的，
# # 所以如果是在這幾天，請回傳"不開市”
#
# # 輸入：星期一 99 1000       輸出：99000
# # 輸入：星期六 100 10        輸出：不開市
#
# # ---------------------------

x = input()  # 輸入(字串)
x_sp = x.split()  # 拆開

if x_sp[0] == '星期五':  # 如果第1個字為星期五，則列印不開市
    print('不開市')
elif x_sp[0] == '星期六':  # 如果第1個字為星期六，則列印不開市
    print('不開市')
elif x_sp[0] == '星期日':  # 如果第1個字為星期日，則列印不開市
    print('不開市')
else:  # 其餘狀況，將第1、2個字轉為數字後相乘
    print(int(x_sp[1]) * int(x_sp[2]))