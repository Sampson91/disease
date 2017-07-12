import requests

import urllib
import lxml.html as H
import time
from lxml import etree


url = 'http://www.tianqihoubao.com/lishi/hangzhou/month/201101.html'
# html = requests.get(url)
values = []

page = urllib.urlopen(url)
html = page.read()
doc = H.document_fromstring(html)

title = doc.xpath('//*[@id="content"]/table/tbody/tr[2]/td[1]/a/text()')
#title = doc.xpath('//*[@id="content"]/div[3]/dl[1]/dt/a/text()')
print(title)
for shi in title:
    print shi.xpath("/dt/a/@href"),shi.xpath("/dt/a/text()")
datetime = doc.xpath("//*[@class='release-authorship']/time/@datetime")