import requests
def getState(code):
    code=str(code)
    url = ("https://covid-india2.p.rapidapi.com/states/code/%s" %(code))

    headers = {
        'x-rapidapi-host': "covid-india2.p.rapidapi.com",
        'x-rapidapi-key': "721bd46ec5msh1895563b314a99cp14eeecjsn9260f8ff52a3"
    }

    response = requests.request("GET", url, headers=headers)

    h=(response.json())
    return h[1]['state_name'],h[1]['active_today'],h[1]['death_today'],h[1]['recovered_today'],h[1]['active_today'],h[1]['positive'],h[1]['recovered'],h[1]['death']
