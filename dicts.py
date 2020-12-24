mydict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

# # print(mydict['two'])
# mydict["six"] = 6
# print(mydict)
# mydict["six"] = 66
# print(mydict)


# def looping(dict):
#     for key in dict:
#         print(key,)


# print(looping(mydict))
# for i in mydict.items():
#     print(i)

# #searching through a dictonary
# 1) defining a function and taking dictionary as input and targeted value to find
# 2) using for loop iterate through the dictonary
# 3) in the for loop using if statement check the dict[key]== targeted
# 4) if the target and value in the dictionary matched it will print the both key and Value
# 5) else it exits from the loop
# 6) in the for loop intened we will return a simple statement to user "not found the value"

def searching(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "not found"


print(searching(mydict, 2))
print(searching(mydict, 3))

# trying to find with key
# same as previous but here we find with keys and return that key and value


def searching1(dict, value):
    for key in dict:
        if key == value:
            return key, dict[key]
    return "not valid"


print(searching1(mydict, "one"))
