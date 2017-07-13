# coding=utf-8
import MySQLdb
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
mysqlHost = "localhost"
mysqlDB="sys"
mongoHost="localhost"
user1="root"
password1='sampson'
import calendar
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from chainmap import ChainMap
conn = MySQLdb.connect(host='localhost', user=user1, passwd=password1, db=mysqlDB, port=3306,charset = 'utf8')
cur = conn.cursor()
sql = 'SELECT * from weather where shi="杭州"'
weather = pd.read_sql(sql,conn,index_col='time')
aag = cur.execute('SELECT * from weather where shi="杭州"')
info = cur.fetchmany(aag)
cur.close()
conn.commit()
conn.close()

def getWeatherFeature():
    conn = MySQLdb.connect(host='localhost', user=user1, passwd=password1, db=mysqlDB, port=3306, charset='utf8')
    cur = conn.cursor()
    sql = 'SELECT * from weather where shi="杭州"'
    weather = pd.read_sql(sql, conn, index_col='time')
    aag = cur.execute('SELECT * from weather where shi="杭州"')
    info = cur.fetchmany(aag)
    cur.close()
    conn.commit()
    conn.close()

    t = 3
    feathre = []
    values = []
    for idx in weather.index:  # 前后三天
        all_feature={}
        # if datetime.datetime(2011, 1, 4) <= idx <= datetime.datetime(2016, 12, 28):
        if idx == datetime.datetime(2016, 12, 28):
            weather_z = {}
            wind1_z = {}
            wind2_z = {}
            temp_z = {}
            d = 2*t+1
            day_night = {}
            temp_day_day = {}
            temp_night_night = {}
            temp_day_night = {}
            temp_night_day = {}
            for i in range(1,d+1):
                forward = idx - datetime.timedelta(days=t) + datetime.timedelta(days=i-1)  # 七天时间

                weahter1 = {"weather_day" + str(i): weather.loc[forward]['weather_day'],"weather_night" + str(i): weather.loc[forward]['weather_night']}
                weather_z = dict(weather_z, **weahter1)

                wind1 = {"wind_day1" + str(i): weather.loc[forward]['wind_day1'],"wind_night1" + str(i): weather.loc[forward]['wind_night1']}
                wind1_z = dict(wind1_z, **wind1)

                wind2 = {"wind_day2" + str(i): weather.loc[forward]['wind_day2'],"wind_night2" + str(i): weather.loc[forward]['wind_night2']}
                wind2_z = dict(wind2_z, **wind2)

                temp = {"tem_day" + str(i): weather.loc[forward]['tem_day'],"tem_night" + str(i): weather.loc[forward]['tem_night']}
                temp_z = dict(temp_z, **temp)

                day_day1={"day" + str(i)+":day"+str(j+1): weather.loc[forward]['tem_day'] - weather.loc[forward + datetime.timedelta(days=j)]['tem_day'] for j in range(1,d+1-i) }  # 日温差
                temp_day_day=dict(temp_day_day,**day_day1)

                night_night1= {"night" + str(i)+":next_night"+str(i+j): weather.loc[forward]['tem_night'] -weather.loc[forward + datetime.timedelta(days=j)]['tem_night'] for j in range(1,d+1-i) }   # 夜温差
                temp_night_night = dict(temp_night_night,**night_night1)

                day_night1={"day" + str(i)+":night"+str(i+j): weather.loc[forward]['tem_day'] - weather.loc[forward+ datetime.timedelta(days=j)]['tem_night'] for j in range(0,d-i)}   # 日夜温差
                temp_day_night=dict(temp_day_night,**day_night1)

                night_day1={"night" + str(i)+":next_day"+str(i+j): weather.loc[forward]['tem_night'] -weather.loc[forward + datetime.timedelta(days=j)]['tem_day'] for j in range(1,d+1-i)}  # 大量日夜温差  1-7天
                temp_night_day=dict(temp_night_day,**night_day1)

            all_feature=dict(weather_z.items()+wind1_z.items()+wind2_z.items()+temp_z.items()+temp_day_day.items()+temp_night_night.items()+temp_day_night.items()+temp_night_day.items())          #多个字段字典合并
            feathre = all_feature.keys()
            value = all_feature.values()
            values.append(value)

        else:
            continue

    all_values = pd.DataFrame(values,columns=feathre)
    all_values = all_values.concat(weather)

hangzhou_date = weather[[5]]

feathre = []
values = []
times = []
for idx in hangzhou_date.index:  # 前7天 后三天
    if datetime.datetime(2011, 1, 10) <= idx <= datetime.datetime(2016, 12, 20):
        d = 10
        disease_z = {}
        time = {"time": idx}
        for i in range(0, d):
            forward = idx - datetime.timedelta(days=(7 - i))  # 七天时间
            try:
                infection = {"disease_day" + str(i - 7): hangzhou_date.loc[forward]['tem_night']}
            except:
                infection = {"disease_day" + str(i - 7): hangzhou_date.loc[forward]['tem_night']}
            disease_z = dict(disease_z, **infection)

        feathre = disease_z.keys()
        value = disease_z.values()
        values.append(value)
    else:
        continue
disease_values = pd.DataFrame(values, columns=feathre)
disease_values.head()