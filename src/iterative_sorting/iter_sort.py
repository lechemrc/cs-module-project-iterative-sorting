
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
            prevprev = prev
            prev = cur

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