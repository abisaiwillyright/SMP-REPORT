# Multiple default parameters

def log_day(steps, water = 8, protocal = 'OMAD'):
    print(f'steps: {steps} | water: {water} galsses | protocal: {protocal}')

log_day(9200)
# Uses both defaults.
log_day(10500, water = 9)

# Override water only.
log_day(8800, water = 7, protocal='2MAD')  #Override both
