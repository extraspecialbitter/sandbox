import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 5wP44Zxy7irccurw0YJsxy:5FyeP2cvsXmk9ZCCvp9dK6"
    }

conn.request("GET", "/chancegame/usaMegaMillions", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
