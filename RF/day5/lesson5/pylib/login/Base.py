from robot.libraries.BuiltIn import logger

class Father():
    def __init__(self):
        print('init Father')
        logger.console('init Father')

    def money(self):
        return '$10000'




if __name__ == '__main__':
    print(Child().use_money())