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

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from json import dumps
from util import SQLite, utils


app = Flask(__name__)
api = Api(app)


# class Token(Resource):
#     def post(self):


class Logs(Resource):
    def get(self):
        user_token = request.headers.get('Authorization')
        tokens_db = SQLite.DataBase("tokens")
        if user_token in [token[0] for token in tokens_db.exe("SELECT token FROM tokens;")]:
            logs_db = SQLite.DataBase("logs")
            user_id = tokens_db.exe(f"SELECT id FROM tokens where token = '{user_token}'")[0]
            db = logs_db.exe(f"SELECT * FROM logs WHERE id = {user_id[0]};")
            tokens_db.close()
            logs_db.close()
            return dumps({"id": user_id[0],
                          "logs": [{"time": data[1], "light": True if data[2] == 1 else False, "id": data[3]} for data
                                   in db],
                          "statusCode": 200})
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}

    def post(self):
        user_token = request.headers.get('Authorization')
        tokens_db = SQLite.DataBase("tokens")
        if user_token in [token[0] for token in tokens_db.exe("SELECT token FROM tokens;")]:
            logs_db = SQLite.DataBase("logs")
            params = reqparse.RequestParser()
            params.add_argument("light")
            user_id = tokens_db.exe(f"SELECT id FROM tokens where token = '{user_token}'")[0][0]
            light = 1 if params.parse_args()["light"] is True else 0
            count = 1
            try:
                count = logs_db.exe("SELECT breach from logs ORDER BY breach DESC LIMIT 1")[0][0] + 1
            except IndexError:
                count = 1
            logs_db.post_log("INSERT INTO logs VALUES (?, ?, ?, ?)", (user_id, str(utils.date()), light, count))
            db = logs_db.exe(f"SELECT * FROM logs WHERE id = {user_id} AND breach = {count};")
            tokens_db.close()
            logs_db.close()
            return dumps({"id": user_id,
                          "logs": [{"time": data[1], "light": True if data[2] == 1 else False, "id": data[3]} for data
                                   in db],
                          "statusCode": 200})
        return {"error": "Unauthorized, authentication error!", "statusCode": 401}


api.add_resource(Logs, "/logs/")

if __name__ == "__main__":
    app.run(debug=True)
