# 1 FINDING KEY--VALUE IN DICTIONARY

dictionary={"name":"Nagaraj Loni","age":"21","mobile_Number":881145485,"college name":"BiTM Ballari","sem":4 ,"nnnnnnnn":977}

if "name" in dictionary:
    print(dictionary["name"])
else:
    print("Key is not found")


# 2 Sort Python Dictionaries by Key or Value

dictionary={"name":"Nagaraj Loni","age":"21","mobile_Number":881145485,"college name":"BiTM Ballari","sem":4}

sorted_dictionary = sorted(dictionary.items())
print(sorted_dictionary)


# length of dictionary
print("Size of the dictionary is : "+str(dict.__sizeof__(dictionary)))

print("Size of the dictionary is : "+str(dict.__len__(dictionary)))