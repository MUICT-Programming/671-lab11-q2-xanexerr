# YOUR CODE HERE
def summation(lst1, lst2):
     return [x + y for x, y in zip(lst1, lst2)]

def find_min_max(lst):
     return (min(lst), max(lst))


n = int(input())
lst1 = [int(input()) for underscore in range(n)]
lst2 = [int(input()) for underscore in range(n)]

updated_list = summation(lst1, lst2)
print(updated_list)


print(find_min_max(updated_list))