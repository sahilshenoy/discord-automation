#Complete Discord Automation Applicable Anywhere Just Channel ID of 
# send_gif_channel_id and send_dankmemer_msg_channel_id and run

import requests
import time
import random
from ListofGifs import List
from BotSpam import *
from NamesList import *
from keys import *
send_gif_channel_id = 878442772166766603 #OP Chat
send_dankmemer_msg_channel_id = 892296240463749140 #Dank Memers Channel ID of Mallu Gang


#Sahil's GIF
def sendGif1():
    url = "https://discord.com/api/v9/channels/{}/messages".format(send_gif_channel_id)
    message = random.choice(List)
    payload = {'content' : message}
    header = {'authorization' : sahil_key}
    requests.post(url , data=payload , headers=header)

#Atul's GIF
def sendGif2():
    url = "https://discord.com/api/v9/channels/{}/messages".format(send_gif_channel_id)
    message = random.choice(List)
    payload = {'content' : message}
    header = {'authorization' : atul_key}
    requests.post(url , data=payload , headers=header)

#For Sending WOPing Messages Sahil
def sendWOPingMsg1():
    list = random.choice(WO_PingMsg)
    url = "https://discord.com/api/v9/channels/{}/messages".format(send_dankmemer_msg_channel_id)
    data = {'content': list}
    header = {'authorization': sahil_key}
    requests.post(url, data = data, headers = header)

#For Sending WOPing Messages Atul
def sendWOPingMsg2():
    list = random.choice(WO_PingMsg)
    url = "https://discord.com/api/v9/channels/{}/messages".format(send_dankmemer_msg_channel_id)
    data = {'content': list}
    header = {'authorization': atul_key}
    requests.post(url, data = data, headers = header)

#For Sending Ping Messages Sahil
def sendPingMsg1():
    list = random.choice(PingMsg)
    url = "https://discord.com/api/v9/channels/{}/messages".format(send_dankmemer_msg_channel_id)
    data = {'content': list}
    header = {'authorization': sahil_key}
    requests.post(url, data=data, headers=header)

#For Sending Ping Messages Atul
def sendPingMsg2():
    list = random.choice(PingMsg)
    url = "https://discord.com/api/v9/channels/{}/messages".format(send_dankmemer_msg_channel_id)
    data = {'content': list}
    header = {'authorization': atul_key}
    requests.post(url, data=data, headers=header)

x = int(input("Enter 1(Gif), 2(Dank Memer Non Ping Spam) and 3(Dank Memer Ping Spam): "))
if x == 1:
    while 1:
        sendGif1() #Sahil's GIF 
        time.sleep(15)
        sendGif2() #Atul's GIF
        time.sleep(15)
elif x == 2:
    while 1:
        #Sahil's WOPing Msg
        sendWOPingMsg1()
        time.sleep(8)
        #Atul's WOPing Msg
        sendWOPingMsg2()
        time.sleep(8)
elif x == 3:
    while 1:
        #Sahil's Ping Msg
        sendPingMsg1()
        time.sleep(8)
        #Atul's Ping Msg
        sendPingMsg2()
        time.sleep(8)