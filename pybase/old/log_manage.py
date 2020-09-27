# Time:2020-01-07 22:06
# Author:TSL
# 1.下面的log变量记录了云服务器上 当天上传的文件信息
# 其中第一列是文件名，第二列是文件大小
# 请编写一个程序，统计出不同类型的 文件的大小总和
# 比如：
# jpeg  9988999
# json   324324
# png   2423233
#
log = '''
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0
'''

FileTypeSum = []
def type_Sum(fileType,fileSum):
    for one in FileTypeSum:
        if one[0] == fileType:
            one[1] += fileSum
            return

    FileTypeSum.append([fileType,fileSum])
    return

for sen in log.split('\n'):
    if sen.strip() == '':
        continue

    line = sen.split('\t')

    name,size = line[:2]
    form = name.split('.')[-1]

    type_Sum(form,int(size))

print(FileTypeSum)



























































