#* Code for Live cricket score Notification * ( Using plyer )

import sports
i=sports.get_match("Cricket","Team1","Team2")
import time
from plyer import notification
notification.notify(
     title="IPL Scores Updates",
     message=str(i),
     app_icon="Path of Image",
     timeout=10,
)
time.sleep(10)

#*Code for Live cricket score Notification * ( Using pynotifier )

import sports
Matchinfo=sports.get_sport("CRICKET")
from pynotifier import Notification

Notification(
     title="IPL Live score Updates",
     description=str(Matchinfo),
     duration=60,
     ).send()
