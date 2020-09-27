# Time:2020-02-27 22:12
# Author:TSL

# 一、Xpath在appinum中的原理

# (1)在Appinum中，没法使用css，因为css是web专用的
#
# (2)与web不同，底层测试驱动并不识别XPATH
#
# (3)Appinum负责解析xpath给底层测试驱动来识别
#
# (4)每个节点名对应元素的class属性
#
# (5)对于一些比较复杂的元素定位，我们可以用它定位
# driver.find_element_by_xpath('//ele1/ele2[@attr="a1"]')



# 二、Xpath在appinum中的应用

# xpath表达式：
# (1)通过ID选择
# //*[@resource-id="com.hpbr.bosszhipin:id/view_job_card"]

# (2)通过CLASS选择
# //android.view.ViewGroup      //*[@class="android.view.ViewGroup"]

# (3)通过其他属性选择
# //*[@属性="属性值"]

# (4)选择子元素/后代元素
# //*[@属性="属性值"]/*        //*[@属性="属性值"]//*

# (5)选择父元素
# //*[@属性="属性值"]/..






























