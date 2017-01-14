import sys
a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
ls = [a,b,c,d,e]
ls.sort()
mins = sum(ls[0:4])
maxs = sum(ls[1:5])
print(mins,maxs)

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""
