from mySE import error
from json import loads
from requests import post

# General data:
local_url, server_secret, mail = "http://127.0.0.1:5000/", "mySecureServerPassword", "mail@mail.mail"
fetch = None

# Example user data:
username, email, password = "MyUserName", "my@personal.mail", "mySecurePassword"

try:
    fetch = post(local_url + "user/add/", data={"username": username, "email": email, "password": password, "serverSecret": server_secret})
    if fetch.status_code == 401 or loads(fetch.text)["statusCode"] == 401:
        raise error.UnauthorizedError("Oh, an invalid username, email or password got given.")
    print(f"Created a account:\n\tUsername: {username}\n\tEmail: {email}\n\tPassword: {password}")
except error.UnauthorizedError:
    print("Existing account found.\nLogging in...")
    
try:
    fetch = post(local_url + "user/", data={"email": email, "password": password})
    if fetch.status_code == 401 or loads(fetch.text)["statusCode"] == 401:
        raise error.UnauthorizedError("Oh, Invalid password got given.")
    print(f"Logged in on an account with the username: '{loads(fetch.text)['user_name']}'")
except error.UnauthorizedError as e:
    print(e)
