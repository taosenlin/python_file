# Time:2020-01-10 22:05
# Author:TSL
# 现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下
# name: Jack   ;    salary:  12000
#  name :Mike ; salary:  12300
# name: Luk ;   salary:  10030
# 每个员工一行，记录了员工的姓名和薪资，
# 每行记录 原始文件中并不对齐，中间有或多或少的空格
#
# 现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
# 以如下格式存入新的文件 file2.txt中，如下所示
#
# name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
# name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
# name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
# 要求像上面一样的对齐
# tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数

file1 = 'D:\\file1.txt'
file2 = 'D:\\file2.txt'

with open(file1) as ifile,open(file2,'w') as ofile:
    beforesala = ifile.read().splitlines()
# print(beforesala)
    for one in beforesala:
        namePart,salaryPart = one.split(';')
        name = namePart.split(':')[1].strip()
        salary = int(salaryPart.split(':')[1].strip())

        income = int(salary*0.9)
        tax = int(salary*0.1)

        print('name:{:6};salary:{:6};tax:{:6};income:{:6}'.format(name,salary,tax,income))

        ofile.write('name:{:6};salary:{:6};tax:{:6};income:{:6}'.format(name,salary,tax,income) + '\n')






























































