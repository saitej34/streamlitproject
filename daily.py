import requests
def getDetails(dat):
    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

    querystring = {"date":dat}

    headers = {
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
    'x-rapidapi-key': "721bd46ec5msh1895563b314a99cp14eeecjsn9260f8ff52a3"        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    e=(response.json())
    return e["data"]["confirmed"],e["data"]["deaths"]
    

