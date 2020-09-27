# Time:2020-02-26 22:43
# Author:TSL

# 元素定位工具1
# Android SDK中的 uiautomateviewer
# 在目录 .\Android\sdk\tools\bin\uiautomateviewer.bat



# 一、根据ID
#
# （1）元素的resource id属性

# driver.find_element_by_id('')
# 缺点：有时候并非唯一
# a、
# 使用 uiautomateviewer 将app的界面树形结构打开，然后保存到桌面
# 通过编辑器打开界面元素的xml形式，当resource id 元素不唯一时，
# 可以通过 bounds（坐标）去判断取第几个的下标


# 注：通过WebDriver查找范围是整个界面树形结构
    # 通过WebElement查找范围是该节点的子节点



# 二、根据CLASS NAME

# (1)class属性决定了界面元素的类型

# (2)使用场景：
# a、我们要查找的是某种类型的界面元素
# b、而且这种类型的界面元素在当前界面中只有一个
# driver.find_element_by_class_name('')



# 三、根据ACCESSIBILITY ID

# (1)content-desc属性是用来描述该元素的作用

# (2)要查询的界面元素的content-desc属性在当前界面中唯一
# driver.find_element_by_accessibility_id('')



# 注意：
# Appium选择元素套路
# 和Selenium选择元素套路基本相同

# find_element_by_xxx 符合条件的第一个元素，找不到抛出异常
# find_elements_by_xxx 符合条件的所有元素的列表，找不到返回空列表
# 通过 WebDriver 查找范围是整个界面树形结构
# 通过 WebElement 查找范围是该节点的子节点



































