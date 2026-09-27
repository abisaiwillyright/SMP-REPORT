dairy_log = ['two hundred']
for item in dairy_log:
    try:
        ltrs = int(item)
        print(ltrs)
       
    except ValueError:
        print(f"Invalid entry: {item} is not a number")