# Conditional statements
check = False

if check is False:
    print(0)
elif check == "Hamburger":
    print("2")
elif check == "Bacon":
    print("3")
else:
    print(1)

# Forward loop and while loop
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

run = True
current = 1

while run:
    if current == 100:
        run=False
    else:
        print(current)
        current += 1

# Import libraries and using Regex
import re
string ="You have gone incognito. Pages you browse are not tracked by the browser"
print(string)
new = re.sub('[A-Z]','',string)
print(new)
new = re.sub('[A-Z]','',string)