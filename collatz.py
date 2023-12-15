import matplotlib.pyplot as plt
import time


# This code calculates, collects and plots the amount of Collatz operations for each integer from 1 to provided number.
def collatz(x, ctr=0):
    if x == 1:
        return ctr
    return collatz(3*x+1, ctr=ctr+1) if x % 2 == 1 else collatz(x/2, ctr=ctr+1)


limit = int(input("Please provide a limit value: "))

# Starting time
st = time.time()

# Plotting operations
plt.plot([i for i in range(1, limit+1)], [collatz(i) for i in range(1, limit+1)], ",")
plt.xlabel("Number")
plt.ylabel("Iterations to 1")

# Ending time. 
et = time.time()

print(f"Whole thing takes {et - st} seconds.")
plt.show()
