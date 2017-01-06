import os
import urllib, urllib.parse, urllib.request
import json

# query for images
url = 'http://www.panoramio.com/map/get_panoramas.php?order=popularity&\
set=public&from=0&to=20&minx=-77.037564&miny=38.896662&\
maxx=-77.035564&maxy=38.898662&size=medium' #url not working now 1/4/2017
url = 'http://schematic-ipsum.herokuapp.com/'
c = urllib.request.urlretrieve(url)
print (c)
# get the urls of individual images from JSON
j = json.load(c.read())
imurls = []
for im in j['photo']:
    imurls.append(im['photo_file_url'])

# download images
for url in imurls:
    image = urllib.URLopener()
    image.retrieve(url, os.path.basename(urllib.parse.urlparse(url).path))
    print ('downloading:', url)
