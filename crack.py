from string import digits
from itertools import product
import time

rep = input("Repeat? ")
if rep.isdigit():
    rep = int(rep)
else:
    rep = 8

#get start time
begin = time.time() #The lenght of the password

    
for passcode in product(digits, repeat=rep):
    print(*passcode)


# store end time
end = time.time()

time.sleep(1)

# total time taken (rounded to 3 decimals)
print(f"Time to check all passwords: {round(end - begin, 3)} s")

# total combinations
print(f"Number of all combinations: {len(digits)**rep:,}") #add , separation every tree digits