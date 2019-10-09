from urllib.request import urlopen

html = urlopen("http://google.com")
print(html.read())