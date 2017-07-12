# coding=utf-8

"""
Created on 2016-04-28
@author: xuzhiyuan

功能: 爬取新浪微博的搜索结果,支持高级搜索中对搜索时间的限定
网址：http://s.weibo.com/
实现：采取selenium测试工具，模拟微博登录，结合PhantomJS/Firefox，分析DOM节点后，采用Xpath对节点信息进行获取，实现重要信息的抓取

"""
# import MySQLdb

mysqlHost = "localhost"
mysqlDB = "sys"
# mongoHost="localhost"
user1 = "root"
password1 = 'root'
import time
import datetime
import re
from selenium import webdriver
from selenium import webdriver
import MySQLdb
mysqlHost = "localhost"
mysqlDB="sys"
# mongoHost="localhost"
user1="root"
password1='sampson'
import calendar

# 先调用无界面浏览器PhantomJS或Firefox
# driver = webdriver.PhantomJS()
driver = webdriver.Chrome(executable_path=r"E:\DATA\chromedriver_win32\chromedriver.exe")
# ********************************************************************************
#                  第二步: 访问http://s.weibo.com/页面搜索结果
#               输入关键词、时间范围，得到所有微博信息、博主信息等
#                     考虑没有搜索结果、翻页效果的情况
# ********************************************************************************

def GetSearchContent(shi_qu,months):

    for ci in range(1,shi_qu+1):   #11个地级市
        driver.get("http://www.tianqihoubao.com/lishi/zhejiang.htm")
        citys = driver.find_element_by_xpath('//*[@class="citychk"]/dl['+str(ci)+']/dd').text
        citys = citys.split(" ")
        city_first = citys[0]
        for i in range(1,len(citys)+1):  #获取每个市的地级县区
            driver.get("http://www.tianqihoubao.com/lishi/zhejiang.htm")
            shi  = driver.find_element_by_xpath('//*[@class="citychk"]/dl['+str(ci)+']/dd/a['+str(i)+']').text
            href = driver.find_element_by_xpath('//*[@class="citychk"]/dl['+str(ci)+']/dd/a['+str(i)+']').get_attribute("href")
            href = href.split(".html")[0]
            for k in range(1,months+1):       #60个月 2011-2016
                m = k%12
                if m==0:                       #月校验
                    m=12
                n = 0
                if k>12:                        #年校验
                    n=(k-1)/12
                times_day = time.localtime(time.mktime(datetime.datetime(2011+n, m, 1).timetuple()))
                monthRange = calendar.monthrange(2011+n, m)
                days = monthRange[1]
                href1 = href + "/month/" + str((2011 + n) * 100 + m) + ".html"
                driver.get(href1)
                values=[]
                for d in range(1,days+1):    #每个月多少天

                    day=datetime.datetime(2011 + n, m, d)
                    e = d + 1
                    try:
                        day_time    = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr['+str(e)+']/td[1]/a').text
                        wether      = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr['+str(e)+']/td[2]').text
                        weather_day      = wether.split("/")[0]
                        weather_night    = wether.split("/")[1]
                        temperature = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr['+str(e)+']/td[3]').text
                        tem_day     = temperature.split("/")[0]
                        tem_day     = int(filter(lambda ch: ch in '0123456789-', tem_day))
                        tem_night   = temperature.split("/")[1]
                        tem_night   = int(filter(lambda ch: ch in '0123456789-', tem_night))
                        wind        = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr['+str(e)+']/td[4]').text
                        wind_day    = wind.split("/")[0]
                        wind_day1   = wind_day.split(" ")[0]
                        wind_day2   = wind_day.split(" ")[1]
                        wind_night  = wind.split("/")[1]
                        wind_night1 = wind_night.split(" ")[0]
                        wind_night2 =wind_night.split(" ")[1]
                    except:
                        continue
                    values.append((city_first.encode('UTF-8'),shi.encode('UTF-8'),day,weather_day.encode('UTF-8'),weather_night.encode('UTF-8'),tem_day,tem_night,wind_day1.encode('UTF-8'),wind_day2.encode('UTF-8'),wind_night1.encode('UTF-8'),wind_night2.encode('UTF-8')))
                conn = MySQLdb.connect(host='localhost', user=user1, passwd=password1, db=mysqlDB, port=3306,charset="utf8")
                cur = conn.cursor()
                cur.executemany('insert into weather values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', values)
                conn.commit()
                cur.close()
                conn.close()
if __name__ == '__main__':
    shi_qu=11
    months = 72
    conn = MySQLdb.connect(host='localhost', user=user1, passwd=password1, db=mysqlDB, port=3306,charset="utf8")
    cur = conn.cursor()
    cur.execute('create table weather (city_first varchar(300),shi varchar(300),time datetime,weather_day varchar(300),weather_night varchar(300),tem_day int,tem_night int,wind_day1 varchar(300),wind_day2 varchar(300),wind_night1 varchar(300),wind_night2 varchar(300))')
    conn.commit()
    cur.close()
    conn.close()
    GetSearchContent(shi_qu,months)
