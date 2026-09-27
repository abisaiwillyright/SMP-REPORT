bench_press_set = 5
reps_per_set = 12
weight_per_rep_kgs = 80
total_reps = bench_press_set * reps_per_set
total_volume_kgs = total_reps * weight_per_rep_kgs
reps_per_minute = total_reps // 4  # assume 4 minutes workout time
print("=== Bench Press Workout Summary ===")
print(f"sets: {bench_press_set}")
print(f"reps per set: {reps_per_set}")
print(f"total reps: {total_reps}")
print(f"weight per rep (kgs): {weight_per_rep_kgs}")
print(f"total volume (kgs): {total_volume_kgs}")
print(f"reps per minute: {reps_per_minute}")

steps = 16000
water_glasses = 8
sleep_hours = 7
fasting = "OMAD"
print(steps >= 10000)  # Did I hit my step goal?
print(water_glasses == 9)  # Did I hit my water goal?
print(sleep_hours < 6)  # Did I hit my sleep goal?
print(fasting != "None") # Am I on a fasting plan?
print(steps > 17000)  # Did I exceed 17000 steps?
