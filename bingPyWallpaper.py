import urllib2
import json
import urllib
import commands

url = urllib2.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
json = url.read()
data = json.loads(json)

urllib.urlretrieve("http://bing.com/" + data['images'][0]['url'], "wallpaper.jpg")	

#Replace path_to_file with the file path
command = "gsettings set org.gnome.desktop.background picture-uri file:/home/sumedh/Projects/BingPyWallpaper/test.jpg"

status, output = commands.getstatusoutput(command)