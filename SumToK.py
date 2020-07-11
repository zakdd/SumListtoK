#Given a list of numbers and a number k, return whether any two numbers from the list add up to k


sample_set = set()

arr = [10, 15, 3, 7]

sample_set.update(arr)

k = 17 

for i in arr:
    if k-i in sample_set:
        print(i)

