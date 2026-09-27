#arrange in order low to high
step_counts = [8800, 6500, 11000, 9200, 7300]
step_counts.sort()
print('Sorted from low to high:', step_counts)


#add 10500 to the end 
step_counts.insert(5, 10500)
print('After:', step_counts)

#remove 6500
step_counts.remove(6500)
print('Removed', step_counts)

#arrange in order high to low
step_counts.sort(reverse=True)
print('Reversed:', step_counts)

print('Final list:', step_counts)

#count days over 9000
hight_days = 0
for s in step_counts:
    if s >= 9000:
        hight_days +=1
print('Days oves 9000 steps:', hight_days)
