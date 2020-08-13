
# -------------------------------------
# Lecture Notes:

nums = [2, 6, 8, 3, 4, 1, 9, 6, 7]
def insert_sort(nums):
    # Loop through sums
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        # While we're not at the beginning. AND
        while j > 0 and temp < nums[j - 1]:
            # swap
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp
    return nums

print(nums)
sorted_nums = insert_sort(nums[:])
print(nums)
print(sorted_nums)


def countdown(n):
    print(n)
    if n == 0:
        print('*BOOM*')
        return
    # Recursive case
    else:
        countdown(n-1)

# countdown(10)

def rec_fib(n):
    # Base case
    if n == 1 or n == 2:
        return 1
    
    # Recursive case -- add two previous terms 
    else:
        return rec_fib(n-1) + rec_fib(n-2)


def iter_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        prevprev = 1
        prev = 1
        for i in range(1, n-1):
            cur = prevprev + prev
            prevprev, prev = prev, cur

    return cur


print('-------------------')

print(rec_fib(1))
print(rec_fib(2))
print(rec_fib(3))
print(rec_fib(4))

print('-------------------')
print(iter_fib(1))
print(iter_fib(2))
print(iter_fib(3))
print(iter_fib(4))
print(iter_fib(5))
print(iter_fib(6))
print(iter_fib(7))
print(iter_fib(8))
print(iter_fib(9))
print(iter_fib(10))


# Ex. 1
# Given the radius of a circle, calculate it's area and and format
# the result to three decimal places
def area_circle(radius):

    pass
print(area_circle(3))   # 28.274


# Ex. 2
# We'll say that a positive int divides itself if every digit in the 
# number divides into the number evenly. So for example 128 divides 
# itself since 1, 2, and 8 all divide into 128 evenly. 
# And we'll say that 0 does not divide into anything evenly, so no 
# number with a 0 digit divides itself. 
# Write a function to determine if a number divides itself.
# [source - https://codingbat.com/prob/p165941]


def divides_self(num):
    # Return boolean
    # Skip error handling
    # num % 10 to get the digit on right
    # if result is 0, return false
    pass


print(divides_self(128)) # → True
print(divides_self(12)) # → True
print(divides_self(120)) # → False


# Ex. 3
# The Knapsack Problem
# https://en.wikipedia.org/wiki/Knapsack_problem

def naive_knapsack(weight_limit, items):
    items.sort(key=lambda x: x.value, reverse=True)
    # could be better if we sorted by value/weight ratio

    sack = []
    cur_weight = 0
    i = 0

    # While there is room in the sack
    while cur_weight < weight_limit:
        # Put the next most valuable item in it IF there is room
        if cur_weight + items[i].weight <= weight_limit:
            sack.append(items[i])

    return sack