# introduction-to-algorithms
# pseudo-code for binary search in array:
1. Let min = 0 and max = n - 1.
2. If max < min, then stop: target is not present in array. Return -1.
3. Compute guess as the average of max and min, rounded down (so that it is an integer)
4. If array[guess] equals target, then stop. You found it. Return guess.
5. If the guess was too low, that is, array[guess] < target, then set min = guess + 1
6. Otherwise, the guess was too high. Set max = guess -1.
7. Go back to step 2.

# pseudo-code for selection sort in array:
1. Find the smallest card. Swap it with the first card.
2. Find the second-smallest card. Swap it with the second card.
3. Find the third-smallest card. Swap it with the third card.
4. Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
