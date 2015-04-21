import urllib2
import re

url = raw_input("URL: ")
html = urllib2.urlopen(url).read()

for link in re.findall("href=[\'\"].+[^>][\'\"]", html):
    print link
