def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    dict1 = {}

    for i in range(len(a)):
        dict1[i] = a[i] ;

    #print(dict1)

    result = []
    # start_array = [-1, -2, 1, 2, 3, 4, -4]
    # array = [-1, -2, -4]
    array = []
    for i in range(len(a)):
        if a[i] < 0:
            array.append(a[i])
    #print(f'array is {array}')

    for i in range(len(array)):
        if (array[i] * (-1)) in a:
            result.append((array[i] * (-1)))

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))




            


