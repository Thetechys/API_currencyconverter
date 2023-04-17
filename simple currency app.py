import tkinter as tk
from tkinter import messagebox
import requests
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from math import floor
import numpy as np



''' regarding api key, go to README '''
apiheader = {'apikey':'/replace your own API key here'}

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




class fxtkwindow():


    
    def __init__(self):

        self.dimension = xwidth, yheight = 800,650
        self.root = tk.Tk()
        self.root.geometry(f"{int(xwidth)}x{int(yheight)}")

        self.var = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()
        self.var5 = tk.StringVar()
        self.var6 = tk.StringVar()
        self.var7 = tk.StringVar()
        self.var8 = tk.StringVar()


        '''----------------1ST ROW----------------'''
        self.exc_label = tk.Label(self.root,text='From')
        self.exc_label.grid(row=1,column=1)
        self.exc_label = tk.Label(self.root,text='To')
        self.exc_label.grid(row=1,column=2)
        self.exc_label = tk.Label(self.root,text='Exchange amount')
        self.exc_label.grid(row=1,column=3)
        self.rate_label = tk.Label(self.root,text='Exchange rate: ')
        self.rate_label.grid(row=1,column=4)
        self.out_label = tk.Label(self.root,text='Total value')
        self.out_label.grid(row=1,column=5)
        self.out_label = tk.Label(self.root,text='Currency code guide')
        self.out_label.grid(row=1,column=6)
        self.out_label = tk.Label(self.root,text='Currency code')
        self.out_label.grid(row=1,column=7)


        '''----------------2ND ROW----------------'''
        self.from_entry = tk.Entry(self.root,width=7,textvariable=self.var)
        self.from_entry.grid(row=2,column=1)

        self.to_entry = tk.Entry(self.root,width=7,textvariable=self.var2)
        self.to_entry.grid(row=2,column=2)

        '''entry box to input amount to exchange'''
        self.text_entry = tk.Entry(self.root,width=15,textvariable=self.var3)
        self.text_entry.grid(row=2,column=3)
        '''label for EXCHANGE RATE output'''
        self.rate_label = tk.Label(self.root,width=15,textvariable=self.var4)
        self.rate_label.grid(row=2,column=4)
        '''label for EXCHANGED AMOUNT output'''
        self.examt_label = tk.Label(self.root,width=15,textvariable=self.var5)
        self.examt_label.grid(row=2,column=5)

        '''CURRENCY CODE GUIDE - entry box for country search'''
        self.guide_entry = tk.Entry(self.root,width=15,textvariable=self.var6)
        self.guide_entry.grid(row=2,column=6)
        self.out_label = tk.Label(self.root,textvariable=self.var7)
        self.out_label.grid(row=2,column=7)


        '''----------------3RD ROW----------------'''
        self.submit_button = tk.Button(self.root, text='Submit',command=self.query_exc_rate)
        self.submit_button.grid(row=3,column=2)

        self.reset_button = tk.Button(self.root, text='Reset',command=self.reset)
        self.reset_button.grid(row=3,column=3)

        ''' this button is available ONLY when there are changes in country codes'''
        ''' at that time - uncomment refresh_button.grid below '''
        refresh_button = tk.Button(self.root, text='Refresh country',command=self.f5_country)

        self.search_button = tk.Button(self.root, text='Search',command=self.search_code)
        self.search_button.grid(row=3,column=6)

        self.reset_button2 = tk.Button(self.root, text='Reset',command=self.reset_code)
        self.reset_button2.grid(row=3,column=7)


        '''----------------4TH ROW----------------'''
        self.stat_label = tk.Label(self.root,textvariable=self.var8)
        self.stat_label.grid(row=4,column=1, columnspan=7)


        '''----------------5TH ROW----------------'''
        '''5TH ROW RESERVED FOR SHOW TREND'''

        self.root.mainloop()

        




    def check_num(self, num):

        message = 'Please enter proper INTEGER or FLOAT value'

        if num.get().isdigit() and num.get() != '':
            return True
        else:
            messagebox.showinfo("Prompt",message)
            return False

    def check_txt(self, txt):

        message = 'Please enter proper TEXT value'

        if txt.get().isalpha() and txt.get() != '':
            return True

        else:
            messagebox.showinfo("Prompt",message)
            return False

    def reset(self):
        self.var.set('')     ##FROM entry box
        self.var2.set('')    ##TO entry box    
        self.var3.set('')    ##EXHANGE AMOUNT entry box
        self.var4.set('')    ##exchange RATE label
        self.var5.set('')    ##exchanged AMOUNT label




    def reset_code(self):
        self.var6.set('')    ##GUIDE entry box
        self.var7.set('')    ##guide OUTPUT label



    def query_exc_rate(self, *args):

        if self.check_txt(self.var) and self.check_txt(self.var2) and self.check_num(self.var3):

            exfrom = self.var.get().upper()
            exto = self.var2.get().upper()
            amount = self.text_entry.get()

            response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={exto}&from={exfrom}&amount={amount}", headers=apiheader
            )

            resobj = response.json()
            self.var4.set(resobj['info']['rate'])
            self.var5.set(resobj['result'])
            self.var8.set(f"** Exchange rate as of {resobj['date']} **")

            self.show_trend()

    def show_trend(self):

        base = self.var.get()
        symbols = self.var2.get()


        tday = datetime.today()
        pastday = tday - timedelta(days=120)

        st_day = pastday.strftime("%Y-%m-%d")
        end_day = tday.strftime("%Y-%m-%d")
        


        history = requests.get(f"https://api.apilayer.com/exchangerates_data/timeseries?\
                        start_date={st_day}&end_date={end_day}&base={base}&symbols={symbols}"
                                ,headers=apiheader, stream=True)

        historyobj = history.json()

        raw_date_point = [datetime.strptime(i, "%Y-%m-%d") for i in historyobj["rates"].keys()]
        date_point = [dt.strftime("%d/%m/%y") for dt in raw_date_point]
        np_date_point = np.array(date_point)
        

        rate_point = [rt for key,val in historyobj["rates"].items() for rt in val.values()]
        np_rate_point = np.array(rate_point)


        yclimax_idx = np.argmax(np_rate_point)  ##index of the highest rate in array
        yvalley_idx = np.argmin(np_rate_point)  ##index of lowest rate in array

        yclimax_pt = np_rate_point[yclimax_idx]
        yvalley_pt = np_rate_point[yvalley_idx]
        xclimax_pt = np_date_point[-1]
        xvalley_pt = np_date_point[-1]

        date_len = len(date_point)
        mididx = floor(date_len/2)
        oneidx = floor(mididx/2)
        thirdidx = floor(((date_len-mididx) / 2) + mididx)

        xticks = [date_point[0], date_point[oneidx], date_point[mididx], date_point[thirdidx], date_point[-1]]

        fig, ax = plt.subplots()
        fig_size = fig.get_size_inches()
        font_size = min(fig_size)


        ax.plot(np_date_point, np_rate_point)

        ax.axhline(y=yvalley_pt, color='red', linestyle='--')
        ax.axhline(y=yclimax_pt, color='green', linestyle='--')
        ax.annotate(f"{yclimax_pt:.2f}",xy=(xclimax_pt, yclimax_pt),\
                        arrowprops=dict(facecolor='green', arrowstyle='<-'), xytext=(xclimax_pt,yclimax_pt+0.02))
        ax.annotate(f"{yvalley_pt:.2f}",xy=(xvalley_pt, yvalley_pt),\
                        arrowprops=dict(facecolor='red', arrowstyle='<-'), xytext=(xvalley_pt,yvalley_pt+0.01))

        ax.set_title("FX Rate Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("Rate")
        ax.set_xlim((xticks[0],xticks[-1]))
        ax.set_xticks(xticks)
        ax.tick_params(axis='both', labelsize=font_size+2)
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=5, column=1, columnspan=7)



    def search_code(self):
    
        if self.check_txt(self.var6):

            try:
                codesearch = self.var6.get().title()
                x = [key for key,val in ccsymbols.items() if re.search(codesearch,val)][0]
                self.var7.set(x)

            except IndexError:
                return 'Currency / Country not found'



    ''' this function defined just in case any changes on country code '''
    def f5_country(self):
        payload = {}
        countries = requests.get(
            f"https://api.apilayer.com/exchangerates_data/symbols", headers=apiheader,data=payload
            )
        
        cc = payload['symbols']   





if __name__ == '__main__':

    app1 = fxtkwindow()
