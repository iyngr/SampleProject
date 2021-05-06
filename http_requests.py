# Requests Intro
import requests
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
r = requests.get("http://3.bp.blogspot.com/-MNJU7nTcF7w/UVKfKSrqHnI/AAAAAAAAAA4/DtCEkOlQcH8/s1600/Emperor+Penguin+Looking+Awesome.jpg")
print(r.status_code)
image = Image.open(BytesIO(r.content))
path = "./image.jpg" + image.format
print(image.size, image.mode, image.format)
try:
    image.save(path, image.format)
except IOError:
    print("Couldn't save image")

# POST Data

my_data = {"name1":"Keshava","email":"info@keshava.com"}
r = requests.post("https://w3schools.com/php/welome.php", data=my_data)

f = open("myfile.html","w+")
f.write(r.text)