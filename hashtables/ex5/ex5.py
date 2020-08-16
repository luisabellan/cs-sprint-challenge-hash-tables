# Your code here


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
    


    a = {}

    for i in range(len(queries)):
        
      
        # populate dictionary a
        if queries[i] in finder_cache:
            a[queries[i]] = finder_cache[queries[i]]
    
    # print(a)
    b = []
    for i in a.values():
        b.append(i)
    result = []
    for array in b:
        for i in array:
            result.append(i)

    return result 
    





if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "bar"
    ]
    print(finder(files, queries))



