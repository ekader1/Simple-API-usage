from footballDatabase import *
from weatherAPI import *
from countryAPI import *
from Log import *


def main():

        result = footballDatabase()
        result2 = weatherAPI(result.userTeamLocation)
        result3 = countryAPI(result2.country_code)


if __name__ == '__main__':
        main()
        
        