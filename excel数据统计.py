import xlrd
# 1.完成衣服销售数据的统计和分析  2.上传代码到云端仓库，并把仓库地址发到群里
# 12月衣服数量  总销售额  平均销售量 、每月销售占比

wb = xlrd.open_workbook(filename='12月份衣服销售数据.xlsx', encoding_override=True)
sheet = wb.sheet_by_name("12月份各种服饰销售情况")
rows = sheet.nrows
cols = sheet.ncols
# print(rows)
# print(cols)
# 打印excel表中数据
for i in range(rows):
    for j in range(cols):
        sheet.cell_value(i, j)
        print(sheet.cell_value(i, j), end='   ')
    print('\n')

# 衣服数量
num_1 = 0
for i in range(1, rows):
    a = float(sheet.cell_value(i, 3))
    num_1 += a
print("1.衣服数量：", round(num_1, 2))
print("\n")

# 总共销售额
num_2 = 0
for i in range(1, rows):
    a = float(sheet.cell_value(i, 2))
    b = float(sheet.cell_value(i, 4))
    c = a * b
    num_2 += c
print("3.总共销售额为：", round(num_2, 2))
print("\n")

# 计算平均销售量：
num_3 = 0
for i in range(1, rows):
    a = int(sheet.cell_value(i, 4))
    num_3 += a
asbc = float(num_3 / (int(rows)-1))
print("4.平均销售量：", round(asbc, 2))
print("\n")

# 销售额占比
num_41 = 0
num_42 = 0
num_43 = 0
num_44 = 0
num_45 = 0
num_46 = 0
for i in range(1, rows):
    a = sheet.cell_value(i, 1)
    b = float(sheet.cell_value(i, 2))
    c = float(sheet.cell_value(i, 4))
    if a == "羽绒服": num_41 += c*b
    if a == "T血": num_42 += c*b
    if a == "风衣": num_43 += c*b
    if a == "衬衫": num_44 += c*b
    if a == "牛仔裤": num_45 += c*b
    if a == "皮草": num_46 += c*b
acc_1 = num_41 / num_2 * 100
print("羽绒服销售占比：", round(acc_1, 3), "%")
acc_2 = num_42 / num_2 * 100
print("T血销售占比：", round(acc_2, 3), "%")
acc_3 = num_43 / num_2 * 100
print("风衣占比：", round(acc_3, 3), "%")
acc_4 = num_44 / num_2 * 100
print("衬衫占比：", round(acc_4, 3), "%")
acc_5 = num_45 / num_2 * 100
print("牛仔裤占比：", round(acc_5, 3), "%")
acc_6 = num_46 / num_2 * 100
print("皮草占比：", round(acc_6, 3), "%")







