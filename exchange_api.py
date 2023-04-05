import requests
import json

# making a foreign exchange application with exchange api

result = requests.get("https://api.exchangerate.host/latest")
result = json.loads(result.text)

given_money = input("Which currency do you want to give: ").upper()
taken_money = input("Which currency do you want to take: ").upper()
amount_given_money = eval(input("How much money will you exchange: "))

my_rates = 0

if given_money != "EURO" and taken_money != "EURO":
    x = result["rates"][given_money]
    y = result["rates"][taken_money]
    my_rates = (y / x)

if given_money == "EURO":
    my_rates = result["rates"][taken_money]

if taken_money == "EURO":
    my_rates = 1/result["rates"][given_money]


result = my_rates * amount_given_money
print("The",taken_money,"amount you will receive is ",round(result,3))
