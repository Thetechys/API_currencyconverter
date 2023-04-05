from argparse import ArgumentParser

json_data = {'success': True, 'query': {'from': 'SGD', 'to': 'MYR', 'amount': 100}, 'info': {'timestamp': 1680708003, 'rate': 3.318753}, 'date': '2023-04-05', 'result': 331.8753}

compre_json_data = [(key,val) for key,val in json_data.items()]

print(json_data)
print(compre_json_data)

outcome = json_data['result']
as_of_date = json_data['date']

print(outcome)
print(as_of_date)





if __name__ == "__main__":


    parser = ArgumentParser(description='cvtf: from this currency , to: to this currency')
    parser.add_argument('-c','--cvtf',type=str)
    parser.add_argument('-t','--to',type=str)
    parser.add_argument('-a','--amount',type=int)
    args = parser.parse_args()


    def xecurrency(cvtf, to, amount):

        if cvtf == 'SGD':

            if to == 'MYR':

                if amount == 100:

                    return f"exchange rate is $100 to {outcome} as of {as_of_date}"
                


    print(xecurrency(args.cvtf,args.to,args.amount))
