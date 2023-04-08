import json
import csv
import datetime
import re
from modles import Transaction , Statement , statemen_from_json, transaction_from_json,transaction_amount,ending_balance
data = {}
transactions = []
Statements = []

try:
    with open('transactions.json') as json_file:
        data =  json.load(json_file)
        for info in data["Transaction"]:
            transactions.append(transaction_from_json(info))

except:
    print("Exception")
def getFloat(amount_str):
    amount_str = amount_str.split(".")
    amount = ""
    for num in amount_str:
        amount = amount + num
    amount = amount.split(",")
    amount = float(amount[0] + "." + amount[1])
    return amount
with open("export.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("skipped")
        else:
            line_count = line_count + 1
            if len(row) > 0:
                date = datetime.datetime.strptime(row[0],"%Y-%M-%d").date()
                account_num = row[1].split(" ")
                account_num = account_num[len(account_num)-1]
                name = row[1].replace(account_num, "")
                transaction = Transaction(
                    name,
                    transaction_amount,
                    date,
                    account_num,
                    ending_balance

                )
                exists = False
                for transfer in transactions:
                    if transfer.date == transaction.date:
                         if transfer.name == transaction.name:
                              if transfer.amount == transaction.amount:
                                   exists = True
                if exists != True:
                    transactions.append(transaction)


        
with open('transactions.json', 'w') as json_file:
     data = {}
     data ["Transactions"] = []
     for transfer in transactions:
          data ["Transactions"] .append(transfer.serialize())
     json.dump(data, json_file, sort_keys=True, indent=4)
