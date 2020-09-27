import os
import datetime
now = datetime.datetime.now()
now = str(now).replace(" ","_")
os.system(f"import -window root Pictures/{now}.png")
os.system("notify-send 'Screenshot Saved' -t 100")