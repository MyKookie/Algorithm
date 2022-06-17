def shellSort(array): 

    n = len(array) 

    gap = n // 2 # initialize the interval 

 

# Perform sorting to all sub-array with interval of gap 

    while gap > 0: 

        for i in range(gap, n): 

            temp = array[i] 

            j = i 

# Check for right element with gap index away 

# When gap = 1 it behaves like insertion sort 

            while j >= gap and array[j - gap] > temp: 

                array[j] = array[j - gap] 

                j -= gap 

 

            array[j] = temp 
        gap //= 2 # gap is reduced after each iteration 

 

A = [16, 30, 95, 51, 84, 23, 62, 44] 

print(A) 

 

shellSort(A) 

print(A) 