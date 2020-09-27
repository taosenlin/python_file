# coding:utf8
# Time:2020-04-07 22:20
# Author:TSL

# 一、自动化项目的目录结构
# 1、已经接触到项目文件种类

# 测试套件文件、目录
# RF资源文件
# 测试库
# 变量文件


# 2、建议的目录结构
# 参考task
# pylib中存放库关键字
# rflib中存放公共的资源文件
# tc中存放用例的主体部分，测试套件目录，子套件（套件文件）；可以根据模块和功能点进行分割
# cfg.py中存放全局配置文件


# 3、以 robot --pythonpath . tc 命令执行tc用例下面所有的用例

# 4、builtin库里面的Run Keywords 方法实现初始化



# 二、RF用例的执行
# 1、Robot Framework 的命令格式
# robot [options] data sources

# (1)options是RF命令的选项，可以为空

# (2)data sources则是要执行的测试套件文件或目录的路径。可以是绝对路径，也可以是相对路径，
# 相对于当前shell的工作目录
# robot tests.robot
# robot path/to/my_tests/
# robot c:\robot\tests.robot

# (3)如果指定的是测试套件文件，则执行该文件中所有的测试用例

# (4)如果指定的是测试套件目录，则递归执行该目录下包含的所有的子目录里面所有测试套件
# 文件里面的用例



# 2、可以指定多个要执行的测试套件文件、目录，甚至用通配符来表示多个测试，如下所示：
# robot my_tests.robot your_tests.robot
# robot --name Example path/to/tests/pattern_*.robot

# (1)多个测试数据的情况，本次测试的名称就是把它们的名字相加
# My Tests & Your Tests

# (2)用 --name选项来指定本次测试名称，像上面第二行所示。
# robot --pythonpath . --name 回归测试 tc



# 3、根据名称选择测试用例
# 我们可以通过 --test --suite来指定执行那些用例或者套件，而且还支持用通配符的方式

# --test Example   简写(-t)           #执行名为example的用例
# --test mytest  --test yourtest     #执行名为mytest和yourtest的用例
# --test example*                    #执行名字以example开头的用例
# --suite mysuite  简写(-s)           #执行名为mysuite的套件



# 4、参数文件
# 如果有时候，参数太长，我们通常可以使用参数文件，我们可以把所有的参数都放在参数文件中
# 比如：argfile

# --pythonpath .
# --name 回归测试
# --test *tc00001
# --test *tc00002
# --test *tc00003
# --test *tc00004
# --test *tc00005
# t1.robot

# 命令就只需要  robot -A argfile t1.robot
# -A 表示arguments


# 三、RF用例标签
# 测试用例也可以有多个标签，根据任何一个标签都可以过滤到该用例

# 1、Settings表里的 Force Tags
#(1)该套件里面所有测试用例都具有了该tag

# 2、测试用例表里的 [tags] 配置

# 3、Settings 表里的 Default Tags

#(1)该套件里面所有 没有[tags] 设置的测试用例都具有了该tag
#(2)测试目录里面的 __init__.robot 不支持Default Tags(测试目录中只能存在Force Tags标签)


# 4、根据标签选择测试用例

#执行包含 标签'foo'的用例
# --include foo
#执行不包含 标签'foo'的用例
# --exclude foo

#执行同时包含 标签'one','web test'的用例
# --include oneAND"web test"

#执行包含 标签'one'或者'two'的用例
# --include oneORtwo

#执行包含 标签'one'但是不包含标签'two'的用例
# --include oneNOTtwo

#执行 标签格式为 W*W的用例
# --include w*w


# 5、举例说明
# robot --include web测试   "webtest"
# robot --include 冒烟测试   "webtest"
# robot --include admin   "webtest"
# robot --include admin   --include teacher   "webtest"
# robot --include "admin"AND"teacher"    "webtest"
# robot --include "admin"OR"teacher"     "webtest"
# robot --include notag    "webtest"
# robot --include *    "webtest"



# 四、指定关键测试用例
# 1、如果本次测试中有关键测试用例没有通过，那么整个测试就被视为测试不通过。
#    反之，整个测试就视为通过

# (1)缺省情况下，RF执行测试时，每个测试用例都被视为关键测试用例

# (2)我们可以通过命令参数 --critical (-c) 和 --noncritical (-n) 后面加 tag 名称
# 来指定测试用例是否为关键测试用例

# --critical regression 指定 只有具有 regression 标签的用例才是关键用例
# --noncritical not_ready 指定 不具有 not_ready 标签的用例是关键用例，其他用例
# 都不是关键用例
# --critical ok*  --noncritical tbd*  指定 具有 以ok开头的标签且没有以tbd开头的
# 标签的用例都是关键用例，其他用例都不是关键用例

# (3)通常我们可以在关键用例中打上标签，比如 basic 表示是关键用例









































































































































