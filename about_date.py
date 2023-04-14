from datetime import date
from datetime import datetime


tday = date.today()

formatted_tday = tday.strftime("%m/%d")

print(f"today's date in YYYY-MM-DD format: {formatted_tday}")

try_date = '2023-03-25'


date_list = ['2023-03-25', '2023-03-26', '2023-03-27', '2023-03-28', '2023-03-29', '2023-03-30', '2023-03-31', '2023-04-01', '2023-04-02']

p_date_list = [datetime.strptime(d,"%Y-%m-%d") for d in date_list]

f_date = [d.strftime("%m/%d") for d in p_date_list]

print(f_date)