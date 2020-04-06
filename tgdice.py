#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import pytg
import time
import random
import json

langplace = str(input("Enter the lang json place: [./lang/en-us.json] "))
if langplace == "":
    langplace = "./lang/en-us.json"
langjson = json.load(open(langplace))
token = str(input("Enter the token of the bot: "))
channel = str(input("Enter the group ID: "))
sleep = str(input("Enter sleep time: [5] "))
if sleep == "0":
    sleep = "1"
elif sleep == "":
    sleep = "5"

print(pytg.send(token,"%23DiceBot %23DiceBotStart\nDiceBot v1.0.1-stable-v0.1.0-alpha\n{}\nSend dice per {} second".format(langjson["start"],sleep),channel))

dice1,dice2,dice3,dice4,dice5,dice6,diceBAN,dicenonstop,dicecant = 0,0,0,0,0,0,0,0,0

while True:
    try:
        lucky = random.randint(0,1)
        if lucky == 0:
            result = pytg.senddice(token,channel)
            print(result)
            if result["ok"] == False:
                if result["error_code"] == 429:
                    time.sleep(result["parameters"]["retry_after"] + 1)
                    continue
            elif result["result"]["dice"]["value"] == 1:
                dice1 = dice1 + 1
            elif result["result"]["dice"]["value"] == 2:
                dice2 = dice2 + 1
            elif result["result"]["dice"]["value"] == 3:
                dice3 = dice3 + 1
            elif result["result"]["dice"]["value"] == 4:
                dice4 = dice4 + 1
            elif result["result"]["dice"]["value"] == 5:
                dice5 = dice5 + 1
            elif result["result"]["dice"]["value"] == 6:
                dice6 = dice6 + 1
            time.sleep(int(sleep))
        elif lucky == 1:
            lucky = random.randint(0,1)
            elif lucky == 0:
                result = pytg.sendsticker(token,"CAACAgIAAxkBAAMEXolx18fLBEz726hs5ujKoLVB-zcAAgRzAAKezgsAAY2zz5SZwiUlGAQ",channel)
                diceBAN = diceBAN + 1
                print(result)
            elif lucky == 1:
                lucky = random.randint(0,20)
                if lucky != 20:
                    result = pytg.sendsticker(token,"CAACAgIAAxkBAAMFXolx2KD2jRIYi9aPSgxHv44i0DoAAgVzAAKezgsAAZcFf4sIxmfIGAQ",channel)
                    dicenonstop = dicenonstop + 1
                else:
                    result = pytg.sendsticker(token,"CAACAgIAAxkBAAMCXomZFLxb5_AtGnij69ssbI4vjpEAAppcAAKezgsAATg8wxLSaVSzGAQ",channel)
                print(result)
            time.sleep(int(sleep))
        if result["ok"] == False:
            dicecant = dicecant + 1
            if result["error_code"] == 429:
                time.sleep(result["parameters"]["retry_after"] + 1)
            if result["error_code"] == 400:
                if result["description"] == 'Bad Request: have no rights to send a message':
                    time.sleep(int(30))
    except KeyboardInterrupt:
        break

print(pytg.send(token,"%23DiceBot %23DiceBotReport\n{}\n⚀×{}\n⚁×{}\n⚂×{}\n⚃×{}\n⚄×{}\n⚅×{}\nBAN×{}\nNonstop×{}\nCant Send×{}".format(langjson["ended"],dice1,dice2,dice3,dice4,dice5,dice6,diceBAN,dicenonstop,dicecant),channel))
