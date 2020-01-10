# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# API created for mySE by Arthurdw                        #
# mySE stands for My Secure Environment!                  #
# mySE was created for GO-Atheneum Oudenaarde             #
# This project and all it files are under a MIT licence.  #
# Project (mySE) started on 09/01/2020!                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file just simply creates a date object.            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from datetime import datetime


def date():
    return {"microsecond": datetime.now().microsecond, "second": datetime.now().second,
            "minute": datetime.now().minute, "hour": datetime.now().hour, "day": datetime.now().day,
            "month": datetime.now().month, "year": datetime.now().year}
