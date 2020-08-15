

def calculate(x, y, z):
    return 




def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # create dictionary
    weights_dict = {}
    result = []
    # populate dictionary
    for i in range(length):
        
        # populate dictionary
        weights_dict[weights[i]] = i

        value = limit - weights[i]
        if value in weights_dict.keys():

            # add indices to result
            result.append(weights_dict[weights[i]])
            result.append(weights_dict[value])

            # if there are only 2 items in the array
            if result == [0,0]:
                result[0] += 1 

            # print(result)
            return result

    
  
    
       

# # test 1    
# weights_1 = [9]
# get_indices_of_item_weights(weights_1, 1, 9)

# # test 2
# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

# test 3 
# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
# print(answer_3)


# test 4
# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# print(get_indices_of_item_weights(weights_4, 9, 7))



