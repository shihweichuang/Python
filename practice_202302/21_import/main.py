# # 【語法1：21_import <module>]
#
# # 注意：import會優先從專案找尋，
# # 如果專案名稱與內建功能重複，會直接覆蓋掉，以致無法使用內建功能
#
# 21_import my_module
#
# a = my_module.A()
#
# a.hello()               # 印出 hello A
#
# # ------------------------------------------
#
# # 【語法2：from <module> 21_import <name1, name2, …>]
#
# from my_module 21_import A   # 直接帶入定義名稱
#
# a = A()
#
# a.hello()                 # 印出 hello A
#
# # ------------------------------------------
#
# # 【語法3：21_import <module> as <new_name> 把套件名稱改名]
#
# 21_import my_module as zzz
#
# a = zzz.A()
#
# a.hello()                   # 印出 hello A