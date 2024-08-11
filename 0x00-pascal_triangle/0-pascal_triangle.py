#!/usr/bin/python3
""" function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    """function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    
    for i in range(1, n):
        #let every row starts with 1
        row = [1]
        for j in range(1, i):
            # get each element of the row
            r = triangle[i-1][j-1] + triangle[i-1][j]
        #append r and let the row end with 1
        row.append(r, 1)
        #append the row to the triangle
        triangle.append(row)

    return triangle
    