#Remove() - deletes the first item in the list that matches the value that you give it.

habits = ["8 glasses water," "cold shower", "OMD fasting", "cold shower",]
print("Before:", habits)

habits.remove("cold shower")  #Remove only the first one
print("After:", habits)


#Pop() - removes an item by its index position and gives you back the item it removed. With no index, it removes the last item.

weekly_steps = [9200, 10500, 8800, 11000, 7600]
print("Before:", weekly_steps)

removed = weekly_steps.pop()  #remove the last item.
print("Remove", removed)
print("After:", weekly_steps)