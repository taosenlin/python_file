# Time:2020-03-17 8:03
# Author:TSL

with open(r'D:\pythonfile\gbk.txt','rb') as f1,open(r'D:\pythonfile\utf8.txt','rb') as f2:
    file1 = f1.read().decode("gbk")
    file2 = f2.read().decode("utf8")
    file = file1 + file2
    name = input("请输入新文件的名称:")
    with open(f'./{name}.txt','w',encoding="utf8") as f3:
        f3.write(file)