def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    if not lst:
        raise ValueError("Empty list!")
    max_ = lst[0]
    for element in lst[1:]:
        if element > max_:
            max_ = element
    return max_        


list1 = [-23,-1,5,7]
print(find_max_element(list1))

#############################################################
#Given a list of integers, write a function to find the sum of all the elements in the list.
## Normal way
def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    sum_ = 0
    for element in lst:
        sum_ += element
    return sum_

my_list = [1,2,3,3,2,1]
print(sum_of_elements(my_list))

### I think this i my mid i feel that in that way also possible does i make different thing

# just fun another way to find largest 
def sum_list(lst):
    ## first i will sort this list
    size = len(lst)
    for passes in range(size - 1):
        for j in range(0, (size -1) - passes):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    max_element = lst[-1]
    return max_element
list2 = [1,2,4,35,3345,234324,23443,5,63,434]
print(sum_list(list2))
#####################
#🔁 Palindrome Check Using Two Pointers
def is_palindrome(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1
    return True
my_list = [1,2,4,5,6]
print(is_palindrome(my_list))
print(is_palindrome([1,2,3,2,1]))

