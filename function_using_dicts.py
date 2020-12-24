def mean(value):
    if type(value) == dict:
        mean = sum(value.values()) / len(value)
    else:
        mean = sum(value) / len(value)

    return mean
test_list = [3,5,6,7,89,99]
test_dict = {'pradeep': 22.6, 'jyo': 22.9}


print(mean(test_dict))

