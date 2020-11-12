import math

def missing_number_single(arr):
    # If there's only one entry the solution is obvious
    if len(arr) == 1:
        return arr[0]

    # Get the middle index
    middle = math.floor(len(arr)/2)
    
    # Originally this line used arr.count, but I figure that function might be O(n) and that's too high for me
    # So I replaced it with manually checking the element below and above
    # We know both of those elements exist since we never get an array with an even element count, and we already checked if there's only 1 element
    # If the middle number matches neither the one above or below it we know that that's the issue
    if arr[middle] != arr[middle-1] and arr[middle] != arr[middle+1]:
        return arr[middle]
    
    # Originally this line used arr.index, but I figure that function might be O(n) and that's too high for me
    # So I replaced it with manually checking if this index or the element below it is the first occurence
    # Since this is single-paired we know there's max 2 elements of the same number
    if arr[middle] == arr[middle-1]:
        index = middle-1
    else:
        index = middle
    
    # If the index is even, we know every integer before this one is paired
    if index % 2 == 0:
        return missing_number_single(arr[index+2:])
    # If the index is odd, we know the problem arose previously
    else:
        return missing_number_single(arr[:index])

def test_q1():
    if missing_number_single([1]) != 1:
        return False
    
    if missing_number_single([1, 1, 2]) != 2:
        return False
    
    if missing_number_single([1, 1, 2, 2, 3]) != 3:
        return False
    
    if missing_number_single([1, 1, 6, 7, 9, 9, 230, 230, 240, 24053, 24053]) != 240:
        return False
    
    return True

print(test_q1())


# This is essentially going to be missing_number_single() except we modify it to account for various assumptions
# regarding the indices and counts of certain numbers not being accurate anymore
def missing_number_paired(arr):
    # If there's only one entry the solution is obvious
    if len(arr) == 1:
        return arr[0]

    # Get the middle index
    middle = math.floor(len(arr)/2)
    
    # Originally this line used arr.count, but I figure that function might be O(n) and that's too high for me
    # So I replaced it with manually checking the element below and above
    # We know both of those elements exist since we never get an array with an even element count, and we already checked if there's only 1 element
    # If the middle number matches neither the one above or below it we know that that's the issue
    if arr[middle] != arr[middle-1] and arr[middle] != arr[middle+1]:
        return arr[middle]
    
    # Originally this line used arr.index, but I figure that function might be O(n) and that's too high for me
    # So I replaced it with manually checking if this index or the element below it is the first occurence
    # Since this isn't single paired we have to loop through every number before the middle to find the first occurence of the middle number
    index = middle
    while index > 0 and arr[index] == arr[index-1]:
        index = index - 1
    
    # If the index is even, we know every integer before this one is paired
    if index % 2 == 0:
        return missing_number_single(arr[index+2:])
    # If the index is odd, we know the problem arose previously
    else:
        return missing_number_single(arr[:index])

def test_q2():
    if missing_number_paired([1]) != 1:
        return False
    
    if missing_number_paired([1, 1, 2]) != 2:
        return False
    
    if missing_number_paired([1, 1, 2, 2, 3]) != 3:
        return False
    
    if missing_number_paired([1, 1, 6, 7, 9, 9, 230, 230, 240, 24053, 24053]) != 240:
        return False
    
    if missing_number_paired([1, 1, 1]) != 1:
        return False
    
    if missing_number_paired([1, 1, 2, 2, 2, 3, 3, 3, 3]) != 2:
        return False
    
    if missing_number_paired([1, 1, 3, 240, 240, 240, 240]) != 3:
        return False
    
    if missing_number_paired([1, 1, 3, 3, 3, 3, 3, 2, 2]) != 3:
        return False
    
    if missing_number_paired([1, 1, 1, 1, 1, 1, 1, 5, 5]) != 1:
        return False
    
    return True

print(test_q2())