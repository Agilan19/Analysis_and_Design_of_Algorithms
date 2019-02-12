#Agilan Ampigaipathar (100553054)

def knapsack(weights, values):
    cap = int(input("Enter capacity: "))
    n = len(weights)

    unitValues = []
    #Get unit value based on weight and values
    for i in range(0, n):
        unitValue = values[i]/weights[i]
        unitValues.append(unitValue)

    final = []
    #Initialize list 
    for i in range(0, n):
        final.append(0)


    while cap > 0:
        i = maxIndex(unitValues)
        if cap > weights[i]:
            #Everything into knapsack
            cap = cap - weights[i]
            final[i] = 1.0
        else:
            #Fill knapsack with the next best
            final[i] = cap / weights[i]
            #Empty cap
            cap = 0
        unitValues[i] = -1 

    return final

#Get max index of knapsack
def maxIndex(list):
    max = -1
    index = -1
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    return index

w = [1.0, 2.0, 3.0, 3.5, 34.5, 12.0, 33.0, 21.0]
val  = [4, 5, 7, 2, 1, 6, 7, 26]

result = knapsack(w, val)
print result
