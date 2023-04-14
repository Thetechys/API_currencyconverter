import requests
from datetime import date
#from argparse import ArgumentParser

apiheader = {'apikey':'bG2L7chuotIKj5efvfpr1d50z2z8e7mY'}
to = 'MYR'
cvtfrom = 'SGD'
amount = 100


# response = requests.get(
#     f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={cvtfrom}&amount={amount}", headers=apiheader
#     )


# resobj = response.json()

# payload = {}

# countries = requests.get(
#     f"https://api.apilayer.com/exchangerates_data/symbols", headers=apiheader,data=payload
#     )


#rescount = countries.json()

enddate = "2023-04-02"
startdate = "2023-03-25"
symbols = "MYR"
base = "SGD"

# start_date = startdate.strptime("%Y-%m-%d")
# end_date = enddate.strptime("%Y-%m-%d")

history = requests.get(f"https://api.apilayer.com/exchangerates_data/timeseries?\
                       start_date={startdate}&end_date={enddate}&base={'SGD'}&symbols={'MYR'}"
                            ,headers=apiheader, stream=True)


historyobj = history.content.decode()

iterobj = history.iter_content(chunk_size=1024)

# for i in iterobj:

#     iterdecode = i.decode()
#     print(iterdecode)

print(historyobj)


historydata_holder = {
  "success": "true",
  "timeseries": "true",
  "start_date": "2023-03-25",
  "end_date": "2023-04-02",
  "base": "SGD",
  "rates": {
    "2023-03-25": {
      "MYR": 3.322099
    },
    "2023-03-26": {
      "MYR": 3.324066
    },
    "2023-03-27": {
      "MYR": 3.321922
    },
    "2023-03-28": {
      "MYR": 3.32073
    },
    "2023-03-29": {
      "MYR": 3.324784
    },
    "2023-03-30": {
      "MYR": 3.33032
    },
    "2023-03-31": {
      "MYR": 3.315668
    },
    "2023-04-01": {
      "MYR": 3.315668
    },
    "2023-04-02": {
      "MYR": 3.308878
    }
  }
}