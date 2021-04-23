import requests
import baostock as bs
import pandas as pd
from pymongo import MongoClient

collection = MongoClient(host='127.0.0.1')['fund']['all_fund']

url = 'https://api.doctorxiong.club/v1/fund/all'



res = requests.get(url)

for item in res.json()['data']:
    fund_code = item[0]
    fund_name = item[2]
    fund_type = item[3]

    collection.insert_one({'_id': fund_code, 'fund_name': fund_name, 'fund_type': fund_type })