import urllib.request
import datetime

# Variables

URL = 'http://www.nbrb.by/API/RefinancingRate?onDate='
data = datetime.date.today()


def __api_call(URL, data):

    response = urllib.request.urlopen(str(URL)+str(data))

    return str(response.read().decode('utf-8')).split(",")

def define(URL, data):
    tmp_list = []

    tmp_list.extend(__api_call(URL, data))
    a = str(tmp_list.pop(1)).split(":")
    b = str(a.pop(1)).replace("}]", "")
    if b.isdigit() < 20:
        print(b + ' Loshara')
    else:
        print("zvoni v bank")


define(URL, data)