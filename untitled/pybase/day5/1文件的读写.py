#Author : taosenlin
#Time : 2020/3/4 16:00

# 一、文件打开
# 1、内置函数open打开文件，获取文件操作对象
# 2、open函数
# (1) file_Object = open(file_name,access_mode='r')
# a、 file_name 文件路径：相对路径和绝对路径
# b、 access_mode 读（定义时等于号指定的值，缺省参数）、写、读+写



# 3、文件的相对路径
# （1）如果进程操作文件，不是全路径，比如
# open('file1.txt')   open('./file1.txt')
# open('../fold1/file2.txt')
# ../../表示上级目录的上级目录，以此类推

# （2）相对于当前目录来寻找该文件，称之为相对路径

# 注：windows---文件里面换行---\r\n   2个长度
#     字符串    '\n'     1个长度
#     linux          1个长度



# 4、文件路径的写法
# fileDir = 'G:\pyTest.txt'
# 常用方式：
# fileDir = 'G:\\pyTest1.txt'
# fileDir = r'G:\pyTest1.txt'      #加'r' 取消转义

# Fdir = 'C:\ntest'
# print(repr(Fdir))      #取消转义
# repr()  #取消转义函数



# 5、文件指针
# （1）文件指针的概念
# 接下来的读写操作开始的位置
# （2）文件对象的tell方法获取文件指针的位置（文件对象.tell()）



# 6、文件模式---r
# （1）r---读模式
# 只是为了读取文件而打开文件。文件指针在文件的开头，这也是缺省文件打开方式
# open('file1') == open('file1','r')

# 例：
# file1 = 'D:\\file1.txt'
# fo = open(file1,'r')    #默认是r,可不写r
# print(fo.tell())        #获取文件中指针的位置（下标）
# fo.seek(4,0)            #移动文件指针位置 seek(位置，模式)
# print(fo.tell())
# print(fo.read(2))       #获取此时指针位置往后2位的长度(read()不写数字，则全部读取)
# fo.close()              #关闭文件



# 7、文件内容读取
# (1) fo.read()      #注意文件指针的移动，最后的关闭操作
# str = fo.read(2)   #读取2位
# print(str)
# str1 = fo.read()   #读取全部
# print(str1)
# fo.close()


# (2) fo.seek(x)
#注意文件指针的移动
# file1 = 'D:\\file1.txt'
# fo = open(file1,'r')
# fo.seek(2)            #文件指针移动2位
# print(fo.tell())      #打印当前指针位置
# print(fo.read(3))     #打印往后读取的3位

#############################扩展##############################
# fo.seek(x) 扩展用法
# seek(位置，模式)
# 0模式，从头开始算（往后推移--位置）--处理文本文件（txt、log）--返回str
# 1模式，从当前位置开始算--文件打开模式rb--读二进制(bin)--.pcap格式、音视频、图片文件用
# 2模式，从尾部算--rb--读二进制（bin）
###############################################################



# 8、文件读取一行内容
# (1) fo.readline()     #读取一行内容
# file1 = 'D:\\file1.txt'
# fo = open(file1,'r')     #默认是r,可以不写
# print(fo.readline())     #读取一行
# print(fo.readline())     #再读一行    \r  回车  \t  制表符  \n  换行
# fo.close()

# (2) fo.readlines()    #读取多行内容
# 每行作为list的一个元素，行尾是带\n的
# file1 = 'D:\\file1.txt'
# fo = open(file1,'r')
# print(fo.readlines())          #['123456\n', '654321\n', 'abcdef\n', '\n']
# 读取多行内容
# print(fo.read().splitlines())  #['123456', '654321', 'abcdef', '']
# 去除每一个元素换行符操作--返回是个列表
# fo.close()



# 9、文件内容写入
# 写模式---w
# w---只是为了写文件而打开文件。
# 如果文件已经存在，其内容将被清空。如果文件不存在，则创建一个文件。

# file1 = 'D:\\file1.txt'
# fo = open(file1,'w')        #文件存在，会清空file1文件中的内容
# fo.write('taosenlin')       #文件缓冲区buffer,如果打印（有返回值：返回写入内容的长度）
# fo.flush()                  #将文件写入磁盘
# fo.write('12345')           #文件缓冲区buffer,如果打印（有返回值：返回写入内容的长度）
# fo.flush()                  #将文件写入磁盘
# fo.close()                  #关闭文件
#
# file2 = 'D:\\file2.txt'
# fo = open(file2,'w')        #文件不存在,会在磁盘新建file2文件



# 10、追加模式---a
# (1)只是为了在文件末尾追加内容而打开文件
# (2)如果文件存在，文件指针在文件的结尾
# (3)如果文件不存在，则创建一个文件

# 注：很多OS强制写都在末尾，不管文件指针被seek到了什么地方
# file2 = 'D:\\file2.txt'
# fo = open(file2,'a')     #追加模式---文件不存在（新建）--文件存在（尾部追加）
# fo.write('\ntaosenlin')  #加换行符（另起一行添加）--不加换行符（直接尾部添加）
# fo.flush()
# fo.close()

# 注： write() 内部只能写字符串



# 11、文件扩展用法
# (1)r+
# 为了读取并且写文件而打开文件。如果文件不存在，会报错。文件指针在文件开头。

# (2)w+
# 为了读取并且写文件而打开文件。如果文件不存在，会创建一个文件。
# 文件指针在文件的开头。如果文件已经存在，其内容将被清空。

# (3)a+
# 为了读取并且写文件而打开文件。如果文件不存在，会创建一个文件。
# 文件指针在文件的结尾。很多OS上写操作永远在文件结尾进行，不管是否用了seek。



# 12、 with open()用法
# (1)
# file2 = 'D:\\file2.txt'
# with open(file2,'r') as f:
#     fo = f.read()
#        ...
# 执行结束时，系统自动调用f.close()


# (2)
# 支持多个文件的打开
# file2 = 'D:\\file2.txt'
# with open(inFileName) as ifile,open(outFileName,'w') as ofile:
#     fo = ifile.read()
#     ofile.write(fo)
#
# with open(fileDir,'r') as rFile,open('','w') as wFile:
#     print('文件操作')












































































































