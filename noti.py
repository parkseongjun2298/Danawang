#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

KEY = "bsE5AeiHGFzKvS7n2oM6rZ8IQEOVLh%2FO8gKrORcpl3fl2ut8D2TfLcTIbYTmwFOvj3tCfdUBxigtsKCz16bNwA%3D%3D"
TOKEN = '1814031402:AAGMfkJuVXJjp_WT5MYPaFme8BmA7CvwrX8'
MAX_MSG_LENGTH = 300
martBaseurl = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getStoreInfoSvc.do?ServiceKey="
goodsBaseurl = "http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/getProductInfoSvc.do?ServiceKey="

def getMartData(martName):
	res_list = []
	temp_list = []
	url = martBaseurl+KEY
	#print(url)
	res_body = urlopen(url).read()
	#print(res_body)
	soup = BeautifulSoup(res_body, 'html.parser')
	items = soup.findAll('iros.openapi.service.vo.entpinfovo')
	#print(items)
	for item in items:
		item = re.sub('<.*?>', '|', item.text)
		tempparsed = item.split('|')
		parsed = tempparsed[0].split('\n')
		try:
			martInfo = '상호명 : ' + parsed[2] + '\n주소 : ' + parsed[8] + parsed[9]
		except IndexError:
			martInfo = item.replace('|', ',')

		if martInfo:
			temp_list.append(martInfo.strip())

	for minfo in temp_list:
		if martName in minfo:
			res_list.append(minfo.strip())

	#print(res_list)

	return res_list

def getGoodsData(goodName):
	res_list = []
	temp_list = []
	url = goodsBaseurl+KEY
	#print(url)
	res_body = urlopen(url).read()
	#print(res_body)
	soup = BeautifulSoup(res_body, 'html.parser')
	items = soup.findAll('item')
	for item in items:
		item = re.sub('<.*?>', '|', item.text)
		tempparsed = item.split('|')
		parsed = tempparsed[0].split('\n')
		try:
			goodsInfo = '상품명 :' + parsed[2] + '\n용량 : ' + parsed[7] + parsed[8]
		except IndexError:
			goodsInfo = item.replace('|', ',')

		if goodsInfo:
			temp_list.append(goodsInfo.strip())

	for ginfo in temp_list:
		if goodName in ginfo:
			res_list.append(ginfo.strip())

	return res_list


def sendMessage(msg):
 	bot = telepot.Bot(TOKEN)
 	print(bot.getMe())
 	bot.sendMessage('1871728424', msg)


def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData(param)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg) + 1> MAX_MSG_LENGTH:
                    sendMessage(  msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( msg )
    conn.commit()


if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')
    print( '[',today,']received token :', TOKEN )
    bot = telepot.Bot(TOKEN)
    pprint( bot.getMe() )
    run(current_month)