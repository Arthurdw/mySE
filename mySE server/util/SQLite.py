# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# API created for mySE by Arthurdw                        #
# mySE stands for My Secure Environment!                  #
# mySE was created for GO-Atheneum Oudenaarde             #
# This project and all it files are under a MIT licence.  #
# Project (mySE) started on 09/01/2020!                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file covers all interactions with the mySE db.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sqlite3
from secrets import token_urlsafe


class DataBase:
    def __init__(self, database):
        self.connection = sqlite3.connect("db\\" + database + ".db")

    def close(self):
        self.connection.close()

    def exe(self, executable):
        fetched = self.connection.execute(executable).fetchall()
        self.connection.commit()
        return fetched

    def setup(self, table, fields):
        self.connection.execute(f"CREATE TABLE {table} {fields}")
        self.connection.commit()

    def post_log(self, exe, ins_tuple):
        self.connection.execute(exe, ins_tuple)
        self.connection.commit()

    @property
    def add_token(self, db, id):
        token = None
        while True:
            token = token_urlsafe(32)
            if [_token[0] for _token in db.exe(f"SELECT token from tokens WHERE token = '{token}';")]:
                pass
            else:
                break
        self.connection.execute(f"")
