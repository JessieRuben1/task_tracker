
def duplicate_values(lst):
    '''
    Returns True if there are duplicate values in a list and False
    if there are no duplicate values
    '''
    # Sort the list first
    sorted_lst = sorted(lst)
    # Check adjacent elements for duplicates
    for i in range(len(sorted_lst)-1):
        if sorted_lst[i] == sorted_lst[i+1]:
            return True
    return False


        
print(duplicate_values([0, 1, 3, 5, 2, 5]))