def dot_product (a,b):
    if len(a) != len(b):
        raise ValueError("a and b must have the same length")
    else:
        result = 0
        for i in range(len(a)):
            result += a[i] * b[i]
        return result



print(dot_product([1, 2, 3], [4, 5, 6]))  # Expected output: 32