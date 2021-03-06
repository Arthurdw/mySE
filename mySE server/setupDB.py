# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# API created for mySE by Arthurdw                        #
# mySE stands for My Secure Environment!                  #
# mySE was created for GO-Atheneum Oudenaarde             #
# This project and all it files are under a MIT licence.  #
# Project (mySE) started on 09/01/2020!                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file will do the basic DB setup for first usage.   #
# If this file hasn't been run yet and you start the -    #
# - server errors will occur!                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from os import system
from util.utils import date
from util.SQLite import DataBase
from json import dumps

# DB formats:
#   Tokens DB:
#       id int, token string, mail string
#   Logs DB:
#       id int, time blob, light int, breach int
#   Users DB:
#       user_name text, mail text, password text

# Create DB object and DB:
print("\r", "Creating DB...", end=' ')
tokens = DataBase("tokens")
logs = DataBase("logs")
users = DataBase("users")
print("\b\b\b\b: Done")

# Add the db parameters:
print("\r", "Setting up DB", end=' ')
tokens.setup("tokens", "(id int, token string, mail string)")
logs.setup("logs", "(id int, time blob, light int, breach int)")
users.setup("users", "(user_name text, mail text, password text)")
print("\b\b\b\b: Done")

# Create example token:
print("\r", "Creating first token...", end=' ')
token = tokens.add_token("email@mail.mail")
print("\b\b\b\b: " + str(token))

# Create example log:
print("\r", "Creating first log...", end=' ')
date = date()
logs.post_log("INSERT INTO logs VALUES (?, ?, ?, ?)", (1, str(date), 0, 1))
# Hard coded example:
print("\b\b\b\b: " + dumps({"time": date, "light": False, "id": 1}))

# Install dependecies.
print("Installing depencencies.")
system("python -m pip install -r requirements.txt")
print("Succesfully installed the server dependencies.")
