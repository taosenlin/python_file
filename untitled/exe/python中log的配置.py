#coding : utf8
#Author : taosenlin
#Time : 2020/6/9 15:22

"""
# 一、
# 第一种使用方式：简单配置
import logging
logging.debug("debug_msg")
logging.info("info_msg")
logging.warning("warning_msg")
logging.error("error_msg")
logging.critical("critical_mag")
# WARNING:root:warning_msg
# ERROR:root:error_msg
# CRITICAL:root:critical_mag

# 默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
# 这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）
# 默认输出格式为:  默认的日志格式为日志级别：Logger名称：用户输出消息
"""


"""
# 二、
# 这里可以用 logging.basicConfig()函数调整日志级别、输出格式等
import logging
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d %H:%M:%S %a'  #这里的格式化符与time模块相同
                   )
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")
# 2020-06-10 14:16:48 Wed root DEBUG msg1
# 2020-06-10 14:16:48 Wed root INFO msg2
# 2020-06-10 14:16:48 Wed root WARNING msg3
# 2020-06-10 14:16:48 Wed root ERROR msg4
# 2020-06-10 14:16:48 Wed root CRITICAL msg5
"""


# logging.basicConfig()函数包含参数说明
# filename   指定日志输出目标文件的文件名（可以写文件名也可以写文件的完整的绝对路径，写文件名日志放执行文件目录下，
#            写完整路径按照完整路径生成日志文件），指定该设置项后日志信心就不会被输出到控制台了
# filemode   指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
# format     指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
# datefmt    指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
# level      指定日志器的日志级别

# logging模块中定义好的可以用于format格式字符串说明
# 字段/属性名称              使用格式                                            描述
# asctime                   %(asctime)s                         将日志的时间构造成可读的形式，默认情况下是‘2016-02-08 12:00:00,123’精确到毫秒
# name                      %(name)s                            所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
# filename                  %(filename)s                        调用日志输出函数的模块的文件名； pathname的文件名部分，包含文件后缀
# funcName                  %(funcName)s                        由哪个function发出的log， 调用日志输出函数的函数名
# levelname                 %(levelname)s                       日志的最终等级（被filter修改后的）
# message                   %(message)s                         日志信息， 日志记录的文本内容


# 三、
"""
import logging
LOG_FROMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"
logging.basicConfig(level=logging.DEBUG,
                    format = LOG_FROMAT,
                    datefmt = DATE_FORMAT,
                    filename= r'E:\test.log'
                    )
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")
"""

# 说明：
# 1、logging.basicConfig()函数是一个一次性的简单配置工具使，也就是说只有在第一次调用该函数时会起作用，
# 后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作。
# 2、日志器（Logger）是有层级关系的，上面调用的logging模块级别的函数所使用的日志器是RootLogger类的实例，
# 其名称为'root'，它是处于日志器层级关系最顶层的日志器，且该实例是以单例模式存在的。
# 3、如果要记录的日志中包含变量数据，可使用一个格式字符串作为这个事件的描述消息（logging.debug、logging.info等函数的第一个参数），
# 然后将变量数据作为第二个参数*args的值进行传递。
# import logging
# logging.warning("%s is %d years old.","tom",10)



# 四、
# 第二种使用方式：日志流处理流程
# 1、logging.basicConfig()（用默认日志格式（Formatter）为日志系统建立一个默认的流处理器（StreamHandler），
# 设置基础配置（如日志级别等）并加到root logger（根Logger）中）这几个logging模块级别的函数。
# 2、第二种是一个模块级别的函数是logging.getLogger([name])（返回一个logger对象，如果没有指定名字将返回root logger）。

# logging日志模块四大组件：
# 日志器     Logger          提供了应用程序可一直使用的接口
# 处理器     Handler         将logger创建的日志记录发送到合适的目的输出
# 过滤器     Filter          提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
# 格式器     Formatter       决定日志记录的最终输出格式
# logging模块就是通过这些组件来完成日志处理的，上面所使用的logging模块级别的函数也是通过这些组件对应的类来实现的。

# 这些组件之间的关系描述：
# 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
# 不同的处理器（handler）可以将日志输出到不同的位置；
# 日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
# 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
# 每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。

# 简单点说就是：日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和
# 格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。



# 1、Logger类
# Logger对象有3个任务要做：
# 1）向应用程序代码暴露几个方法，使应用程序可以在运行时记录日志消息；
# 2）基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理；
# 3）将日志消息传送给所有感兴趣的日志handlers。

# Logger对象最常用的方法分为两类：配置方法 和 消息发送方法
# 最常用的配置方法如下：
#                     方法                                                       描述
#                Logger.setLevel()                                 设置日志器将会处理的日志消息的最低严重级别
#   Logger.addHandler() 和 Logger.removeHandler()                  为该logger对象添加 和 移除一个handler对象
#   Logger.addFilter() 和 Logger.removeFilter()                    为该logger对象添加 和 移除一个filter对象


# logger对象配置完成后，可以使用下面的方法来创建日志记录：
#                                            方法                                                                  描述
#    Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical()              创建一个与它们的方法名对应等级的日志记录
#                                      Logger.exception()                                            创建一个类似于Logger.error()的日志消息
#                                         Logger.log()                                               需要获取一个明确的日志level参数来创建一个日志记录

# 一个Logger对象呢？一种方式是通过Logger类的实例化方法创建一个Logger类的实例，但是我们通常都是用第二种方式--logging.getLogger()方法。
# logging.getLogger()方法有一个可选参数name，该参数表示将要返回的日志器的名称标识，如果不提供该参数，则其值为'root'。
# 若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。

# 多次使用注意不能创建多个logger,否则会出现重复输出日志现象。



# 2、Handler类
# Handler对象的作用是（基于日志消息的level）将消息分发到handler指定的位置（文件、网络、邮件等）。
# Logger对象可以通过addHandler()方法为自己添加0个或者更多个handler对象。
# 比如，一个应用程序可能想要实现以下几个日志需求：
# 1）把所有日志都发送到一个日志文件中；
# 2）把所有严重级别大于等于error的日志发送到stdout（标准输出）；
# 3）把所有严重级别为critical的日志发送到一个email邮件地址。
#    这种场景就需要3个不同的handlers，每个handler复杂发送一个特定严重级别的日志到一个特定的位置。

# Handler.setLevel(lel): 指定被处理的信息级别，低于lel级别的信息将被忽略
# Handler.setFormatter()：给这个handler选择一个格式
# Handler.addFilter(filt)、Handler.removeFilter(filt)：新增或删除一个filter对象

# 需要说明的是，应用程序代码不应该直接实例化和使用Handler实例。因为Handler是一个基类，
# 它只定义了素有handlers都应该有的接口，同时提供了一些子类可以直接使用或覆盖的默认行为。
# 下面是一些常用的Handler：
#                              Handler                                                 描述
#                         logging.StreamHandler                  将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
#                         logging.FileHandler                    将日志消息发送到磁盘文件，默认情况下文件大小会无限增长



# 3、formater类
# Formater对象用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用代码可以直接实例化Formatter类。
# 另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。

# Formatter类的构造方法定义如下：
# logging.Formatter.__init__(fmt=None, datefmt=None, style='%')

# 可见，该构造方法接收3个可选参数：
# fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
# datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
# style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'

# 一般直接用logging.Formatter（fmt, datefmt）



# 4、Filter类（暂时了解）
# Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。
# Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤。
# 该类定义如下：
'''
class logging.Filter(name='')
    filter(record)
'''
# 比如，一个filter实例化时传递的name参数值为'A.B'，那么该filter实例将只允许名称为类似如下规则的loggers产生的日志记录通过过滤：'A.B'，'A.B.C'，'A.B.C.D'，'A.B.D'，
# 而名称为'A.BB', 'B.A.B'的loggers产生的日志则会被过滤掉。如果name的值为空字符串，则允许所有的日志事件通过过滤。

# filter方法用于具体控制传递的record记录是否能通过过滤，如果该方法返回值为0表示不能通过过滤，返回值为非0表示可以通过过滤。
# 说明：
# 如果有需要，也可以在filter(record)方法内部改变该record，比如添加、删除或修改一些属性。
# 我们还可以通过filter做一些统计工作，比如可以计算下被一个特殊的logger或handler所处理的record数量等。



# 日志流处理简要流程
# 1、创建一个logger
# 2、设置下logger的日志的等级
# 3、创建合适的Handler(FileHandler要有路径)
# 4、设置下每个Handler的日志等级
# 5、创建下日志的格式
# 6、向Handler中添加上面创建的格式
# 7、将上面创建的Handler添加到logger中
# 8、打印输出logger.debug\logger.info\logger.warning\logger.error\logger.critical



"""
import logging

# 创建logger,如果参数为空则返回root logger
logger = logging.getLogger("tsl")
logger.setLevel(logging.DEBUG)    #设置logger日志等级

# 创建handler
fh = logging.FileHandler("test.log",encoding="utf-8")
sh = logging.StreamHandler()

# 设置输出日志格式
formatter = logging.Formatter(fmt= "%(asctime)s %(name)s %(filename)s %(message)s",
                              datefmt= "%Y-%m-%d %H:%M:%S %a"
                            )
# 注意logging.Formatter的大小写

# 为handler指定输出格式，注意大小写
fh.setFormatter(formatter)
sh.setFormatter(formatter)

# 为logger添加日志处理器
logger.addHandler(fh)
logger.addHandler(sh)

# 输出不同级别的log
logger.warning("警告")
logger.info("提示")
logger.error("错误")
"""


# python logging 重复写日志问题
# 用Python的logging模块记录日志时，可能会遇到重复记录日志的问题，第一条记录写一次，第二条记录写两次，第三条记录写三次
# 原因：没有移除handler 解决：在日志记录完之后removeHandler


"""
import logging

def log(msg):
    # 创建logger,如果参数为空则返回root logger
    logger = logging.getLogger("tsl")
    logger.setLevel(logging.DEBUG)    #设置logger日志等级

    # 创建handler
    fh = logging.FileHandler("test.log",encoding="utf-8")
    sh = logging.StreamHandler()

    # 设置输出日志格式
    formatter = logging.Formatter(fmt= "%(asctime)s %(name)s %(filename)s %(message)s",
                                  datefmt= "%Y-%m-%d %H:%M:%S %a"
                                )
    # 注意logging.Formatter的大小写

    # 为handler指定输出格式，注意大小写
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    # 为logger添加日志处理器
    logger.addHandler(fh)
    logger.addHandler(sh)

    # 输出不同级别的log
    logger.info(msg)

log('警告')
log('提示')
log('错误')
"""

# 分析：可以看到输出结果有重复打印
# 原因：第二次调用log的时候，根据getLogger(name)里的name获取同一个logger，而这个logger里已经有了第一次你添加的handler，
# 第二次调用又添加了一个handler，所以，这个logger里有了两个同样的handler，以此类推，调用几次就会有几个handler。


# 解决方案1
# 添加removeHandler语句

"""
import logging

def log(msg):
    # 创建logger,如果参数为空则返回root logger
    logger = logging.getLogger("tsl")
    logger.setLevel(logging.DEBUG)    #设置logger日志等级

    # 创建handler
    fh = logging.FileHandler("test.log",encoding="utf-8")
    sh = logging.StreamHandler()

    # 设置输出日志格式
    formatter = logging.Formatter(fmt= "%(asctime)s %(name)s %(filename)s %(message)s",
                                  datefmt= "%Y-%m-%d %H:%M:%S %a"
                                )
    # 注意logging.Formatter的大小写

    # 为handler指定输出格式，注意大小写
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    # 为logger添加日志处理器
    logger.addHandler(fh)
    logger.addHandler(sh)

    # 输出不同级别的log
    logger.info(msg)

    # 解决方案1,添加removeHandler,每次用完之后移除handler
    logger.removeHandler(fh)
    logger.removeHandler(sh)

log('警告')
log('提示')
log('错误')
"""


# 解决方案2
# 在log方法里做判断，如果这个logger已有handler，则不再添加handler。

"""
import logging

def log(msg):
    # 创建logger,如果参数为空则返回root logger
    logger = logging.getLogger("tsl")
    logger.setLevel(logging.DEBUG)    #设置logger日志等级

    if not logger.handlers:
        # 创建handler
        fh = logging.FileHandler("test.log",encoding="utf-8")
        sh = logging.StreamHandler()

        # 设置输出日志格式
        formatter = logging.Formatter(fmt= "%(asctime)s %(name)s %(filename)s %(message)s",
                                      datefmt= "%Y-%m-%d %H:%M:%S %a"
                                    )
        # 注意logging.Formatter的大小写

        # 为handler指定输出格式，注意大小写
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        # 为logger添加日志处理器
        logger.addHandler(fh)
        logger.addHandler(sh)

    # 输出不同级别的log
    logger.info(msg)

    # # 解决方案1,添加removeHandler,每次用完之后移除handler
    # logger.removeHandler(fh)
    # logger.removeHandler(sh)

log('警告1')
log('提示1')
log('错误1')
"""


# logger调用方式例子

import logging

def log():
    # 创建logger,如果参数为空则返回root logger
    logger = logging.getLogger("tsl")
    logger.setLevel(logging.DEBUG)    #设置logger日志等级

    if not logger.handlers:
        # 创建handler
        fh = logging.FileHandler("test.log",encoding="utf-8")
        sh = logging.StreamHandler()

        # 设置输出日志格式
        formatter = logging.Formatter(fmt= "%(asctime)s %(name)s %(filename)s %(message)s",
                                      datefmt= "%Y-%m-%d %H:%M:%S %a"
                                    )
        # 注意logging.Formatter的大小写

        # 为handler指定输出格式，注意大小写
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        # 为logger添加日志处理器
        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger   # 直接返回logger

logger = log()
logger.warning("警告2")
logger.info("提示2")
logger.error("错误2")





















































