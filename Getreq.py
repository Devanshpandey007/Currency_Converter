import requests
import os
class ExchangeCurrency:
    def __init__(self,fromCurrency,toCurrency):
        self.fromCurrency = fromCurrency
        self.toCurrency = toCurrency
        self.URL = f"https://v6.exchangerate-api.com/v6/5b898aa30a91a2b720f5af6f/latest/{self.fromCurrency}"
        self.news_API = os.getenv("API_KEY")
        self.currency= self.fromCurrency
        self.parameter = {
            "apikey": self.news_API,
            "Latest": "latest",
        }
        response = requests.get(self.URL,params=self.parameter)
        readable_format = response.json()
        self.converted_val = readable_format["conversion_rates"][self.toCurrency]

    def give_value(self,amnt):
        money = float(self.converted_val)* amnt
        return money
# obj1 = ExchangeCurrency("USD","INR")
# print(obj1.give_value(15))


