import tkinter as tk
from tkinter import messagebox
import requests
import re




apiheader = {'apikey':'bG2L7chuotIKj5efvfpr1d50z2z8e7mY'}

cc = {
    "success": "true",
    "symbols": {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "AMD": "Armenian Dram",
        "ANG": "Netherlands Antillean Guilder",
        "AOA": "Angolan Kwanza",
        "ARS": "Argentine Peso",
        "AUD": "Australian Dollar",
        "AWG": "Aruban Florin",
        "AZN": "Azerbaijani Manat",
        "BAM": "Bosnia-Herzegovina Convertible Mark",
        "BBD": "Barbadian Dollar",
        "BDT": "Bangladeshi Taka",
        "BGN": "Bulgarian Lev",
        "BHD": "Bahraini Dinar",
        "BIF": "Burundian Franc",
        "BMD": "Bermudan Dollar",
        "BND": "Brunei Dollar",
        "BOB": "Bolivian Boliviano",
        "BRL": "Brazilian Real",
        "BSD": "Bahamian Dollar",
        "BTC": "Bitcoin",
        "BTN": "Bhutanese Ngultrum",
        "BWP": "Botswanan Pula",
        "BYN": "New Belarusian Ruble",
        "BYR": "Belarusian Ruble",
        "BZD": "Belize Dollar",
        "CAD": "Canadian Dollar",
        "CDF": "Congolese Franc",
        "CHF": "Swiss Franc",
        "CLF": "Chilean Unit of Account (UF)",
        "CLP": "Chilean Peso",
        "CNY": "Chinese Yuan",
        "COP": "Colombian Peso",
        "CRC": "Costa Rican Col\u00f3n",
        "CUC": "Cuban Convertible Peso",
        "CUP": "Cuban Peso",
        "CVE": "Cape Verdean Escudo",
        "CZK": "Czech Republic Koruna",
        "DJF": "Djiboutian Franc",
        "DKK": "Danish Krone",
        "DOP": "Dominican Peso",
        "DZD": "Algerian Dinar",
        "EGP": "Egyptian Pound",
        "ERN": "Eritrean Nakfa",
        "ETB": "Ethiopian Birr",
        "EUR": "Euro",
        "FJD": "Fijian Dollar",
        "FKP": "Falkland Islands Pound",
        "GBP": "British Pound Sterling",
        "GEL": "Georgian Lari",
        "GGP": "Guernsey Pound",
        "GHS": "Ghanaian Cedi",
        "GIP": "Gibraltar Pound",
        "GMD": "Gambian Dalasi",
        "GNF": "Guinean Franc",
        "GTQ": "Guatemalan Quetzal",
        "GYD": "Guyanaese Dollar",
        "HKD": "Hong Kong Dollar",
        "HNL": "Honduran Lempira",
        "HRK": "Croatian Kuna",
        "HTG": "Haitian Gourde",
        "HUF": "Hungarian Forint",
        "IDR": "Indonesian Rupiah",
        "ILS": "Israeli New Sheqel",
        "IMP": "Manx pound",
        "INR": "Indian Rupee",
        "IQD": "Iraqi Dinar",
        "IRR": "Iranian Rial",
        "ISK": "Icelandic Kr\u00f3na",
        "JEP": "Jersey Pound",
        "JMD": "Jamaican Dollar",
        "JOD": "Jordanian Dinar",
        "JPY": "Japanese Yen",
        "KES": "Kenyan Shilling",
        "KGS": "Kyrgystani Som",
        "KHR": "Cambodian Riel",
        "KMF": "Comorian Franc",
        "KPW": "North Korean Won",
        "KRW": "South Korean Won",
        "KWD": "Kuwaiti Dinar",
        "KYD": "Cayman Islands Dollar",
        "KZT": "Kazakhstani Tenge",
        "LAK": "Laotian Kip",
        "LBP": "Lebanese Pound",
        "LKR": "Sri Lankan Rupee",
        "LRD": "Liberian Dollar",
        "LSL": "Lesotho Loti",
        "LTL": "Lithuanian Litas",
        "LVL": "Latvian Lats",
        "LYD": "Libyan Dinar",
        "MAD": "Moroccan Dirham",
        "MDL": "Moldovan Leu",
        "MGA": "Malagasy Ariary",
        "MKD": "Macedonian Denar",
        "MMK": "Myanma Kyat",
        "MNT": "Mongolian Tugrik",
        "MOP": "Macanese Pataca",
        "MRO": "Mauritanian Ouguiya",
        "MUR": "Mauritian Rupee",
        "MVR": "Maldivian Rufiyaa",
        "MWK": "Malawian Kwacha",
        "MXN": "Mexican Peso",
        "MYR": "Malaysian Ringgit",
        "MZN": "Mozambican Metical",
        "NAD": "Namibian Dollar",
        "NGN": "Nigerian Naira",
        "NIO": "Nicaraguan C\u00f3rdoba",
        "NOK": "Norwegian Krone",
        "NPR": "Nepalese Rupee",
        "NZD": "New Zealand Dollar",
        "OMR": "Omani Rial",
        "PAB": "Panamanian Balboa",
        "PEN": "Peruvian Nuevo Sol",
        "PGK": "Papua New Guinean Kina",
        "PHP": "Philippine Peso",
        "PKR": "Pakistani Rupee",
        "PLN": "Polish Zloty",
        "PYG": "Paraguayan Guarani",
        "QAR": "Qatari Rial",
        "RON": "Romanian Leu",
        "RSD": "Serbian Dinar",
        "RUB": "Russian Ruble",
        "RWF": "Rwandan Franc",
        "SAR": "Saudi Riyal",
        "SBD": "Solomon Islands Dollar",
        "SCR": "Seychellois Rupee",
        "SDG": "Sudanese Pound",
        "SEK": "Swedish Krona",
        "SGD": "Singapore Dollar",
        "SHP": "Saint Helena Pound",
        "SLE": "Sierra Leonean Leone",
        "SLL": "Sierra Leonean Leone",
        "SOS": "Somali Shilling",
        "SRD": "Surinamese Dollar",
        "STD": "S\u00e3o Tom\u00e9 and Pr\u00edncipe Dobra",
        "SVC": "Salvadoran Col\u00f3n",
        "SYP": "Syrian Pound",
        "SZL": "Swazi Lilangeni",
        "THB": "Thai Baht",
        "TJS": "Tajikistani Somoni",
        "TMT": "Turkmenistani Manat",
        "TND": "Tunisian Dinar",
        "TOP": "Tongan Pa\u02bbanga",
        "TRY": "Turkish Lira",
        "TTD": "Trinidad and Tobago Dollar",
        "TWD": "New Taiwan Dollar",
        "TZS": "Tanzanian Shilling",
        "UAH": "Ukrainian Hryvnia",
        "UGX": "Ugandan Shilling",
        "USD": "United States Dollar",
        "UYU": "Uruguayan Peso",
        "UZS": "Uzbekistan Som",
        "VEF": "Venezuelan Bol\u00edvar Fuerte",
        "VES": "Sovereign Bolivar",
        "VND": "Vietnamese Dong",
        "VUV": "Vanuatu Vatu",
        "WST": "Samoan Tala",
        "XAF": "CFA Franc BEAC",
        "XAG": "Silver (troy ounce)",
        "XAU": "Gold (troy ounce)",
        "XCD": "East Caribbean Dollar",
        "XDR": "Special Drawing Rights",
        "XOF": "CFA Franc BCEAO",
        "XPF": "CFP Franc",
        "YER": "Yemeni Rial",
        "ZAR": "South African Rand",
        "ZMK": "Zambian Kwacha (pre-2013)",
        "ZMW": "Zambian Kwacha",
        "ZWL": "Zimbabwean Dollar"
    }
}

ccsymbols = cc["symbols"]









dimension = xwidth, yheight = 800,400
root = tk.Tk()
root.geometry(f"{int(xwidth)}x{int(yheight)}")


var = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()
var7 = tk.StringVar()
var8 = tk.StringVar()


def check_num(num):

    message = 'Please enter proper INTEGER or FLOAT value'

    if num.get().isdigit() and num.get() != '':
        return True
    
    else:
        messagebox.showinfo("Prompt",message)
        return False


def check_txt(txt):

    message = 'Please enter proper TEXT value'

    if txt.get().isalpha() and txt.get() != '':
        return True

    else:
        messagebox.showinfo("Prompt",message)
        return False

def reset():
    var.set('')     ##FROM entry box
    var2.set('')    ##TO entry box    
    var3.set('')    ##EXHANGE AMOUNT entry box
    var4.set('')    ##exchange RATE label
    var5.set('')    ##exchanged AMOUNT label

def reset_code():
    var6.set('')    ##GUIDE entry box
    var7.set('')    ##guide OUTPUT label


def query_exc_rate(*args):

    if check_txt(var) and check_txt(var2) and check_num(var3):

        exfrom = var.get().upper()
        exto = var2.get().upper()
        amount = text_entry.get()

        response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to={exto}&from={exfrom}&amount={amount}", headers=apiheader
        )

        resobj = response.json()
        var4.set(resobj['info']['rate'])
        var5.set(resobj['result'])
        var8.set(f"Exchange rate as of {resobj['date']}")

def search_code():
    
    if check_txt(var6):

        try:
            codesearch = var6.get().title()
            x = [key for key,val in ccsymbols.items() if re.search(codesearch,val)][0]
            var7.set(x)

        except IndexError:
            return 'Currency / Country not found'



''' this function defined just in case any changes on country code '''
def f5_country():
    payload = {}
    countries = requests.get(
        f"https://api.apilayer.com/exchangerates_data/symbols", headers=apiheader,data=payload
        )
    
    cc = payload['symbols']    


'''----------------1ST ROW----------------'''
exc_label = tk.Label(root,text='From')
exc_label.grid(row=1,column=1)
exc_label = tk.Label(root,text='To')
exc_label.grid(row=1,column=2)
exc_label = tk.Label(root,text='Exchange amount')
exc_label.grid(row=1,column=3)
rate_label = tk.Label(root,text='Exchange rate: ')
rate_label.grid(row=1,column=4)
out_label = tk.Label(root,text='Total value')
out_label.grid(row=1,column=5)
out_label = tk.Label(root,text='Currency code guide')
out_label.grid(row=1,column=6)
out_label = tk.Label(root,text='Currency code')
out_label.grid(row=1,column=7)





'''----------------2ND ROW----------------'''
from_entry = tk.Entry(root,width=7,textvariable=var)
from_entry.grid(row=2,column=1)

to_entry = tk.Entry(root,width=7,textvariable=var2)
to_entry.grid(row=2,column=2)

'''entry box to input amount to exchange'''
text_entry = tk.Entry(root,width=15,textvariable=var3)
text_entry.grid(row=2,column=3)
'''label for EXCHANGE RATE output'''
exrate_label = tk.Label(root,width=15,textvariable=var4)
exrate_label.grid(row=2,column=4)
'''label for EXCHANGED AMOUNT output'''
examt_label = tk.Label(root,width=15,textvariable=var5)
examt_label.grid(row=2,column=5)

'''CURRENCY CODE GUIDE - entry box for country search'''
guide_entry = tk.Entry(root,width=15,textvariable=var6)
guide_entry.grid(row=2,column=6)
out_label = tk.Label(root,textvariable=var7)
out_label.grid(row=2,column=7)


'''----------------3RD ROW----------------'''
submit_button = tk.Button(root, text='Submit',command=query_exc_rate)
submit_button.grid(row=3,column=2)

reset_button = tk.Button(root, text='Reset',command=reset)
reset_button.grid(row=3,column=3)

''' this button is available ONLY when there are changes in country codes'''
''' at that time - uncomment refresh_button.grid below '''
refresh_button = tk.Button(root, text='Refresh country',command=f5_country)
#refresh_button.grid(row=3,column=4)

search_button = tk.Button(root, text='Search',command=search_code)
search_button.grid(row=3,column=6)

reset_button2 = tk.Button(root, text='Reset',command=reset_code)
reset_button2.grid(row=3,column=7)


'''----------------4TH ROW----------------'''
stat_label = tk.Label(root,textvariable=var8)
stat_label.grid(row=4,column=1)




#def a function to get lastest country code list but hide this function
# f5country_button = tk.Button(root, text='Refresh country',command=)
# f5country_button.grid(row=3,column=4)


root.mainloop()