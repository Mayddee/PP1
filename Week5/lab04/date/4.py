from datetime import datetime, date

date_1 = date(2022, 5, 18)
date_2 = date(2022, 7, 12)
delta = date_2 - date_1
print(delta.total_seconds()) #outputs seconds as float