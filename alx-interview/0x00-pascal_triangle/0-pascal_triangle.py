#!/usr/bin/python3

"""
Contains a function that implement pascal triangle
algorithm
"""
def pascal_triangle(n):
    """
    return a list of lists of integers representing the
    Pascal's triangle of n
    """

    initial_arr = [1]
    pascal_arr = []
    pascal_arr.append(initial_arr)
    prev_arr = initial_arr.copy()

    for i in range(n - 1):
        new_arr = []
        new_arr.append(1)
        for j in range(len(prev_arr)):
             if ((j + 1) >= len(prev_arr)):
                break

             first =prev_arr[j]
             second = prev_arr[j + 1]
             new_arr.append(first + second)

        new_arr.append(1)
        prev_arr = new_arr.copy()
        pascal_arr.append(prev_arr)
    
    return pascal_arr

        
