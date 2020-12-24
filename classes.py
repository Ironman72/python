# creating a class
# This is a ""//Parent Class\\""

class Parent:  # declaring a class using class constructor with name of parent
    # using __init__ we are initiliazing the values, self pakka undali
    def __init__(self, name, age, gender):
        self.name = name  # self vale tho manaku kavalsina values ni declare chesthunam
        self.age = age
        self.gender = gender
        print("All the data saved")  # sample print to check no errorrs


# creating and using object

# creating virus object and assign to class, giving the required paramaters
virus = Parent('jimmy', 39, 'male')
# print(virus.name)  # printing virus,name
# print(virus.age)  # printing virus age
# print(virus.gender)  # printing virus gender

# This is a ""//child Class\\""


class Jyothsna(Parent):  # creating a normal class when we use Parent name in barckets that becomes child class,
    # giving all the values to get from parent class
    def __init__(self, name, age, gender, year):
        # here we get all the data from parent class using super(),__init__(we pass the values what we want)
        super().__init__(name, age, gender)
        self.year = year  # creating new variable inside the child class,
        print("this is jyo ")  # sample text


# J is the object to access child class Jyothsna
j = Jyothsna('kanna', 22, 'deyyam', 2020)
print(j.name, virus.name, "are wife and Husband",
      'and they are ', j.age, 'greater')  # using print we are printing the data we want from child/parent class
