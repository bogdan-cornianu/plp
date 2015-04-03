__author__ = 'bogdan.cornianu'
import urllib2
import re

url = input("URL: ")
html = urllib2.urlopen(url).read()

for link in re.findall('href=[\'"]?([^\'" >]+)', html):
    print link
