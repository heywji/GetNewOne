#!/bin/usr/env python3
# -*- coding:utf-8 -*-
# @function:random dictum
# @author:jiwenkangatech@foxmail.com
# @license:MIT License

import requests
import json

class GetNewOne():
    def __init__(self):
        self.data = None
    
    def getSentence(self):
	"""
		API 去这里申请哦：https://www.juhe.cn/docs/api/id/669
	"""
        url = 'https://apis.juhe.cn/fapig/soup/query?key=7b2a9d55b8xxxxxxxxxxxxxxxxxxxx67'
        response = requests.get(url)
        if response.status_code==200:
            originData = response.content.decode('utf-8')
            data = json.loads(originData)
            self.data = data['result']['text']
    
    def sendNotify(self):
	"""
		API 去这里申请哦：https://www.pushdeer.com/official.html#%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF
	"""
        url = 'https://api2.pushdeer.com/message/push?pushkey=PDU883xxxxxxxxxxxxxxxxxxxxxGfmRRaFGVBIql&text='+ self.data
        response = requests.get(url)
        if response.status_code==200:
            print('发送成功')
        else:
            print('发送失败')

getnewone = GetNewOne()
getnewone.getSentence()
getnewone.sendNotify()
