import pymysql

class connection_mysql():
    def __init__(self,connect_key):
        self.mysql = {'host': '', 'port': 3306, 'user': 'root', 'passwd': '', 'db': '', 'charset': 'utf8'}
        if connect_key == 'test':
            self.mysql['host'] = '188.188.0.49'
            self.mysql['passwd'] = '123456'
            self.mysql['db'] = 'wb_league'


