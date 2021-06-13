# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:54:26 2021

@author: 19000
"""

import requests
import base64
# -*- coding: utf-8 -*-
import pymysql
import os
import json
import base64
#from flask_cors import *
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)
idList=[1]
db = pymysql.connect(host='175.24.114.16', port=3306, user='coworkers', passwd='2021irs', db='irs_plant_data', charset='utf8')
cur = db.cursor()
@app.route('/select',methods=['GET','POST'])
#@app.route('/transId')
def getId():
    selected_list=[]
    data=json.loads(request.get_data(as_text=True))
    for i in data['selected']:
        if i[-1]=='属':
            selected_list.append(i)
    ans=[]
    for i in selected_list:
        sql=f"select distinct * from tom where 属名='{i}';"
        cur.execute(sql)
        data = cur.fetchall()
        if data:
            for i in data:
                cats=[i[12][:-1],i[11],i[10],i[9],i[8]]
                cat='->'.join(cats)
                img='https://raw.githubusercontent.com/lunnar-being/30questions/master/'+i[2]+'/1.jpg'
                text = {'id':i[0],'LatinName':i[1],'name_ch':i[2],'Genus':i[3],'Family':i[4],'Order':i[5],'Class':i[6],'Phylum':i[7],'shu':i[8],'ke':i[9],'mu':i[10],'gang':i[11],'men':i[12],'distribution':i[13],'content':i[14],'color':i[15],'花瓣数':i[16],'flower_shape':i[17],'flower_date':i[18],'leaf':i[19],'func':i[20],"cat":cat,"img":img}
                    # print(text)
                ans.append(text)
    return(json.dumps(ans, ensure_ascii=False, indent=4))
@app.route('/image',methods=['POST','GET'])
def getImage():
    if request.method == 'POST':
        f = request.files['file']
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
     #二进制方式打开图片文件
        img = base64.b64encode(f.read())
        params = {"image": img}
        access_token = '24.56650b507916d366d0eea0e3cc1a1fa6.2592000.1625794968.282335-23974442'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        res=None
        if response:
            res=response.json()['result']
        ans=[]
        for i in res:
            name=i['name']
            sql=f"select distinct * from tom where 中文名='{name}';"
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                cats=[i[12][:-1],i[11],i[10],i[9],i[8]]
                cat='->'.join(cats)
                img='https://raw.githubusercontent.com/lunnar-being/30questions/master/'+i[2]+'/1.jpg'
                text = {'id':i[0],'LatinName':i[1],'name_ch':i[2],'Genus':i[3],'Family':i[4],'Order':i[5],'Class':i[6],'Phylum':i[7],'shu':i[8],'ke':i[9],'mu':i[10],'gang':i[11],'men':i[12],'distribution':i[13],'content':i[14],'color':i[15],'花瓣数':i[16],'flower_shape':i[17],'flower_date':i[18],'leaf':i[19],'func':i[20],"cat":cat,"img":img}
                    # print(text)
                ans.append(text)
        print(ans)
        return json.dumps(ans,ensure_ascii=False, indent=4)
@app.route('/advanced',methods=['POST','GET'])
def postAdvance():
    data=json.loads(request.get_data(as_text=True))
    print(data)
    res=data[0]['value']
    for i in data[1:]:
        res+=' '
        res+=i['region']
        res+=' '
        res+=i['value']
    print(res)
    return ('shoudao')
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
