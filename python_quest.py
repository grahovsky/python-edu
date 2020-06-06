import time
from functools import reduce

def quest2():

    def fast_function(n):
        a = list(i for i in range(n))
        n in a


    def very_fast_function(n):
        b = [i for i in range(n)]
        n in b


    def super_very_fast_function(n):
        c = set(i for i in range(n))
        n in c


    def the_fastest_function_ever(n):
        d = {i for i in range(n)}
        n in d

    funcs_for_estimate = [
        #fast_function,
        very_fast_function,
        #super_very_fast_function,
        the_fastest_function_ever
    ]

    def stupid_search_test(n):
        for func in funcs_for_estimate:
            t = time.time()
            func(n)
            print(func.__name__, ':', time.time()-t)

    n = 100000000
    stupid_search_test(n)

# quest2()

def quest5():
    
    pan_settings = [
        [15, 10, 9], 
        [10, 12, 17],
        [11, 14, 15],
        [17, 13, 13],
        [14, 9, 11],
        [14, 15, 9],
        [9, 17, 14],
        [10, 12, 13]
        ]

    findSettings = pan_settings[[reduce(lambda x, y: x * y, i) for i in pan_settings].index(2310)]
    print(findSettings)

quest5()

