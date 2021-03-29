from datetime import datetime

ts = int("1617059142")
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
