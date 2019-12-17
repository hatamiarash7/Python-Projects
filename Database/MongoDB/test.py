import pymongo
import requests
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ip"]
mycol = mydb["data"]

URL = "https://api.ipgeolocation.io/ipgeo"
API_KEY = "api" 

print('Start fetching data ...')
index = 1

file = open("v.txt",'r')
lines = file.readlines()

for IP in lines:
  IP = IP.replace('\n', '')
  print(IP)
  # fetch data
  PARAMS = {'apiKey':API_KEY, 'ip':IP}
  r = requests.get(url = URL, params = PARAMS) 
  data = r.json() 
  #insert to db
  x = mycol.insert_one(data)