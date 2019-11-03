# Pseudo-code:

# s1. Let min = 0 and max = n - 1.
# s2. If max < min, then stop: target is not present in array. Return -1
# s3. Compute guess as the average of max and min, rounded down (so thay it is an integer)
# s4. If array[guess] equals target, then stop. You found it! Return guess.
# s5. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
# s6. Otherwise, the guess was too high. Set max = guess - 1
# s7. Go back to step 2.

def binSearch(arr, target):
    min = 0
    max = len(arr) + 1
    while (min <= max):
        guess = int(round((max + min)/2))
        if (arr[guess] == target):
            return guess
        elif (arr[guess] < target):
            min = guess + 1
        else:
            max = guess -1
    return -1