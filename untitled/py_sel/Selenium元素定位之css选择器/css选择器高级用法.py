#coding : utf8
#Author : taosenlin
#Time : 2020/3/30 14:48

# css相比较xpath选择元素优点如下：
# 表达式更加简洁
# 一般情况css的运行速度要优于xpath


# 一、常用的CSS选择器大致分为以下几种：

# 1、基础选择器：
# 基础选择器包括：
# 标签：直接使用标签名，如下列：  P

# 类（class）： "."(英文符号)+class值

# id: "#"+id值

# 通配符: 匹配所有元素,用"*"表示



# 2、组合选择器
# 组合选择器就是将基础选择器的方法进行混合使用,有如下几种方式：

# (1)标签指定选择：以标签为基本选择再连接id或class进行综合选择 如：p #title

# (2)后代选择：可以选择父类以下所有的子类（既能选中儿子也能选中孙子以及所有后代），
# 相比较子代选择，后代选择范围更广。后代选择使用空格连接 父类到子类及下面类的元素。

# (3)子代选择：通过父类选择子类，只能选中子类，不包含子类的子类（即只能选中儿子，
# 不能选中孙子）。使用 ">" 连接，子代选择只能选择子类中的第一个子类，不能选择子类的子类。

# (4)并集选择：将多个选择使用 "," 连接，表示"和"的意思



# 3、属性选择器
# 属性选择器是运用标签中的属性进行定位，比如标签中常用的text、title、id、class属性等


















































































