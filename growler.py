#!/usr/bin/env python27

#Importing the modules

from BeautifulSoup import BeautifulSoup
import sys
import urllib2
import re
import json

title = raw_input("Please enter a movie title: ")
year = raw_input("which year? ")
raw_string = re.compile(r' ')
searchstring = raw_string.sub('+', title)
print searchstring
url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year
response = json.load(urllib2.urlopen(request))
request = urllib2.Request(url)
print json.dumps(response,indent=2)
