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

    def add_user(self, username, email, password):
        self.connection.execute(f"INSERT INTO users VALUES (?, ?, ?);", (username, email, password))
        self.connection.commit()
        self.close()

    def add_token(self, mail, _id=None):
        token = None
        while True:
            token = token_urlsafe(32)
            if [_token[0] for _token in self.exe(f"SELECT token from tokens WHERE token = '{token}';")]:  pass
            else: break
        if _id is None:
            try: _id = self.exe("SELECT id from tokens ORDER BY id DESC LIMIT 1")[0][0] + 1
            except IndexError: _id = 1
        self.connection.execute(f"INSERT INTO tokens VALUES (?, ?, ?)", (_id, token, mail))
        self.connection.commit()
        self.close()
        return token
