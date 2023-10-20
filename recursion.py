"""
Recursion is a way of solving a problem by having a function calling itself. It's a method of solving a problem where the solution depends on the solution to the smaller instance of the same problem. Such problems caan generally be solveed by iteration as well. 

PROPERTIES OF RECURSION
1. performing the same operation multiple times with different inputs
2. in every step we try smaller inputs to make the problem smaller
3. Base condition is needed to stop the recursion, otherwise infinite loop will occur


WHY RECURSION

1. Recursive thinking is really importatnt in programming  and it helps you break down big problems into smaller ones easier to use.
 - WHEN DO YOU CHOOSE RECURSION
    when you hear such a problem begining with the following statement:
    1. if you can divide the problem into similar sub problem
    2. design an algorithm to compute nth...
    3. write code to list the n...
    4. implement a method to compute  all..

2. The prominent usage of recussion in data structure like trees and graphs.
3. interviews
4. It is used in many algorithm for instance divide and coinqure, greedy and dynamic algorythm


HOW RECURSION WORK
    
"""


"""
fibonacci = 0,1,1,2,3,5,8,13
"""

n = 3


# def recursive_fibernacci(n):
#     if n <= 1:
#         return n
#     else:
#         return recursive_fibernacci(n-1) + recursive_fibernacci(n-2)


# result =  recursive_fibernacci(5)
# print(result)


# def openCircusDull(dull):
#     if dull == 1:
#         print('All dolls are opened')
#     else:
#         openCircusDull(dull - 1)


# openCircusDull(5)


def factorial(n):
    if n <= 1:
        return n
    else:
        return factorial(n-1)
    
print(factorial(5))