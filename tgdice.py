#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import pytg
import time
import random


token = str(input("Enter the token of the bot: "))
channel = str(input("Enter the group ID: "))
sleep = str(input("Enter sleep time: [5] "))
if sleep == "0":
    sleep = "1"
elif sleep == "":
    sleep = "5"

print(pytg.send(token,"%23DiceBot %23DiceBotStart\nBot session start!\nSend dice per {} second".format(sleep),channel))

dice1,dice2,dice3,dice4,dice5,dice6,diceBAN,dicenonstop = 0,0,0,0,0,0,0,0

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
            if result["result"]["dice"]["value"] == 1:
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
            if lucky == 0:
                result = pytg.sendsticker(token,"CAACAgIAAxkBAAMEXolx18fLBEz726hs5ujKoLVB-zcAAgRzAAKezgsAAY2zz5SZwiUlGAQ",channel)
                diceBAN = diceBAN + 1
                print(result)
            elif lucky == 1:
                result = pytg.sendsticker(token,"CAACAgIAAxkBAAMFXolx2KD2jRIYi9aPSgxHv44i0DoAAgVzAAKezgsAAZcFf4sIxmfIGAQ",channel)
                dicenonstop = dicenonstop + 1
                print(result)
            time.sleep(int(sleep))
    except KeyboardInterrupt:
        break

print(pytg.send(token,"%23DiceBot %23DiceBotReport\nBot session ended!\n⚀×{}\n⚁×{}\n⚂×{}\n⚃×{}\n⚄×{}\n⚅×{}\nBAN×{}\nNonstop×{}".format(dice1,dice2,dice3,dice4,dice5,dice6,diceBAN,dicenonstop),channel))
