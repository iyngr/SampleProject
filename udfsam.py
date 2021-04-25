def user_def():
    print("An example function")
    print("The second string")


user_def()


# Arguments in UDF

def user_def1(str1, str2):
    print(str1)
    print(str2)


user_def1("Arg1", "Arg2")


# Default arguments
def print_st(name="", age=""):
    print("Name is ", name, "age is ", age)

    print_st("Keshava", 25)


# Keyword Arguments
def print_something(name="Keshava", age="Unknown"):
    print("Name is ", name, "Age is ", age)
    print_something(age=27, name="Keshava")


# Infinite number of arguments
def print_people(*people):
    for person in people:
        print("This person is", person)

        print_people("Keshava", "Dan", "Nick", "Jack", "King", "Smiley")


# Return values in functions
def do_math(num1, num2):
    return num1 + num2


sum = do_math(5, 7)
sum2 = do_math(12, 11)
print(sum, sum2)
