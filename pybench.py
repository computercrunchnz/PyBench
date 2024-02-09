import time
import math
import random

runs = 1

runsa = 0

runb = time.time() + 60 * int(runs)

while time.time() < runb:
    calct = random.randint(0,5)
    calc1 = random.randint(0,999999999)
    calc2 = random.randint(0,999999999)
    if calct == 0:
        a = calc1 + calc2
        b = calc1 - calc2
    elif calct == 1:
        a = calc1 * calc2
        b = calc1 / calc2
    elif calct == 2:
        a = math.e
        b = math.e
    elif calct == 3:
        a = math.pi
        b = math.pi
    elif calct == 4:
        a = math.cos(calc1)
        b = math.cos(calc2)
    elif calct == 5:
        a = math.sin(calc1)
        b = math.sin(calc2)
    elif calct == 6:
        a = math.tan(calc1)
        b = math.tan(calc2)
    elif calct == 7:
        a = math.factorial(calc1)
        b = math.factorial(calc2)
    runsa = runsa + 1
    
runs = runsa

print("Done!")
print("Score: " + str(runsa))
