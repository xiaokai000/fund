
import requests
import baostock as bs
import pandas as pd
from pymongo import MongoClient

collection = MongoClient(host='127.0.0.1')['fund']['all_fund']



url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNInverstPosition?product=EFund&appVersion=6.4.2&serverVersion=6.4.2&FCODE={FCODE}&deviceid=5864c1192f56de0019596186fb3baa36%7C%7C766393540303768&version=6.4.2&userId=uid&DATE=2021-03-31&cToken=ctoken&MobileKey=5864c1192f56de0019596186fb3baa36%7C%7C766393540303768&appType=ttjj&OSVersion=9&plat=Android&uToken=utoken&passportid=12345678'


for item in collection.find({'$where':"!this.stock_list "}):
    code = item['_id']
    print(code)



    res = requests.get(url.format(FCODE=code))
    stockList = res.json()['Datas']['fundStocks']
    stockList = [{ 'stock_name': item['GPJC'], 'percent': item['JZBL'], 'industry': item['INDEXNAME']} for item in stockList ]
    collection.update_one({'_id': code}, {'$set': {'stock_list': stockList}})
