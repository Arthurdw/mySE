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

from util.SQLite import DataBase

# DB formats:
#   Tokens DB:
#       id int, token string
#   Logs DB:
#       id int, time blob, light int, breach int

# Create DB object and DB:
print("\r", "Creating DB...", end=' ')
tokens = DataBase("tokens")
logs = DataBase("logs")
print("\b\b\b\b: Done")

# Add the db parameters:
print("\r", "Setting up DB", end=' ')
tokens.setup("tokens", "(id int, token string)")
logs.setup("logs", "(id int, time blob, light int, breach int)")
print("\b\b\b\b: Done")

# Create example token:
print("\r", "Creating first token...", end=' ')
# TODO:
#  Create token here
token = None
print("\b\b\b\b: " + str(token))

# Create example log:
print("\r", "Creating first log...", end=' ')
# TODO:
#  Create a log here
print("\b\b\b\b: " + "LOG INFO")
