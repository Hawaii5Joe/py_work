# returns biggest_value x array and corresponding position
def value_position (x):
    # initializing biggestValue, and position to 0 to start comparison
    biggestValue = x[0]
    position = 0
    # comparing value of ith position to biggestValue variable, if true biggestValue is replaced with the value in the
    #ith position.
    for i in range(len(x)):
        if x[i] > biggestValue:
            biggestValue = x[i]
            position = i
    # returning largest value and position in x
    return biggestValue, position

# swap takes in x array, position, and position 2 so that the values at each of those positions can be swapped
def swap (x, position, position2):
    # need a t variable to store the value that is being written over
    t = x[position]
    # setting position equal to position 2
    x[position] = x[position2]
    # setting x position2 to t
    x[position2] = t



# takes in an array x, and sorts it ascending
def listSort (x):
    # for loop below counts the number of swaps needed to sort array x
    for i in range(len(x) - 1):
        # for a single swap you get out biggestValue, and position from the calling of value_position, the whole array will be
        # iterated over to pull out the biggestValue, position
        biggestValue, position = (value_position(x[0:len(x) - i]))
        # print(biggestValue)
        # print(position)

        # swap is passed an array of x, position  placeholder variable, and length of 
        swap(x, position, len(x) - i - 1)
        # print(x)


x = [0, 2, 4000, 59680, -100]

print(x)
listSort(x)
print(x)