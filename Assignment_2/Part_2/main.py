#Agilan Ampigaipathar (100553054)
import numpy as np

Arr = [65738,11329,5231,242,7,2432,100021]
numValues = 10

#From Tutorial 5 counting sort
def countingSort(Arr, numValues, digPos):
    A = np.array(Arr, dtype=np.int)
    B = np.zeros_like(Arr, dtype=np.int)

    # initialize the counts
    k = A.max()
    counting_vector = np.zeros([k + 1], dtype=np.int)

    # count the occurrences of each value
    for num in A:
        counting_vector[num] += 1

    # determine the cumulative frequencies
    for i in range(1, k + 1):
        counting_vector[i] = counting_vector[i] + counting_vector[i - 1]

    # order the elements by their frequency
    for num in A[::-1]:
        B[counting_vector[num] - 1] = num
        counting_vector[num] -= 1

    return B

#Function from instruction pdf 
def getDigit(num, digit):
	working = num / 10**(digit-1)
	return working % 10

def radixSort(A,d):
  radixArr = []
  for i in range(0, len(A)):
    radixArr.append(0)
    
  for j in range(1, d+1):
    radixArr = countingSort(A, 10, j)
              
  return radixArr

print "Original Array: \n", Arr
#6 digit numbers 
sortedArr = radixSort(Arr,6)
print "\n"
print "Sorted Array: \n", sortedArr
