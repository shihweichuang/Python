# # 【python 運算子】
# print(2+3)           # 加，印出 5
# print(2-3)           # 減，印出 -1
# print(2*3)           # 乘，印出 6
# print(2/3)           # 除，印出 0.666666666666
# print(2//3)          # 整數除，印出 0
# print(2%3)           # 求餘數，印出 2
# print(2**3)          # 次方，印出 8
#
# # -------------------------------------------------
#
# # 【配合變數的運算】
# age = 18 + 3
# year = 10
# age = age + year
# print(age)           # 印出 31
#
# # -------------------------------------------------
#
# 【注意：同樣類型才能進行運算】
# # print("hi" + 100)  # 跳出 ERROR
# print("hi" + "ya")   # 印出 hiya
# print("100" + "200") # 印出 100200
#
# a = "hi" * 3
# print(a)             # 印出 hihihi
#
# print("-" * 10)      # 印出 ----------
#
# # -------------------------------------------------
#
# a = 100
# a = 10               # 會蓋掉上面的資料
# print(a)             # 印出 10
#
# a = 100
# a = 10               # 會蓋掉上面的資料
# a = a + 100
# print(a)             # 印出 110
#
# a = 100
# a = 10
# a = a + a + a
# print(a)             # 印出 30