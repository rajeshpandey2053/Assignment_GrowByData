elements = [1, 2, 3, 4, 5]
# Delcare and defining an array
# Using map() and sum() inbuilt function to find sum of each integer array and store in a list.

tot = 0


def sum_func(a):
    global tot
    tot = tot + a
    return tot


total_sum = list(map(sum_func, elements))
print(total_sum[-1])  # print the sum of list
