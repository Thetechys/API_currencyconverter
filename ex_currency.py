import requests
#from argparse import ArgumentParser

apiheader = {'apikey':'bG2L7chuotIKj5efvfpr1d50z2z8e7mY'}
to = 'MYR'
cvtfrom = 'SGD'
amount = 100


# response = requests.get(
#     f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={cvtfrom}&amount={amount}", headers=apiheader
#     )


# resobj = response.json()

payload = {}

countries = requests.get(
    f"https://api.apilayer.com/exchangerates_data/symbols", headers=apiheader,data=payload
    )


#rescount = countries.json()

print(countries.text)
