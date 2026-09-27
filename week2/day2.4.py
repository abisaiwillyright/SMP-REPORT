#Index() - retuns the position of the first matching value. use it to know the item is on the list and whant to know its position.

habits = ["8 glasses water", "cold shower", "OMD fast", "workout"]
position = habits.index("OMD fast")
print("OMD fast is at position:", position)



#Count() - counts how many time a specific item appears on the list.
daily_results = ['hit', 'miss', 'hit', 'miss', 'miss', 'hit', 'hit']
hit_count = daily_results.count('hit')
miss_count = daily_results.count('miss')
print('Daily target hit:', hit_count)
print('Daily target miss:', miss_count)