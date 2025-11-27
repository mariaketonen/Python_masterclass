import datetime as dt
from datetime import datetime

#today = dt.datetime.today() # module and class have the same name
now = datetime.now() # use this to get current date and time
utc_now = datetime.utcnow()

#print(today)
print(now)
print(utc_now)