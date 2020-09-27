#coding : utf8
#Author : taosenlin
#Time : 2020/7/29 16:33

import os

readfile = 'tclist.txt'

with open(readfile) as ifile,open('comfile.txt','w') as ofile:
    arglines = []
    fo = ifile.read().replace('\n','')
    fo1 = fo.split('|')
    for ele in fo1:
        ele = ele.strip()
        if ele:
            arglines.append('--test *' + ele)

    #去除重复的用例
    argstr = list(set(arglines))
    argstr1 = '\n'.join(argstr)

    argstr1 += '\n--pythonpath .'
    argstr1 += '\ntc'
    # print(argstr1)

    ofile.write(argstr1)

os.system('robot --loglevel debug -A comfile.txt')



















