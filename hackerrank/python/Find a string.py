def count_substring(string, sub_string):
    counter = 0 # this is where were going to store the value of the count of how many times the substring appeared on the string

    for i in range(1, len(string)): # lets iterate through the string with how many letters are in it
        if sub_string in string: # this will check if the sub string exist on the string
            find = string.find(sub_string) # .find will find the substring index on the string ( the first letter of the sub_string)
            string = string[find + 1:] # now lets slice the string to where we found the first letter of the sub string
                                        # and then add 1 so the checker will move on to the next letter of the string.
                                        # because if we dont add 1 the if statement will become true again on the same letter from
                                        # the last time that the statement became true.
            counter += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)