from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import sys

url = 'http://poe.trade/search'


html_report_part1 = open('test.html','r').read()
data = BeautifulSoup(html_report_part1, "html.parser")

print(data.prettify())
parsed = data.find_all("tbody", id=re.compile("^item-container"))
