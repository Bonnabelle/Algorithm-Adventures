def get_length_of_missing_array(array_of_arrays):
    lengths = []
    for i in array_of_arrays:
        lengths.append(len(i))

    for n in range(1,len(lengths)+1):
        if n not in lengths:
            return n

"""
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3
"""
