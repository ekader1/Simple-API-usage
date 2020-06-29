# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
from APIProxy import *
from Log import Log

class weatherAPI(APIProxy):
    def __init__(self, location):

        # TODO: replace with your own app_id and app_key
        self.url = "None"
        self.app_key = 'a136fece97fb4f64bf56b89aacb5b853'
        self.city_name = location
        self.country_code = 'none'
        self.statusCode = 'none'
        self.proxy_id = 2
        self.enter_data()
        self.logOBJ = Log(self)
        
    def enter_data(self):
        for character in self.city_name:
            if character ==',':
                new_list = self.city_name.split(", ")
                self.first = new_list[0]
                self.city_name = new_list[1]
            

        self.url = 'https://api.weatherbit.io/v2.0/forecast/daily?city=' + self.city_name + '&key=' + self.app_key
        r = requests.get(self.url, headers = {'app_key' : self.app_key})
        a = r.json()
        self.statusCode =  r.status_code
        
        for i in a['data']:
           print('Date: ' + i['datetime'] + '  ' + i['weather']['description'])
           print('Max.temp: ', i['app_max_temp'])
           print('Min.temp: ', i['app_min_temp'])
           
            
        self.country_code = (a['country_code'])

    def fallback(self):
        pass





        

