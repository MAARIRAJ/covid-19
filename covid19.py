import requests
from win10toast import ToastNotifier
import time
import json

def update():
    count=0
    while count<2:
        r=requests.get("https://api.covidtracking.com/v1/status.json")
        data=r.json()
        text=f'Time : {data["buildTime"]} \nProduction :  {data["production"]},\nRun : {data["runNumber"]}'
        toast =ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration=10)
        count+=1
        time.sleep(20)
update()


'''https://reqres.in/'''

