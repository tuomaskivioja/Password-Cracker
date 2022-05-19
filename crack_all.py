from string import ascii_letters, digits
from itertools import product
import time

letters_digits = ascii_letters+digits #this password can have letters and digits

rep = input("Repeat? ") #The lenght of the password
if rep.isdigit():
    rep = int(rep)
else:
    rep = 8

#get start time
begin = time.time()

for passcode in product(letters_digits, repeat=rep):
    print(*passcode)

# store end time
end = time.time()

time.sleep(1)

# total time taken (rounded to 3 decimals)
print(f"Time to check all passwords: {round(end - begin,3)} s")

# total combinations
print(f"Number of all combinations: {len(letters_digits)**rep:,}") #add , separation every tree digits