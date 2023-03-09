def reverse_list(l):
    """
    Girilen liste elemanlarını tersine döndürür ve içindeki alt listeleri de tersine döndürür.
    """
    result = []
    for i in l:
        if isinstance(i, list):
            result.append(reverse_list(i))
        else:
            result.append(i)
    return result[::-1]

m = [[1, 2], [3, 4], [5, 6, 7]]

print(reverse_list(m))