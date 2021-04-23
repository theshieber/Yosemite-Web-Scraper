from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

url = "https://www.nps.gov/yell/learn/photosmultimedia/soundlibrary.htm"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "lxml")

print "collecting links..."
unfilteredLinks = []
for link in soup.findAll('a'):
	unfilteredLinks.append(link.get('href'))


print "filtering links..."
filteredLinks = []
for link in unfilteredLinks:
	if link[0:10] == "/yell/lear":
		filteredLinks.append(link)

print "collecting mp3 URL's..."
mp3URLs = []
for link in filteredLinks:
	page = urlopen("https://www.nps.gov" + link)
	html_bytes = page.read()
	html = html_bytes.decode("utf-8")
	soup = BeautifulSoup(html, "lxml")
	for link in soup.findAll('audio'):
		strLink = str(link)
		splitLink = strLink.split(" ")
		mp3URL = "https://www.nps.gov" + (splitLink[9].split("\""))[1]
		print("     " + mp3URL)
		mp3URLs.append(mp3URL)

print "downloading mp3's..."
for mp3 in mp3URLs:
	filedata = urlopen(mp3)
	datatowrite = filedata.read()
	mp3Label = mp3.split("/")[-1]
	mp3path = "/Users/elishieber/Desktop/Web Scraper/Scraped/" + mp3Label
	print("     " + mp3Label)
	mp3URLs.append(mp3URL)
	with open(mp3path, 'wb') as f:
		f.write(datatowrite)
