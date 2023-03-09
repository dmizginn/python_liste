def flatten_list(l):
    """
    Girilen liste elemanlarını düzleştirir ve tek boyutlu bir liste döndürür.
    """
    result = []
    for i in l:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result

m = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print (flatten_list(m))