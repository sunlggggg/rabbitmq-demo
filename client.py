#!/usr/bin/env python
#coding: UTF-8
import pika
import requests
import requests

r = requests.get("https://cache.zhibo8.cc/json/2018_10_25/news/nba/130734_hot.htm")
# 创建一个连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) 
#创建通道
channel = connection.channel() 
#把消息队列的名字为comment
channel.queue_declare(queue='comment')
channel.basic_publish(exchange='', routing_key='comment',body=r.text.decode('unicode_escape')) 
print r.text.decode('unicode_escape')
print(" [x] Sent Comment!")
