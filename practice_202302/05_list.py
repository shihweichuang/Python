# # 【用[]來建立清單】
#
# empty_list = []
# weekdays = ["Monday", "Tuesday", "Wednesday"]
# years = [2000, 2001, 2002, 2003]
#
# # -------------------------------------------------
#
# # 【用[座位號]來取得內容】
#
# print(weekdays[0])  # 印出 Monday
#
# stds = []           # 建立空的list
# stds = ["ss1", "ss2", "ss3", "ss4", "ss5"]
# # 索引值 0 1 2 3 4
# # 索引值 -5 -4 -3 -2 -1
# print(stds)         # 印出 ['ss1', 'ss2', 'ss3', 'ss4', 'ss5']
# print(type(stds))   # 印出 <class 'list'>
# print(stds[0])      # 抓第一個，印出 ss1
# print(stds[2])      # 抓第三個，印出 ss3
# print(stds[-1])     # 抓最後一個，印出 ss5
#
# # -------------------------------------------------
#
# # 【用slice取得內容】
# # 語法：stds[X:Y]
# # 從X開始，Y-1結束
# weekdays = ['Monday', 'Tuesday', 'Wednesday']
# print(weekdays[1:3])    # 印出 ['Tuesday', 'Wednesday']
#
# stds = ["A", "B", "C", "D", "E"]
# print(stds[1:2])        # 從1開始，2-1結束，印出 ['B']
#
# stds = ["A", "B", "C", "D"]
# print(stds[1:4])        # 從1開始，4-1結束，印出 ['B', 'C', 'D']
#
# stds = ["A", "B", "C", "D"]
# print(stds[1:])         # 從1開始，到尾結束，印出 ['B', 'C', 'D']
#
# stds = ["A", "B", "C", "D"]
# print(stds[:3])         # 從0開始，3-1結束，印出 ['A', 'B', 'C']
#
# stds = ["A", "B", "C", "D"]
# print(stds[:])          # 從頭開始，到尾結束，印出 ['A', 'B', 'C', 'D']
# print(stds)
#
# stds = ["A", "B", "C", "D", "E"]
# print(stds[::2])        # 從頭開始，到尾結束，兩個一跳，印出 ['A', 'C', 'E']
#
# stds = ["A", "B", "C", "D", "E"]
# print(stds[::-1])       # 從尾開始，到頭結束，印出 ['E', 'D', 'C', 'B', 'A']
#
# stds = ['A', 'B', 'C', 'D', 'E']
# # print(stds[100])      #選到不存在的值，會跳出ERROR
#
# # -------------------------------------------------
#
# # 【append 加入】
# # 語法：list.append()
# num_list = []
# num_list.append(1)      # 將1加到清單中
# num_list.append(2)      # 將2加到清單中
# print(num_list)         # 印出 [1, 2]
#
# a = []
# a.append("A")           # 將"A"加到清單中
# print(a)                # 印出 ['A']
# a.append("B")           # 將"B"加到清單中
# print(a)                # 印出 ['A', 'B']
#
# # -------------------------------------------------
#
# # 【insert(索引)插入】
# # 語法：list.insert(插入座位號, 插入文字)
# num_list = [1, 2, 3, 4, 5, 6]
# num_list.insert(4, 100)
# print(num_list)         # 印出 [1, 2, 3, 4, 100, 5, 6]
#
# # -------------------------------------------------
#
# # 【del刪除】
# # 語法：del list[X]
# num_list = [1, 2, 3, 4, 5, 6]
# del num_list[2]
# print(num_list)         # 印出 [1, 2, 4, 5, 6]
#
# # -------------------------------------------------
#
# # 【remove(值)刪除】
# # 語法：list.remove("X")
# num_list = ["A", "B", "C", "D"]
# num_list.remove("B")
# print(num_list)         # 印出 ['A', 'C', 'D']
#
# # remove() 僅刪除第一個遇到的值
# num_list = ["A", "B", "B", "C", "D"]
# num_list.remove("B")    # 僅刪除第一個B就停止
# print(num_list)         # 印出 ['A', 'B', 'C', 'D']
#
# num_list = [1, 2, 2, 3, 4, 5, 6]
# num_list.remove(2)      # 僅刪除第一個2就停止
# print(num_list)
#
# num_list = ['A', 'B', 'B', 'C', 'D']
# num_list.remove('Z')  # 欲刪除的值不在清單中
# print(num_list)       # 跳出 ERROR
#
# # -------------------------------------------------
#
# # 【index(值)找索引】
# # 語法：list.index(座位號)
# num_list = [6, 5, 4, 3, 2, 1]
# print(num_list.index(2))  # 印出 4
#
# # -------------------------------------------------
#
# # 【in 是否存在裡面】
# # 語法：數字 in list
# num_list = [6, 5, 4, 3, 2, 1]
# print(2 in num_list)     # 印出 True
# print(11 in num_list)    # 印出 False
#
# # -------------------------------------------------
#
# # 【count 計算一個值的出現次數】
# # 語法：list.count(數值)
# num_list = [1, 2, 3, 4, 5, 6, 7, 2, 3, 5, 2]
# print(num_list.count(2))  # 印出 3
# print(num_list.count(3))  # 印出 2
#
# # -------------------------------------------------
#
# # 【join 用指定符號串起內容】
# # 語法：'串接用符號'.join(list)
# student_list = ["小一", "老二", "老三"]
# print("-----".join(student_list))  # 印出 小一-----老二-----老三
#
# # -------------------------------------------------
#
# # 【sort、sorted 排序】
# # 有兩種算法
# # a.sort()    None→不會有回傳值，而是直接修改變數內的結果
# # sorted(a)   回傳list→不會修改變數內的結果
# # 語法：list.sort()
# a = [4, 2, 1, 3]
# b = a.sort()
# print(a)          # 印出 [1, 2, 3, 4]，可以發現a已經被排序過
# print(b)          # 印出 None，因為sort方法不會回傳值
#
# a = [1, 2, 3, 4, 5, 4, 3, 7, 8, 4, 6, 5]
# a.sort()
# print(a)          # 印出 [1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8]
#
# # 語法：sorted(list)
# b = [1, 2, 3, 4, 5, 4, 3, 7, 8, 4, 6, 5]
# sorted(b)         # 不影響原清單
# print(b)          # 印出 [1, 2, 3, 4, 5, 4, 3, 7, 8, 4, 6, 5]
#
# a = [4, 2, 1, 3]
# b = sorted(a)    # 用b把排序後的結果接起來
# print(a)         # 印出 [4, 2, 1, 3]，a未排序
# print(b)         # 印出 [1, 2, 3, 4]，b已排序
#
# # -------------------------------------------------
#
# # 【len 取得長度】
# # 語法：len(list)
# num_list = [1, 2, 3, 4, 5, 6, 7, 2, 3, 5, 2]
# print(len(num_list))     # 印出 11
#
# print(len("hi"))         # 印出 2
# print(len('654321'))     # 印出 6
#
# # -------------------------------------------------
#
# # 【比較 ==】
# # 語法：list == list
# num_list_a = [1, 2, 3, 4]
# num_list_b = [1, 2, 3, 4]
# print(num_list_a == num_list_b)  # 印出 True