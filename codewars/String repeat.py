# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"


# in this function we created an empty string that will then be put in the for loo
# and that for loop will be the one responsible to concatenate the string and how many times
# it will run
def repeat_str(repeat, string):
    result = ''

    for i in range(repeat):
        result += string

    return result