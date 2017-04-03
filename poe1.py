from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML

import urllib
import urllib2
import json
url = 'http://poe.trade/search'
data = urllib.urlencode({'name' : 'springs',
                         'league'  : 'legacy'})
content = urllib2.urlopen(url=url, data=data).read()

parser = MyHTMLParser()
parser.feed(content)
