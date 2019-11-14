def formula_bine(n):
    """
    the function uses the Binet formula to calculate the nth number of the Fibonacci series
    :param n: non-negative integers
    :return: integer
    """
    f = int((((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)/5**0.5)
    return f

