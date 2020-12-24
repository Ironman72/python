list_of_lists = [1, 2, 3, [2, 3, 4], [3], [56, 95, [68]], [56]]
for i in list_of_lists:
    print(i)
print(list_of_lists)

list_of_numbers = [i for i in range(0, 11)]
print(list_of_numbers)


list2 = ["this", "is", "virus"]
for i, list in enumerate(list2):
    print("This is ", i, "of the", list)
