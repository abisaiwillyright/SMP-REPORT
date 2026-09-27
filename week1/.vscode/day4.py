import math

steps = 7500
sleep_hours = 6
water_glasses = 5
cold_showers = False
pages_read = 15

excelent_steps = steps >= 10000
good_steps = steps >= 7500  # need to work otherwise

good_sleep = sleep_hours >= 7
low_sleep = sleep_hours < 5

good_water = water_glasses >= 8
low_water = water_glasses < 4

completed_cold_shower = cold_showers == True
skipped_cold_shower = cold_showers == False

good_reading = pages_read >= 10
low_reading = pages_read < 14

print(f"Steps: {steps}")
print(f"Sleep: {sleep_hours}")
print(f"Water: {water_glasses}")
print(f"Cold Shower: {cold_showers}")
print(f"Pages Read: {pages_read}")