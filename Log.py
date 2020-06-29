
import datetime


class footballDBLog():
    def __init__(self):
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()

    def getLog(self, proxyOBJ):
        filename = open("footballAPI.log", "a")
        filename.write("FootballDatabase.py executed\n")
        filename.write("Date:{}/\n".format(self.time))
        filename.write("STATUS:{}\n".format(proxyOBJ.statusCode))
        filename.write("Selected Team:{}\n".format(proxyOBJ.userTeam))
        filename.write("Returned stadium location:{}\n".format(proxyOBJ.userTeamLocation))
        filename.write("-------------------------------------------\n")
        


class weatherDBLog():
    def __init__(self):
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()

    def getLog(self, proxyOBJ):
        filename = open("weatherAPI.log", "a")
        filename.write("weatherAPI.py executed\n")
        filename.write("Date:{}/\n".format(self.time))
        filename.write("STATUS:{}\n".format(proxyOBJ.statusCode))
        filename.write("Location to show weather :{}\n".format(proxyOBJ.city_name))
        filename.write("Returned country code :{}\n".format(proxyOBJ.country_code))
        filename.write("-------------------------------------------\n")
        

class countryDBLog():
    def __init__(self):
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()


    def getLog(self, proxyOBJ):
        filename = open("countryAPI.log", "a")
        filename.write("countryAPI.py executed\n")
        filename.write("Date:{}/\n".format(self.time))
        filename.write("STATUS:{}\n".format(proxyOBJ.statusCode))
        filename.write("Country code :{}\n".format(proxyOBJ.country_code))
        filename.write("Returned country capital :{}\n".format(proxyOBJ.capital))
        filename.write("Returned country currency :{}\n".format(proxyOBJ.currency))
        filename.write("-------------------------------------------\n")


class Log:
    def __init__(self, proxyOBJ):
        self.flog = footballDBLog()
        self.wlog = weatherDBLog()
        self.clog = countryDBLog()
    
        if proxyOBJ.proxy_id == 1:
            self.flog.getLog(proxyOBJ)
        elif proxyOBJ.proxy_id == 2:
            self.wlog.getLog(proxyOBJ)
        elif proxyOBJ.proxy_id == 3:
            self.clog.getLog(proxyOBJ)

        
        
        


