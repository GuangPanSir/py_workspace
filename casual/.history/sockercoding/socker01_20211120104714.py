import urllib.request as request

url = 'http://127.0.0.1:5632/get_data'

req = request.Request(url)
with request.urlopen(req)