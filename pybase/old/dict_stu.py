# Time:2020-01-14 21:35
# Author:TSL
fileName = r'D:\\0005_1.txt'
with open(fileName) as fo:
    fc = fo.read().splitlines()
    for line in fc:
        print(line)
    # print(fc)
