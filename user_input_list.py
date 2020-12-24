# prompting user for how many inputs
user_input = int(input("please enter how many inputs u want: "))
def_list = []  # defining an empty list
for i in range(user_input):  # using for loop creating a range from user input
    # prompting user for input that to add into the list
    user_input1 = input("Enter the number into the list:- ")
    # given input is appended to the empty list which is created previously on line 2
    def_list.append(user_input1)
# printing the values enter by user into list
print("The values in the list are", def_list)
