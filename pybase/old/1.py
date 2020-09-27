# Time:2020-01-07 23:34
# Author:TSL

log = '''
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0
'''

fileLenTable = []

# 根据文件类型找到记录对象,进行累加
def putRecordToTable(fileType,fileLen):
    for one in fileLenTable:
        if one[0] == fileType:
            one[1] += fileLen
            return

    # 没有找到,创建一个记录元素
    fileLenTable.append([fileType,fileLen])
    return


for line in log.split('\n'):
    if line.strip() == '':
        continue

    parts = line.split('\t')
    name,size = parts[:2]

    ext = name.split('.')[-1]

    putRecordToTable(ext,int(size))


print(fileLenTable)