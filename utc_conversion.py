from datetime import datetime

ts = int("1617145607")

# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.utcfromtimestamp(ts).strftime('%H:%M:%S'))

