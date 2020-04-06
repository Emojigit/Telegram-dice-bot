import requests

def send(apikey,message,channel):
    url="https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(apikey,channel,message)
    getdata = requests.get(url=url).json()
    return getdata

def senddice(apikey,channel):
    url="https://api.telegram.org/bot{}/sendDice?chat_id={}".format(apikey,channel)
    getdata = requests.get(url=url).json()
    return getdata

def sendsticker(apikey,sticker,channel):
    url="https://api.telegram.org/bot{}/sendSticker?chat_id={}&sticker={}".format(apikey,channel,sticker)
    getdata = requests.get(url=url).json()
    return getdata
