#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    Returns pascal's triangle of n(integers)

    Args:
        n: number of rows in pascal's triangle
    """
    if (n <= 0):
        return []

    p_triangle = []

    for r in range(n):
        row = [1] * (r + 1)
        if (r > 1):
            r_row = p_triangle[-1]
            t = 1
            while (t < r):
                row[t] = r_row[t - 1] + r_row[t]
                t += 1
        p_triangle.append(row)
    return p_triangle
