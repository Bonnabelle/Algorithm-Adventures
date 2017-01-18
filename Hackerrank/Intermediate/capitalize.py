def capitalize(string):
    string = string.split(" ")
    string = [word.capitalize() for word in string]
    return " ".join(string)

#Provided by creator
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

"""
You are given a string, String. Capitalize each word.
"""
