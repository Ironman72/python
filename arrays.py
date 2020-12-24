from array import *  # importing array module

# declaring an array with name of my_arr,, array("i") should be type of array
my_arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

my_arr.append(10)  # using append() adding a vale to end of the array
print(my_arr)  # printing an array


# using insert() inserting a element to an array in a specific index
my_arr.insert(10, 11)
print(my_arr)  # printing my array

# creating a new array with name of my_array1
my_arr1 = array("i", [12, 13, 14, 15, 16, 17, 18, 19, 20])
# using .extend()method extending 1st array with second array
my_arr.extend(my_arr1)
print(my_arr)  # printing the array
print(my_arr1[3])  # printing the array with index value

''' first method of looping throgh array'''
for i in my_arr:  # looping directly using values
    print(i)

'''second method of looping'''
# for i in range(len(my_arr)): # looping through range
#     print(i)


'''Taking input from user and assigning it into an array'''
empty_array = array("i", [])  # creating an empty array
# asking user to specify the number of items
u_enter = int(input("Please enter the number of items want to type: "))
for i in range(u_enter):  # using for loop from the given input from user
    # specifying user input in the loop to add into empty array
    u_values = int(input("Enter the value: "))
    # appending the values into the empty array that taken from the user values
    empty_array.append(u_values)
# printing the appended values of an array in outside of the loop
print(empty_array)
