def cutRod(price, n):
    if(n <= 0):
        return 0
    max_val = -sys.maxsize-1

    # Recursively cut the rod in different pieces
    # and compare different configurations
    for k in range(0, n):
        max_val = max(max_val, price[k] +
                      cutRod(price, n - k - 1))
    return max_val
