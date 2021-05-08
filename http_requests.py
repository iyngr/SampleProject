# Requests Intro
import requests
import simplejson as json
from io import BytesIO
from PIL import Image

r = requests.get("https://google.com")
print("Status", r.status_code, r.url, r.headers, r.text)

f = open("./page.html", "w+")
f.write(r.text)

# GET Requests
params = {"#q": "pizza"}
r = requests.get("https://bing.com/search", params=params)
print("Status", r.status_code, r.url)

# Pillow Image processing Library (PIL)
r = requests.get(
    "http://3.bp.blogspot.com/-MNJU7nTcF7w/UVKfKSrqHnI/AAAAAAAAAA4/DtCEkOlQcH8/s1600/Emperor+Penguin+Looking+Awesome.jpg")
print(r.status_code)
image = Image.open(BytesIO(r.content))
path = "./image.jpg" + image.format
print(image.size, image.mode, image.format)
try:
    image.save(path, image.format)
except IOError:
    print("Couldn't save image")

# POST Data

my_data = {"name": "Keshava", "email": "info@keshava.com"}
r = requests.post("https://tryphp.w3schools.com/demo/welcome.php", data=my_data)

# Headers in requests
headers = {"Content-Type":"application/text"}
print(r.headers)

f = open("myfile.html", "w+")
f.write(r.text)

# Post JSON Data

url = "http://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "http://www.example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

print(json.loads(r.text))



