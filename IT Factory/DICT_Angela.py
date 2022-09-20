# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
# # print date din dictionar
# print(programming_dictionary["Bug"])

# #Addin new item
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# # empty_dictionary
# empty_dictionary = {}

# #wipe an existing dictionary
# # programming_dictionary = {} # golim dictioanrul

# # edit an item on dic
# programming_dictionary["Bug"] = "A moth in my computer" #assigned a new value
# print(programming_dictionary)

# # loop through a dic
# # for thing in programming_dictionary:
# #     print(thing) # print keys of dic

# # for print values of keys too
# for key in programming_dictionary:
#     # print(key + " " + programming_dictionary[key])
#
#
# #Nesting Dict
# # putem pune ca valoare a unei key o lista sau chiar un dict
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hambursg", "Stuttgart"],
# }
# # this is a dic with value type of list
# #Nest Dict in DIct
# travel_log = {
#     "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits":12},
#     "Germany": {"cities_visited": ["Berlin", "Hambursg", "Stuttgart"], "total_visits":5},
# }
# print(travel_log)
#
# #Nesting a Dic in  a list
# travel_log = [
#     {"country": "France",
#      "cities_visited":["Paris", "Lille", "Dijon"],
#      "total_visits":12
#     }, # mai usor de vazut asezat in acest mod o lista cu 2 dict fiecare dict cu 3 keys
#     {"country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "total_visits":5
#     },
# ]
# print(travel_log)
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
#
# from replit import clear
# TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     travel_log.append({"country": country, "visits": visits, "cities": cities})
# #create a function who can add an dict into a list
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# print(travel_log[2])

from replit import clear
# HINT: You can call clear() to clear the output in the console.

print("Welcome to the secret auction program")
biders_dict = {}

def blind_auction():
  name_input = input("What is your name?\n")
  bid_value = input("what is your bid?\n$")
  biders_dict[name_input] = bid_value
  print(biders_dict)
  clear()

blind_auction()
other_biders = input('Are there any other biders? Type "yes" or "no"]\n')
while other_biders == "yes":
  blind_auction()
  other_biders = input('Are there any other biders? Type "yes" or "no"]\n')
# for biders in biders_dict:
#     list_biders = [biders]
#     print(list_biders)