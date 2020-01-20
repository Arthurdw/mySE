# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# API wrapper created for mySE by Arthurdw                #
# mySE stands for My Secure Environment!                  #
# mySE was created for GO-Atheneum Oudenaarde             #
# This project and all it files are under a MIT licence.  #
# Project (mySE) started on 09/01/2020!                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Main API wrapper file                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from requests import get, post
from json import loads
import error, logs


def get_token(url: str, email: str):
    """Forgot your token?
    Fetch it using this function."""
    fetch = get(url + 'token/', data={'email': email})
    if fetch.status_code == 401 or loads(fetch.text)["statusCode"] == 401:
        raise error.UnauthorizedError("An invalid mail was given on `get_token`!")
    else:
        return loads(fetch.text)["token"]


def gen_token(url: str, email: str):
    """Generate your unique auth token!"""
    fetch = post(url + 'token/', data={'email': email})
    if fetch.status_code == 401 or loads(fetch.text)["statusCode"] == 401:
        raise error.UnauthorizedError("An invalid or used mail was given on `gen_token`!")
    else:
        return loads(fetch.text)["token"]


class Client:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.selected = get(url + "logs/", headers={'Authorization': token})
        if self.selected.status_code == 401 or loads(self.selected.text)["statusCode"] == 401:
            raise error.UnauthorizedError("An invalid token was given on setup!")

    @property
    def id(self):
        """Returns the auth token its linked client id."""
        return loads(self.selected.text)["id"]

    @property
    def logs(self):
        """Fetches all linked log objects."""
        selected = get(self.url + "logs/", headers={'Authorization': self.token})
        return [logs.Log(log) for log in loads(selected.text)["logs"]]

    def add_log(self, light: bool):
        """Add a log to the db."""
        selected = post(self.url + "logs/", data={'light': light}, headers={'Authorization': self.token})
        return [logs.Log(log) for log in loads(selected.text)["logs"]]
