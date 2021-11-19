from datetime import datetime, timezone
import pandas
import os

path = r'.'

name = os.listdir(path)
location = path

size = os.stat(path).st_size
last_mod = os.stat(path).st_mtime

year = datetime.fromtimestamp(os.stat(path).st_mtime, tz=timezone.utc).year
month = datetime.fromtimestamp(os.stat(path).st_mtime, tz=timezone.utc).month
day = datetime.fromtimestamp(os.stat(path).st_mtime, tz=timezone.utc).day

date = year, month, day

pandas.DataFrame(data=[name])

print(name, location, size, date)
