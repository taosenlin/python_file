#coding : utf8
#Author : taosenlin
#Time : 2020/3/30 18:10

# Selenium中的xpath定位
# XPath即为XML路径语言，它是一种用来确定XML1文档中某部分位置的语言。


# 一、xpath属性定位
# 1、xpath通过元素的id、name、class这些属性定位

#  //*[@id='kw']     //*[@name='wd']     //*[@class='s_ipt']



# 二、xpath其他属性
# 1、如果一个元素id、name、class属性都没有，这时候也可以通过其他属性定位到

#  //*[@autocomplete='off']



# 三、xpath标签
# 1、有时候同一个属性，同名的比较多，这时候可以通过标签筛选下，定位更准确
# 2、如果不想制定标签名称，可以用 * 号表示任意标签
# 3、如果想制定具体某个标签，就可以直接写标签名称

#  //input[@autocomplete='off']
#  //input[@id='kw']
#  //input[@name='wd']



# 四、xpath层级
# 1、如果一个元素，它的属性不是很明显，无法直接定位到，这时我们可以先定位其父元素
# 2、找到其父元素，再找下个层级就能定位到
# <form id="form"
#     <span id="s_kw_wrap"
#         <span class="soutu-btn"
#         <input id="kw" class="s_ipt"
# 3、如上图所示，要定位的是input这个标签，它的父元素的 id=s_kw_wrap
# 4、如果它父元素的属性也不是很明显，可以再往上层找父元素的父元素
# 5、于是就可以通过层级关系定位到目标元素

# 通过定位它父元素来定位input输入框
#  //span[@id='s_kw_wrap']/input
# 通过定位它父元素的父元素来定位input输入框
#  //form[@id='form']/span/input



# 五、xpath索引
# 1、如果一个元素它的兄弟元素跟它的标签一样，这时无法通过层级定位到。
# 2、此时可以根据它在html中的排行位置定位
# <td id="se-setting-3"
#     <select id="nr" name="NR"
#         <option selected=""
#         <option value="20"
#         <option value="50"
# 3、如上图所示，用xpath定位三个元素(这里索引是从1开始算起的，跟python的索引不一样)

#用xpath定位第一个
#  //select[@id='nr']/option[1]
# 用xpath定位第二个
#  //select[@id='nr']/option[2]
# 用xpath定位第三个
#  //select[@id='nr']/option[3]



# 六、xpath逻辑运算
# 1、xpath还有一个比较强的功能，可以多个属性逻辑运算，支持 与(and)、或(or)、非(not)
# 2、一般用的比较多的是 and 运算，同时满足两个属性

#  //*[@id='kw' and @autocomplete='off']



# 七、xpath模糊匹配
# 1、xpath还有一个非常强大的功能，模糊匹配
# 2、掌握模糊匹配功能，基本上没有定位不到的
# 3、比如定位百度页面的超链接 "hao123" ,可以通过by_link,也可以通过
# by_partial_link 模糊匹配定位到。xpath也有同样的功能。

# xpath模糊匹配功能
#  //*[contains(text(),'hao123')]
# xpath也可以模糊匹配某个属性
#  //*[contains(@id,'kw')]
# xpath可以模糊匹配以什么开头
#  //*[starts-with(@id,'s_kw_')]
# xpath可以模糊匹配以什么结尾
#  //*[ends-with(@id,'kw_wrap')]
# xpath还支持最强的正则表达式
#  //*[matchs(text(),'hao123')]



# 八、父子、兄弟、相邻节点定位
# 1、由父节点定位子节点

# 根据B节点定位无id的子节点
# (1)串联查找
# driver.find_element_by_id('B').find_element_by_tag_name('div')

# (2)xpath父子关系寻找
# //div[@id='B']/div

# (3)css父子关系寻找
# div#B>div

# (4)css nth-child
# div#B div:nth-child(1)

# (5)css nth-of-type
# div#B div:nth-of-type(1)

# (6)xpath轴 child
# //div[@id='B']/child::div



# 2、由子节点定位父节点

# 根据C节点定位其两层父节点的div
# (1)xpath: '.' 代表当前节点; '..' 代表父节点
# //div[@id='C']/../..

# (2)xpath轴 parent
# //div[@id='C']/parent::*/parent::div



# 3、由弟弟节点定位哥哥节点

# 根据D节点定位其哥哥节点
# (1)xpath通过父节点获取其哥哥节点
# //div[@id='D']/../div[1]

# (2)xpath轴 preceding-sibling
# //div[@id='D']/preceding-sibling::div[1]



# 4、由哥哥节点定位弟弟节点

# 根据D节点定位其弟弟节点
# (1)xpath通过父节点获取其弟弟节点
# //div[@id='D']/../div[3]

# (2)xpath轴 following-sibling
# //div[@id='D']/following-sibling::div[1]

# (3)xpath轴 following
# //div[@id='D']/following::*

# (4)css +  ( + 表示紧跟在当前节点之后的div节点)
# div#D + div

# (5)css ~  ( ~ 表示当前节点之后的div节点，如果用find_elements，则可获取到一组div节点)
# div#D ~ div





































