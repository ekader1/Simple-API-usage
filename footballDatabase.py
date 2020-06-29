from Log import Log
import requests
import json
from APIProxy import *
##select a team - see players - get player information - pick player - see team schedule
#search by team
#url = 'https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=arsenal'
#search for all players in team
##url = https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Arsenal
#search by player name
#url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p=Danny%20Welbeck'
#search by event name
##https://www.thesportsdb.com/api/v1/json/1/searchevents.php?e=Arsenal_vs_Chelsea
#player details by ID
#Schedules Next 5 Events by team ID
##url = 'https://www.thesportsdb.com/api/v1/json/1/eventsnext.php?id=133602'
#url = 'https://www.thesportsdb.com/api/v1/json/1/lookupplayer.php?id=34145395'

class footballDatabase(APIProxy):
    def __init__(self):
        self.url = 'None'
        self.app_key = '4013004'
        self.userTeam = "none"
        self.userTeamID ='None'
        self.userTeamLocation ='None'
        self.statusCode = 'None'
        self.proxy_id = 1
        self.enter_data()
        self.showTeamInfo()
        self.showTeamSquad()
        ##self.next5Games()
        ##self.lookupPlayer()
        self.logOBJ = Log(self)

        

    def enter_data(self):
        userTeam = input("Select a team to get information about: ")
        self.userTeam = userTeam
    
    def showTeamInfo(self):
        self.url = 'https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=' + self.userTeam
        r = requests.get(self.url, headers = {'app_key' : self.app_key})
        a = r.json()
        self.statusCode = r.status_code
        self.userTeamID =(a['teams'][0]['idTeam'])
        self.userTeamLocation = (a['teams'][0]['strStadiumLocation'])
        print(a['teams'][0]['strTeam'])
        print('Year formed: ' + a['teams'][0]['intFormedYear'])
        print('Registered League: ' + a['teams'][0]['strLeague'])
        print('Manager: ' + a['teams'][0]['strManager'])
        print('Stadium: ' + a['teams'][0]['strStadium'])
        print('Team Description: ' + a['teams'][0]['strDescriptionEN'])
        print('Stadium Location: ' + self.userTeamLocation)

    def showTeamSquad(self):
        self.url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=' + self.userTeam
        r = requests.get(self.url, headers = {'app_key' : self.app_key})
        a = r.json()
        
        for i in a['player']:

            print('#######')
            print(i['strPlayer'])
            print('Date of Born: ' + i['dateBorn'])
            print('Nationality: ' + i['strNationality'])
            print('Height: ' + i['strHeight'])
            print('Signing Fee: ' + i['strSigning'])
    
    def next5Games(self):
       self.url = 'https://www.thesportsdb.com/api/v1/json/1/eventsnext.php?id=' + self.userTeamID
       r = requests.get(self.url, headers = {'app_key' : self.app_key})
       a = r.json()
       ##print(a['events'])
       for i in a['events']:
           print(i['strEvent'] + ' ' + i['strDate'])


    def lookupPlayer(self):
        firstName = input("First name: ")
        lastName = input("Last Name: ")
        self.url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p=' + firstName + '%20' + lastName
        r = requests.get(self.url, headers = {'app_key' : self.app_key})
        a = r.json()
        print(a['player'][0]['strPlayer'])
        print('Nationality: ' + a['player'][0]['strNationality'])
        print('Date of born: ' + a['player'][0]['dateBorn'])
        print('Wage: ' + a['player'][0]['strWage'])
        print('Description:')
        print(a['player'][0]['strDescriptionEN'])
        
    def fallback(self):
        pass
            


 




