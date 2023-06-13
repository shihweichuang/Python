# # 【str 型態轉換】
# # 語法：str(數值)
# num = 123
# print(type(str(num)))   # 印出 <class 'str'>
#
# # -------------------------------------------------
#
# # 【format】
#
# # 語法1："字串{}".format(變數)
# name = input("What is your name? ")
# print("Hello {}".format(name))
#
# # 語法2："字串{}".format(變數="字串")
# name = input("What is your name? ")
# print("Hello {name}".format(name = "Lux"))   # 印出 Hello Lux
#
# # 語法3：字串.format(變數,變數,變數)
# a = 100
# t = "答案是{}!!{}!!{}!!{}!!"
# print(t.format(a, a, a, a))     # 印出 答案是100!!100!!100!!100!!
#
# # 語法4：字串.format(變數=變數)
# a = 100
# t = "答案是{score}!!{score}!!{score}!!{score}!!"
# print(t.format(score=a))     # 印出 答案是100!!100!!100!!100!!
#
# # 語法5：字串.format(X=變數1, Y=變數2)
# a = 999
# b = 444
# t = "答案是{score}!!{score2}!!{score}!!{score2}!!"
# print(t.format(score = a, score2 = b))   # 印出 答案是999!!444!!999!!444!!
#
# # 語法6：'字串 {}'.format(變數)
# n = "Lux"
# print('Hello, {}'.format(n))    # 印出 Hello, Lux
#
# # 語法7_f-string：f'字串 {n}'
# n = "Lux"
# print(f"hello, {n}")            # 印出 Hello, Lux
#
# # -------------------------------------------------
#
# # 【len 計算長度】
# # 注意：只能計算字串，不能計算int
#
# # 語法：len(字串)
# print(len("hi"))     # 印出 2
# print(len("654321"))     # 印出 6
#
# # -------------------------------------------------
#
# # 【split 分開、分隔】
# # 注意：split之後為list[str]
#
# # 語法：字串.split(分隔元素)
# str1 = "1 2 3 4 5"
# print(str2.split())      # 印出 ['1', '2', '3', '4', '5']
#
# str2 = '1,2,3,4,5'
# print(str2.split(','))   # 印出 ['1', '2', '3', '4', '5']
#
# s = '1 2 3 4'
# a = '4-5-6-7'
# s_sp = s.split()
# a_sp = a.split('-')
# print(s_sp)          # 印出 ['1', '2', '3', '4']
# print(a_sp)          # 印出 ['4', '5', '6', '7']
#
# s = '1 2 3 4'
# a = '4,5,6,7'
# s_sp = s.split()
# a_sp = a.split('-')    # 沒有切成功
# print(s_sp)            # 印出 ['1', '2', '3', '4']
# print(a_sp)            # 印出 ['4,5,6,7']
#
# # -------------------------------------------------
#
# # 【splitlines 多行、分隔】
# # 語法：str.splitlines()
# str1 = """1
# 2
# 3
# 4
# 5
# """
# print(str1.splitlines())   # 印出 ['1', '2', '3', '4', '5']
#
# q = """this is one
# This is two
# Three"""
# q_sp = q.splitlines()
# print(q_sp)                 # 印出 ['this is one', 'This is two', 'Three']
#
# # -------------------------------------------------
#
# # 【strip 去掉空白】
# # 語法：str.strip()
# str1 = "       Hello           "
# print(str1.strip())       # 印出 Hello
#
# # -------------------------------------------------
#
# # 【count 計算重複字元】
# # 語法：str.count()
# str1 = 'This is a apple'
# print(str1.count('is'))   # 印出 2
#
# # -------------------------------------------------
#
# # 【zfill 不足N位數，補足】
# # 語法：str.zfill()
# str1 = "99"
# print(str1.zfill(5))      # 印出 00099
#
# # -------------------------------------------------
#
# # 【slicing 切斷擷取部分】
# # 語法：str[X: Y]        從X開始，Y-1結束
str1 = "1234567"
# print(str1[0])            # 索引座位號，印出 1
# print(str1[0:3])          # 從0開始，到3-1結束，印出 123
# print(str1[3:-1])         # 從3開始，到最後-1結束，印出 456
# print(str1[0:len(str1)])  # 從0開始，到長度-1結束，印出 1234567
# print(str1[0:])           # 從0開始，到最後結束，印出 1234567
# print(str1[:])            # 從0開始，到最後結束，印出 1234567
# print(str1[::2])          # 從0開始，到最後結束，2個一抓，印出 1357
#
# # -------------------------------------------------
#
# # 【\n 換行】
# # 注意：不支援換行(語法需為一行)
# # 語法："字串\n字串"
# print("Hello\nLux")
# # 印出 Hello
# #     Lux
#
# # -------------------------------------------------
#
# # 【""" """(左右各三個引號) 換行】
# # 注意：支援換行(語法可為多行)
# # 語法： """字串
# #          字串"""
# print("""Hello
# Jerry""")
# # 印出 Hello
# #     Jerry
#
# # -------------------------------------------------
#
# # 【保留小數點後N位】
# # 語法："{:.?f}".format()
# pi = 3.14159
# print("{:.2f}".format(pi))    # 印出 3.14
#
# # -------------------------------------------------
#
# # 【三位一點】
# # 語法："{:,}".format()
# a = 104104104104104
# print("{:,}".format(a))     # 印出 104,104,104,104,104
#
# # -------------------------------------------------
#
# # 【增強數字可讀性】
# # 語法：1_000_000    3個0寫一底線，不會影響數字的值
# a = 1_000_000
# print(a)             # 印出 1000000