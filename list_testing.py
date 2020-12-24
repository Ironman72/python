cars = ["lambo", "benz", "rover", "bentley", "bmw ", "audi"]
bikes = ["zx10r", "bmw s 1000rr", "fireblade"]
cars2 = ["hundai", "suzuki", "tata", "honda", "lamborghini", "buggati"]
bikes2 = ["dugati panigale", "cbr 1000r", "ktm", "yamaha"]

# cars.append("test")
# cars.append("rest")
# cars.remove("test")

favs = cars + bikes
# favs.sort()
print(favs)

# print first 3 items in list
# for b in bikes:
#     if b == "zx10r":
#         print(f"{b} is  the favourite bike for me ", )
for f in favs:
    print(f)
    if f == "zx10r":
        print("thats the fav bike of me", f)
        break
favs.reverse()  # Reverses all the values in the favs list
print(favs)


# appends the electric bike to the end of the list
favs.append("electric bike")
print(favs)

# counter = 0   #counter value starts at 0
# for fav in favs:
#     print(f"{fav} counted {counter}")
#     counter += 1

# print(len(favs))


# using enumerate we can trace the index vale along with looping vale
for counter, fav in enumerate(favs):
    # in 38th line delcared 2 vales 1 is for index tracing 2nd is for looping.
    print(counter, "this is the value for the ", fav)
    # the 39th line we have to print the both index counter and loop counter to trace both vales
