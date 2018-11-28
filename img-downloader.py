"""
image downloader
can use this for any website if the image urls are like this 
--> https://www.somewebsite.com/1.jpg
--> https://www.somewebsite.com/2.jpg
--> https://www.somewebsite.com/3.jpg
and so on
just replace the url in line 15 with your website without the /1.jpg
and replace the range in line 19  with the number range of the images on the website 
"""

import urllib.request

def downloader(imgNum):
	url = ('http://startjoe.com/images/anime-new-tab/' + str(imgNum) + '.jpg')
	file_name = str(imgNum) + '.jpg'
	urllib.request.urlretrieve(url, file_name)

for i in range (1, 380):
	downloader(i)
	print (str(i) + '.jpg downloaded.')

