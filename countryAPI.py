import requests
import json
from APIProxy import *
from Log import Log

class countryAPI(APIProxy):
    def __init__(self, country_code):

        # TODO: replace with your own app_id and app_key
        self.url = "None"
        self.country_code = country_code
        self.r = None
        self.statusCode = 'none'
        self.capital = 'none'
        self.currency = 'none'
        self.proxy_id = 3
        self.enter_data()
        self.logOBJ = Log(self)

    def enter_data(self):   
        self.url = 'http://country.io/capital.json'
        self.r = requests.get(self.url)
        self.statusCode = self.r.status_code
        capital_city_DB = self.r.json()
        print('Capital city: ' + capital_city_DB[self.country_code])
        self.capital = capital_city_DB[self.country_code] 
        self.url = 'http://country.io/currency.json'
        self.r = requests.get(self.url)
        currency_DB = self.r.json()
        print('Currency they use: ' + currency_DB[self.country_code])
        self.currency = currency_DB[self.country_code]

    def fallback(self):
        pass
        
        
        

        

