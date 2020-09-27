# Time:2020-03-07 21:54
# Author:TSL

import requests
import re
import xlwt

#-----------------存储初始化--------------------------
# 创建一个excel文件
workBook = xlwt.Workbook(encoding='utf-8')
# 在文件对象创建一个sheet
workSheet = workBook.add_sheet('testplay')
line = 0
#创建列名
colName = ['工作名称','公司名称','地址','薪水','时间']
for col in range(len(colName)):
    workSheet.write(line,col,colName[col])  #（行，列，内容）



# 1、--------------------模拟浏览器请求-----------------------------------
#拿到所有页的页码
def get_webPages():
    web_url = 'https://search.51job.com/list/020000%252C040000%252C010000%252C030200,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    r = requests.get(web_url)
    r.encoding = 'gbk'
    pages = re.findall('<span class="td">共(.*?)页，到第</span>',r.text,re.S)[0]
    return int(pages)
# print(get_webPages())


#--------------------------------获取所有页的数据-------------------------------------
for i in range(1,get_webPages()+1):
    web_url = f'https://search.51job.com/list/020000%252C040000%252C010000%252C030200,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{i}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    r = requests.get(web_url)

# 2、------------------------------解析页面内容-----------------------------------------
    r.encoding = 'gbk'
    # print(r.text)             #返回是字符串
    # print(r.request.headers)  #获取请求头
    # print(r.request.body)     #获取请求体
    # print(r.headers)          #获取响应头

# 3、-------------------------------提取需要的数据-----------------------------------------
    #获取页面所有信息数据
    info = re.findall('<div class="el">(.*?)</div>',r.text,re.S)
    # print(info[0])
    #对每一个信息提取数据
    for one in info:
        # 获取工作名称
        temp = re.findall('<a target="_blank" title="(.*?)" href=',one,re.S)
        jobName = temp[0]
        #公司名称
        companyName = temp[1]
        #公司地址
        address = re.findall('<span class="t3">(.*?)</span>',one,re.S)[0]
        #薪资
        salary = re.findall('<span class="t4">(.*?)</span>',one,re.S)[0]
        #发布时间
        time = re.findall('<span class="t5">(.*?)</span>',one,re.S)[0]
        # print(jobName,companyName,address,salary,time)

    # for xx:
    #     jobName,companyName,address,salary,time =get(info)
        line += 1
        colNames = [jobName,companyName,address,salary,time]
        for col in range(len(colNames)):
            workSheet.write(line,col,colNames[col])

# 4、-------------------------------写入爬取结果excel表中-----------------------------------
    # 存储数据---写进去excel
    # workSheet.write()
# 存放到具体磁盘路径
workBook.save('D:\\testPlay.xls')



'''
https://search.51job.com/list/020000%252C040000%252C010000%252C030200,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
https://search.51job.com/list/020000%252C040000%252C010000%252C030200,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
'''





















































