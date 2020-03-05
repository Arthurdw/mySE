# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# API created for mySE by Arthurdw                        #
# mySE stands for My Secure Environment!                  #
# mySE was created for GO-Atheneum Oudenaarde             #
# This project and all it files are under a MIT licence.  #
# Project (mySE) started on 09/01/2020!                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This is the server (REST API) for the mySE project!     #
# To be able to interact you need to have a token in the  #
# header of your request under 'Authorization'.           #
# This REST API will cover:                               #
#    - the logs for the interface.                        #
#    - token/account generation. (WIP)                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from configparser import ConfigParser
from json import loads
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from util import SQLite, utils
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
secret = ConfigParser()
secret.read("serverSecret.cfg")
CORS(app, supports_credentials=True)

class UserGet(Resource):
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("email")
        params.add_argument("password")
        _mail = str(params.parse_args()["email"]).lower()
        _password = params.parse_args()["password"]
        users_db = SQLite.DataBase("users")
        if users_db.exe(f"SELECT mail FROM users WHERE mail = '{_mail}' AND password = '{_password}';"):
            fetch = users_db.exe(f"SELECT user_name FROM users WHERE mail = '{_mail}' AND password = '{_password}';")[0]
            return {"user_name": fetch[0], "statusCode": 200}
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}


class UserAdd(Resource):
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("email")
        params.add_argument("username")
        params.add_argument("password")
        params.add_argument("serverSecret")
        _mail = str(params.parse_args()["email"]).lower()
        _password = params.parse_args()["password"]
        _username = params.parse_args()["username"]
        if params.parse_args()["serverSecret"] == secret["SECRET"]["secret"]:
            users_db = SQLite.DataBase("users")
            if not users_db.exe(f"SELECT mail FROM users WHERE mail = '{_mail}' AND password = '{_password}';"):
                users_db.add_user(_username, _mail, _password)
                return {"user_name": _username, "statusCode": 200}
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}


class TokenGet(Resource):
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("email")
        _mail = str(params.parse_args()["email"]).lower()
        tokens_db = SQLite.DataBase("tokens")
        if _mail in [mail[0] for mail in tokens_db.exe("SELECT mail FROM tokens;")]:
            fetch = tokens_db.exe(f"SELECT id, token FROM tokens WHERE mail = '{_mail}'")[0]
            return {"id": fetch[0], "token": fetch[1], "statusCode": 200}
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}


class TokenAdd(Resource):
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument("email")
        params.add_argument("serverSecret")
        _mail = str(params.parse_args()["email"]).lower()
        tokens_db = SQLite.DataBase("tokens")
        if params.parse_args()["serverSecret"] == secret["SECRET"]["secret"]:
            if _mail not in [mail[0] for mail in tokens_db.exe("SELECT mail FROM tokens;")]:
                return {"token": tokens_db.add_token(_mail), "statusCode": 200}
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}


class LogsGet(Resource):
    def post(self):
        user_token = request.headers.get('Authorization')
        tokens_db = SQLite.DataBase("tokens")
        if user_token in [token[0] for token in tokens_db.exe("SELECT token FROM tokens;")]:
            logs_db = SQLite.DataBase("logs")
            user_id = tokens_db.exe(f"SELECT id FROM tokens WHERE token = '{user_token}'")[0]
            db = logs_db.exe(f"SELECT * FROM logs WHERE id = {user_id[0]};")
            tokens_db.close()
            logs_db.close()
            return {"id": user_id[0],
                    "logs": [{"time": data[1], "light": True if data[2] == 1 else False, "id": data[3]} for data in db],
                    "statusCode": 200}
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}


class LogsAdd(Resource):
    def post(self):
        user_token = request.headers.get('Authorization')
        tokens_db = SQLite.DataBase("tokens")
        if user_token in [token[0] for token in tokens_db.exe("SELECT token FROM tokens;")]:
            logs_db = SQLite.DataBase("logs")
            params = reqparse.RequestParser()
            params.add_argument("light")
            user_id = tokens_db.exe(f"SELECT id FROM tokens WHERE token = '{user_token}'")[0][0]
            light = 1 if len(params.parse_args()["light"]) == 4 else 0
            count = 1
            try:
                count = logs_db.exe("SELECT breach from logs ORDER BY breach DESC LIMIT 1")[0][0] + 1
            except IndexError:
                count = 1
            logs_db.post_log("INSERT INTO logs VALUES (?, ?, ?, ?)", (user_id, str(utils.date()), light, count))
            db = logs_db.exe(f"SELECT * FROM logs WHERE id = {user_id} AND breach = {count};")
            tokens_db.close()
            logs_db.close()
            return {"id": user_id,
                    "logs": [{"time": data[1], "light": params.parse_args()["light"], "id": data[3]} for data in db],
                    "statusCode": 200}
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}


api.add_resource(UserAdd, "/user/add/")
api.add_resource(UserGet, "/user/")
api.add_resource(LogsAdd, "/logs/add/")
api.add_resource(LogsGet, "/logs/")
api.add_resource(TokenAdd, "/token/add/")
api.add_resource(TokenGet, "/token/")

if __name__ == "__main__":
    app.run(debug=True)
