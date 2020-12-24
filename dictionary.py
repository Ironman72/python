color = {"Blue": 1,
         "Red": 2,
         "Green": 3,
         "Orange": 4
         }
color["red"] = 5  # retriving the value of red from dict

new_color = color.copy()  # copying the color dict into the new dict (new_color)
print(new_color)  # printing the copied dict  not the original list

# using the get method() we are getting the vale of "blue"
print(color.get("Blue"))

# print(color.update())  # updates the dict

# printing the all items that means key and values in the dict
print(color.items())
