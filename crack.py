from string import digits
from itertools import product
import time

#get start time
begin = time.time()

for passcode in product(digits, repeat=8):
    print(*passcode)

 
time.sleep(1)
# store end time
end = time.time()
  
# total time taken
print(f"Time to check all passwords: {end - begin}")