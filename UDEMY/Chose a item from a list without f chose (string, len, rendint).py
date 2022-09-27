# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# split separate Split the string, using comma, followed by a space, as a separator
import random
#create a variable where we put len funtion to see how items are in variable names (how much names was introduced)
num_items = len(names)
#we create a radom choice with randint (generate radom imnetegrs from a interval) function but last value will be len(names) -1 
#because counting start with 0 in a list
random_name = random.randint(0,num_items-1)
# use another variable person to prin name choise randomly form list names
person = names [random_name]
print (f"{person} will pay the bill.")


