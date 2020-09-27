# Time:2020-03-16 7:56
# Author:TSL
'''
# 1-写
with open('./a.txt','w',encoding='utf8') as f:
    f.write("白日依山尽,黄河入海流")

# 注: encode/decode 为python的内置函数, encoding为定义的一个参数


# 2-读
with open('./a.txt','r',encoding='utf8') as f:
    print(f.read())
# 白日依山尽,黄河入海流
'''

'''
# 3-写bytes类型
with open('./b.txt','wb') as f:           #wb为直接写入bytes类型(二进制方式去写)
    f.write("美人卷珠帘".encode("utf8"))  #需要进行bytes类型编码


# 4-读bytes类型
with open('./b.txt','rb') as f:           #rb为以bytes类型读取
    print(f.read().decode("utf8"))        #需要进行bytes类型解码
# 美人卷珠帘
'''



# 作业1-
with open(r'D:\pythonfile\gbk.txt','rb') as f1,open(r'D:\pythonfile\utf8.txt','rb') as f2:
    file1 = f1.read().decode("gbk")
    file2 = f2.read().decode("utf8")
    file = file1 + file2
    name = input("请输入新文件的名称:")
    with open(f'./{name}.txt','w',encoding="utf8") as f3:
        f3.write(file)












































































