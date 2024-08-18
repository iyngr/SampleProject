class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)


honeycrisp = Apple("red", "sweet")
print(honeycrisp)
'''This code defines a class called Apple and creates an instance of that class called honeycrisp. Let's break it 
down: 
1. Class Definition: class Apple:: This line defines a new class called "Apple". A class is like a blueprint 
for creating objects (like a real-world apple). 
2. Constructor (__init__): def __init__(self):: This defines the 
constructor of the Apple class. The constructor is a special method that gets called automatically when you create a 
new object (instance) of the class. self.color = "red": This line sets the color attribute of the newly created Apple 
object to "red". self.flavor = "sweet": This line sets the flavor attribute of the newly created Apple object to 
"sweet". 
3. Creating an Instance: honeycrisp = Apple(): This line creates a new instance of the Apple class and 
assigns it to the variable honeycrisp. Now, honeycrisp is an object that represents a specific apple. 
4. Accessing 
Attributes: print(honeycrisp.color): This line accesses the color attribute of the honeycrisp object and prints its 
value, which is "red". 
5. In essence: You defined a blueprint for apples (Apple class) with default properties (red and 
sweet). You created a specific apple (honeycrisp) based on that blueprint. You then accessed and printed the color of 
that specific apple.'''

speed_limits = {"street": 35, "highway": 65, "school": 15}
print(speed_limits["highway"])

genre = "transcendental"
print(genre[:-8])
print(genre[-7:9])
