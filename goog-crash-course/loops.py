# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Python doesn't have a do-while loop.
# Here's a way to simulate its behavior:
j = 1
while True:
    print(j)
    j += 1
    if j > 5:
        break

# For loop
for k in range(1, 6):
    print(k)

# Nested for loop
for m in range(1, 4):
    for n in range(1, 4):
        print(f"({m}, {n})")

x = 1
sum = 5
while x <= 10:
    sum += x
    x += 1
print(sum)

for sum2 in range(5):
    sum2 += sum2
    print(sum2)

for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)
