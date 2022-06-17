def countingSort(array):
   # Initialise sorted array
   arrLen = len(array)
   sortedArr = [0] * arrLen
   # Initialise count array
   countLen = max(array) + 1
   count = [0] * countLen

   # Store the count of occurrences in the count array
   for i in range(0, arrLen):
       count[array[i]] += 1

   # Store the cumulative count
   for i in range(1, countLen):
       count[i] += count[i - 1]

   # Find the index of each element of the original array in count array
   # Store the sorted array
   i = arrLen - 1
   while i >= 0:
       sortedArr[count[array[i]] - 1] = array[i]
       count[array[i]] -= 1
       i -= 1

   # Copy the sorted elements back to the original array
   for i in range(0, arrLen):
       array[i] = sortedArr[i]

A = [16, 30, 95, 51, 84, 23, 62, 44]
print("Original Array: " + str(A))
countingSort(A)
print("Sorted Array in Ascending Order: " + str(A))