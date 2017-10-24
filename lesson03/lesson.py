import urllib2
url = "https://www.dict.cc/?s=bier"
content = urllib2.urlopen(url).read()
print content
