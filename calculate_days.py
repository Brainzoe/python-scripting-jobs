#! /usr/bin/python3

from datetime import datetime

# Choose your desired dates in 'YYYY-MM-DD' format
date_str1 = '2023-09-01'
date_str2 = '2023-09-15'

date_format = '%Y-%m-%d'
date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

delta = date2 - date1
print(f"Number of days between {date_str1} and {date_str2}: {delta.days} days")







