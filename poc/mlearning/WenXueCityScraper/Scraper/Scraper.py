# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests



import sys
import matplotlib.pyplot as plt

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://bbs.wenxuecity.com/h1b/604577.html',
            'http://bbs.wenxuecity.com/family/596651.html',
            'http://bbs.wenxuecity.com/h1b/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            print response.body
        self.log('Saved file %s' % filename)


Q = QuotesSpider()
for q in Q.start_requests():
    print q
    Q.parse(q)

# # resp = requests.get('http://finance.yahoo.com/echarts?s=JNPR#{"range":"max","allowChartStacking":true}')
# url = 'http://bbs.wenxuecity.com/h1b/604577.html'
# url = 'http://bbs.wenxuecity.com/family/596651.html'
# # resp = requests.get(url)
# # print resp.encode('utf-8')
# # soup = BeautifulSoup(resp.text, 'html.parser')
#
# #url = "http://www.columbia.edu/~fdc/utf8/"
# r = requests.get(url)
# #print r.text
# r = requests.get(url)
#
# encodedText = r.text#.encode("utf-8")
# #print encodedText.decode('utf-8')
# #print '--------'.encode('utf-8')
# soup = BeautifulSoup(encodedText, "lxml")
# print soup.get_text()
# text =  str(soup.findAll(text=True))
# #print text.encode("utf-8") >> sys.stdout
#
#
# # for t in text.decode("utf-8"):
# #     print t
#
# #print soup.get_text()  # .find('var ')

"""
import ast
CONTs = soup.body.contents

index = 0
for cont in CONTs:
    print index
    print cont
    index = index + 1

soup2string = CONTs[31].string
#print soup2string

ss = soup2string[24:].split(';')




soupitems = ss[0].split('\n')

index = 0
for s in soupitems:
    print index
    print s
    print
    print
    index = index + 1

print '----------------------------------------------------------------------'
newstr = ast.literal_eval(soupitems[1][27:-1])
print 'the length of newstr is :  ', len(newstr)
print 'the elements in newstr is : \n'

for item in newstr:
    print item
    print

#newstr = ast.literal_eval(soupitems[1][27:-1])

#print soup2string[24:].split(';')[0].split('\n')[4][27:100]

import pandas as pd
#note: the index of newstr[i] controls the number of bedrooms
PD1bed = pd.DataFrame(newstr[3]['points'])
#print PD1bed
pddate = pd.to_datetime(PD1bed.date)
pdvalue = pd.to_numeric(PD1bed.value)
#print pddate
plt.plot(pddate, pdvalue,'-')
plt.show()
"""

