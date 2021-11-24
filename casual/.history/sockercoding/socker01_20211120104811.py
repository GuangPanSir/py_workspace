import urllib.request as request

url = 'http://127.0.0.1:5632/get_data'

req = request.Request(url)
with request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)