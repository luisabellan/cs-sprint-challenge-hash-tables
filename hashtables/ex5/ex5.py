# Your code here

# create dictionary which will hold all the files paths from input
finder_cache = {}

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here


    for file in files:
        my_file = file
        ending = my_file.split('/')[-1]
        query = ending
        finder_cache[query] = []
       
    
    for file in files:
        my_file = file
        ending = my_file.split('/')[-1]
        query = ending
        finder_cache[query].append(my_file)
    
    # print(finder_cache)
    
    # create curated dictionary which will hold only the files paths that match the queries from input
    a = {}

    for i in range(len(queries)):
        
      
        # populate dictionary a
        if queries[i] in finder_cache:
            a[queries[i]] = finder_cache[queries[i]]
    
    # print(a)
    
    # create array which will hold and array of arrays of files paths, I'll have to turn this into an array 
    b = []
    for i in a.values():
        b.append(i)
    
    # print(b)

    # create and array, append the paths to it and return it as the result
    result = []
    for array in b:
        for i in array:
            result.append(i)

    return result 
    





if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/bin/waka/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "bar"
    ]
    print(finder(files, queries))



