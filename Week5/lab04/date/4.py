from datetime import datetime, timedelta

d = int(input())
date_1 = datetime.today().replace(microsecond=0)
date_2 = date_1 - timedelta(d)
delta = date_1 - date_2
x = delta.total_seconds() #outputs seconds in floats
print(x)