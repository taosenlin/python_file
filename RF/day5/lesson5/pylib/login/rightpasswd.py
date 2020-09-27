from robot.api import logger


class SubLibrary2:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def printaddr(self):
        logger.console('SubLibrary2:host:%s,port:%s' % (self.host,self.port))


class rightpasswd:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def printaddr(self):
        logger.console('hello')
        logger.console('rightpasswd:host:%s,ip:%s' % (self.host,self.port))

    def printaddr2(self,host, port=8080):
        logger.console('rightpasswd:host:%s,ip:%s' % (host, port))