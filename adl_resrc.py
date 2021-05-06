import simplejson as json
import os

# Reading and Writing files in Python

new_file = open("new_file.txt", "w+")
string = "The content that would be written to the text file"
new_file.write(string)

# Reading an Writing and manipulating existing file in JSON

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- Adding a Year")
    data["age"] = int(data["age"]) + 1
    print("New age is " + str(data["age"]))
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Keshava", "age": "27"}
    print("No file found, writing age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))

# Using Virtual Environment to create a Virtual Env
# pip3 install virtual env
# virtualenv name of the virtualenv
# To activate it, env_name/bin/activate should open the Virtual Env and they are globally accessible too.
# PyPI - Package Index.
