import requests
import time
#Checks if ynet has @word at time @time and if so, prints Mission Acomplished
def YnetHasIt(time,word,func):
    Over = True
    while (Over):
        if time.asctime( time.localtime(time.time()) )[11:16]==time:
            if word in requests.get('http://www.ynet.co.il/home/0,7340,L-8,00.html').text:
                print("Mission Acomplished")
            Over=False


