#Sort() - arranges list in ascending order (lowest to highest for numbers, A to Z for text). changes the list directly.


weekly_steps = [9200, 8800, 10500, 11000, 7600, 9400, 10200]
print("Unsorted:", weekly_steps)

weekly_steps.sort()
print("sorted low to high:", weekly_steps)


#sort high to low by passing reverse=True

weekly_steps.sort(reverse=True)
print("sorted high to low:", weekly_steps)



#Reverse() - flips the order of the list without sorting it. It just turns the list backwards.

skills = ["welding", "tilling", "upholstery", "phone repair"]
print("Unreversed:", skills)
skills.reverse()
print("Reversed:", skills)