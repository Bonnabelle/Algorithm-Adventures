import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)] #The range of Sam's house
a,b = input().strip().split(' ')
a,b = [int(a),int(b)] #The points of the trees - a for apple, b for orange
m,n = input().strip().split(' ')
m,n = [int(m),int(n)] #The number of fallen fruit - m for apples, n for oranges.
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')] #Distance from point a that the apples fell
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')] #Distance from point b that the oranges fell
#Determine how many apples and then oranges fell on Sam's house.

apples = 0
for ap in apple:
    if t >= a + ap and a + ap >= s:
        apples += 1

oranges = 0
for o in orange:
    if t >= o + b and o + b >= s:
        oranges += 1

print(str(apples) + "\n" + str(oranges))



"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
You can assume the trees are located on a single point, where the apple tree is at point a and the orange tree is at point b.

When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. A negative value of  means the fruit fell
units to the tree's left, and a positive value of d means it falls d units to the tree's right.

Given the value of  for  apples and  oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])
Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your
second line of output.

Input Format:

The first line contains two space-separated integers denoting the respective values of s and t.
The second line contains two space-separated integers denoting the respective values of a and b.
The third line contains two space-separated integers denoting the respective values of m and n.
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

Output Format

Print two lines of output:

On the first line, print the number of apples that fall on Sam's house.
On the second line, print the number of oranges that fall on Sam's house.
"""
