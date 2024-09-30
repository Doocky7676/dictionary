# dictionary = a collection of {key:value} pairs ordered and changable. No duplicates.

capitals = {"USA" : "Washington D.C.", "India" : "New Delhi", "China" : "Beijing", "Russia" : "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))

# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")


# # how to update list
# capitals.update({"Germany": "Berlin"})

# print(capitals)

# capitals.update({"Mexico": "Mexico City", "Italy": "Rome", "France": "Paris"})

# print(capitals)

# # remove from list
# capitals.pop("China")

# # remove last thing in dictionary
# capitals.popitem()

# # clear dictionary
# capitals.clear()

# # to get only keys
# keys = capitals.keys()

# print(keys)

# # to get only values
# values = capitals.values()

# print(values)

# # for loop

# for key in capitals.keys():
#     print(key)

# for value in capitals.values():
#     print(value)

# items method

# items = capitals.item()
for key, value in capitals.items():
    print(f"{key}: {value}")
 