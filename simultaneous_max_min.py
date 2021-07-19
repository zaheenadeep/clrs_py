def find_extrema(arr):
    it = iter(arr)

    if len(arr) % 2 == 0:
        num1 = next(it)
        num2 = next(it)

        if num1 < num2:
            min = num1
            max = num2
        else:
            min = num2
            max = num1
    else:
        max = min = next(it)


    for num1 in it:
        num2 = next(it)

        if num1 < num2:
            temp_min = num1
            temp_max = num2
        else:
            temp_min = num2
            temp_max = num1

        if temp_min < min:
            min = temp_min

        if temp_max > max:
            max = temp_max

    return max, min


print(find_extrema([3,8,4,456,8765,234,23,-34]))