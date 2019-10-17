from datetime import datetime as dt
print(dt.now())
import pytz
tz = pytz.timezone("Asia/Kolkata")
print(dt.now(tz))
