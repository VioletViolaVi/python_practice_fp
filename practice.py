# print("Hello world!")

# age = 28
# print(type(age))
# print(type(float(age)))

# sentences = "I'm learning python for the very first time this morning!\nWe're having a great time."
# sentences2 = 'I\'m learning python for the very first time this morning!\nWe\'re having a great time.'
# print(sentences.lower())
# print(sentences2.upper())

# listSentence = ["I'm learning python for the very first time this morning!",
#                 "We're having a great time."]
# print(listSentence)

# numbersList = [1, 2, 3]
# # print(numbersList[0])

# numbersList[2] = 100
# print(numbersList)


# tuplePractice = ("2", "4", "6", "6")
# # print(tuplePractice)
# # print(tuplePractice[3])
# print(tuplePractice[len(tuplePractice)-1])

# if "hello" in tuplePractice:
#     print("tuple has hello")
# else:
#     print("does not have tuple")

from itertools import count


my_dictionary = {
    "name": "Bobby",
    "age": 23,
    "python_skill": 1,
    "had_coffee": False
}

# print(my_dictionary)

# print(my_dictionary["name"])

# my_dictionary["python_skill"] = 2
# print(my_dictionary)
# my_dictionary["programming_languages"] = ("java", "javascript", "html", "css", "jquery", "c#")
# print(my_dictionary)

food_set = {"eggs", "cake", "pasta", "chips", "pie", "ice-cream"}
print(food_set)
print(len(food_set))
