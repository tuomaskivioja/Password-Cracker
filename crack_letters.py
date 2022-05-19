from string import ascii_letters
from itertools import product
import time

rep = input("Repeat? ") #The lenght of the password
if rep.isdigit():
    rep = int(rep)
else:
    rep = 8

#get start time
begin = time.time()

for passcode in product(ascii_letters, repeat=rep):
    print(*passcode)

# store end time
end = time.time()

time.sleep(1)

# total time taken (rounded to 3 decimals)
print(f"Time to check all passwords: {round(end - begin,3)} s")

# total combinations
print(f"Number of all combinations: {len(ascii_letters)**rep:,}")#add , separation every tree digits