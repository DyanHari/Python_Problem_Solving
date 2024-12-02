#Write a function to split a string and convert it into an array of words.

#   "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

# we write a function that uses a method called split where you decide how you will split some strings
# in our case we splitted it by space so everytime a word ends with space it get splitted and then
# that splitted word then putted to the string. thats what the split method does
def string_to_array(s):
    return s.split(' ')