from flask import Flask, request
from flask_cors import CORS
import requests
import base64
# -*- coding: utf-8 -*-
# import pymysql
import os
import json
#from flask_cors import *
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app = Flask(__name__)
CORS(app, supports_credentials=True)
idList = [1]


@app.route('/')
# @app.route('/transId')
def getId():

    a = request.args.get('id')
    idList.append(a)
    return str(idList[-1])


@app.route('/image')
def getImage():
    if request.method == 'POST':
        f = request.files['file']
        print(type(f))
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"

    # 二进制方式打开图片文件
        f = open('C:\\Users\\19000\Pictures\\flower1.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        access_token = '24.56650b507916d366d0eea0e3cc1a1fa6.2592000.1625794968.282335-23974442'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
        return ("shoudao")
# @app.route('/info')
# def getcontent():
#     db = pymysql.connect(host='175.24.114.16', port=3306, user='test', passwd='20010914', db='test', charset='utf8')
#     cur = db.cursor()
#     spid=idList[-1]
#     sql = "SELECT speach_id,title,master,classification,spot,time,sp_dept,label,master_info,sp_info,pic_url FROM `speach` where speach_id=%s;"
#     cur.execute(sql,(spid))
#     data = cur.fetchall()
#     # print(data)
#     para = []
#     for i in data:
#         text = {'id':i[0],'title':i[1],'master':i[2],'classification':i[3],'spot':i[4],'time':i[5],'sp_dept':i[6],'label':i[7],'master_info':i[8],'sp_info':i[9],'pic_url':i[10]}
#         # print(text)
#         para.append(text)
#     return json.dumps(para, ensure_ascii=False, indent=4)
# favorList=[]
# @app.route('/favor')
# def addfavor():
#     a=request.args.get('spid')
#     favorList.append(a)
#     return str(favorList[-1])
# @app.route('/favorite')
# def getfavorite():
#     db = pymysql.connect(host='175.24.114.16', port=3306, user='test', passwd='20010914', db='test', charset='utf8')
#     cur = db.cursor()
#     if len(favorList)==0:
#         return ''
#     spid=favorList[-1]
#     sql = "SELECT speach_id,title,master,classification,spot,time,sp_dept,label,master_info,sp_info,pic_url FROM `speach` where speach_id=%s;"
#     cur.execute(sql,(spid))
#     data = cur.fetchall()
#     # print(data)
#     para = []
#     for i in data:
#         text = {'id':i[0],'title':i[1],'master':i[2],'classification':i[3],'spot':i[4],'time':i[5],'sp_dept':i[6],'label':i[7],'master_info':i[8],'sp_info':i[9],'pic_url':i[10]}
#         # print(text)
#         para.append(text)
#     return json.dumps(para, ensure_ascii=False, indent=4)
# @app.route('/login')
# def logincheck():
#     flag=0
#     db = pymysql.connect(host='175.24.114.16', port=3306, user='test', passwd='20010914', db='test', charset='utf8')
#     cur = db.cursor()
#     sid=request.args.get('sid')
#     spassword=request.args.get('spassword')
#     sql = "SELECT spassword FROM `student` where sid=%s"
#     cur.execute(sql,(sid))
#     data=cur.fetchall()
#     if str(spassword)==data:
#         flag=1
#     for i in data:
#         check={'password':i[0]}
#     return json.dumps(check, ensure_ascii=False, indent=4)
if __name__ == '__main__':
    app.run(host=('127.0.0.1'))

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
# 二进制方式打开图片文件
f = open('C:\\Users\\19000\Pictures\\flower1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = '24.56650b507916d366d0eea0e3cc1a1fa6.2592000.1625794968.282335-23974442'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
