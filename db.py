import os

from lib import Singleton
import mysql.connector 


class DB(object, metaclass=Singleton):
    def __init__(self):
        self.host = os.environ.get('MYSQL_HOST', 'localhost')
        self.user = 'root'
        self.passwd = 'password'
        self.db_name = 'testdb'
        self.connection = None

    def clean_connection(self):
        self.connection = None

    def get_connection(self, dictionary=True):
        self.connect()
        cursor = self.connection.cursor(dictionary=dictionary)
        return cursor

    def start_transaction(self):
        self.connect()
        self.connection.start_transaction(isolation_level='READ COMMITTED')

    def connect(self):
        if self.connection is None:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.db_name,
                autocommit=True
            )

    def commit(self):
        self.connection.commit()
