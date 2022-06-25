import requests
import json


response=requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220624&selectType=30&_=1656121647054re')
print(response.json()['data'])