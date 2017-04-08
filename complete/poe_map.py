from bs4 import BeautifulSoup
import urllib
import urllib2

url = 'http://poe.trade/search'
data = urllib.urlencode({'name' : 'Enduring Beyond Leaguestone of the Call',
                         'league'  : 'Legacy'})
content = urllib2.urlopen(url=url, data=data).read()
data  = BeautifulSoup(content, 'lxml')
parsed = data.select("tbody[id*=item-container-]")
same = []

for i in parsed:
    print('@')+(i['data-ign'])+ (' Hi, I would like to buy your ')+(i['data-name'])+ (' listed for ')+(i['data-buyout'])+(' in Legacy') + ('\n')




