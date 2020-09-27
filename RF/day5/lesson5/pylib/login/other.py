# from robot.libraries.BuiltIn import logger
from robot.api import logger
from pylib.login.Base import Father

class Child(Father):
    def __init__(self):
        Father.__init__(self)
        print('init child')
        logger.console('init Child')


    def use_money(self):
        return self.money()

    def make_money(self):
        return '$9999'

if __name__ == '__main__':
    print(Child().money())