# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# API wrapper created for mySE by Arthurdw                #
# mySE stands for My Secure Environment!                  #
# mySE was created for GO-Atheneum Oudenaarde             #
# This project and all it files are under a MIT licence.  #
# Project (mySE) started on 09/01/2020!                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Error file for API wrapper                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class MySE(Exception):
    """Base exception catcher."""
    pass


class UnauthorizedError(MySE):
    """Exception that occurs when an invalid token/email has been given."""
    pass
