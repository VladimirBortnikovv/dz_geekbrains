#задание 2
import requests

def currency_rates(valut):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    valutes = response.json()['Valute']
    valutes_enter = valutes[valut]
    course = valutes_enter ['Value']
    return (course)

print(currency_rates('USD'))

#задание 4

import utils

utils.currency_rates('USD')
