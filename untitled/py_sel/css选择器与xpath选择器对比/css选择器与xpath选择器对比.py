#coding : utf8
#Author : taosenlin
#Time : 2020/3/31 16:19

# Sizzle Css3还提供一些直接选取form表单元素的伪类

# :input: Finds all input elements (includes textareas, selects, and buttons).

# :text, :checkbox, :file, :password, :submit, :image, :reset,
# :button: Finds the input element with the specified input type
# (:button also finds button elements).



# 定位方式             XPath                                   CSS

# 标签                 //div                                   div


# By id                //div[@id='eleid']                      div #eleid


# By class             //div[@class='eleclass']                div .eleclass
#                      //div[contains(@class,'eleclass')]


# By 属性              //div[@title='Move mouse here']         div[title=Move mouse here]
#                                                              div[title^=Move]
#                                                              div[title$=here]
#                                                              div[title*=mouse]


# 定位子元素           //div[@id='eleid']/*                     div #eleid > *
#                     //div/h1                                 div #eleid > h1


# 定位后代元素         //div[@id='eleid']//h1                   div h1


# By index(索引)      //li[6]                                   li:nth(5)


# By content          //a[contains(.;'Issue 1164')]             a:contains(Issue 1164)


# 根据子元素回溯       //li[a[contains(.;'Issue 1244')]]         li{a:contains(Issue 1244)}
# 定位父元素           //*[./a[contains(.;'Issue 1244')]]        ul{a:contains(Issue 1244)}
#                     //ul[.//a[contains(.;'Issue 1244')]]


# 根据邻近元素定位     //li[preceding-sibling::li[contains(.;'Issue 1244')]]               css=li:contains(Issue 1244) + li
#                     //ul[preceding-sibling::ul[.//a[contains(.;'Issue 1244')]]]         css=ul{a:contains(Issue 1244)} ~ ul
















































































