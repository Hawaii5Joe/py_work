# swap takes in x array, position, and position 2 so that the values at each of those positions can be swapped
def swap (x, position, position2):
    # need a t variable to store the value that is being written over
    t = x[position]
    # setting position equal to position 2
    x[position] = x[position2]
    # setting x position2 to t
    x[position2] = t

# bubble_sort takes in an array x
def bubble_sort (x):
    # outer for loop executes inner for loop length of x - 1 times
    for i in range(len(x)-1):
        # inner for loop cycles through x comparing each element
        for ii in range(len(x)-1):
            # if statement compares value of x[ii] value of x[ii+1] to see if x[ii] is greater, if it is execute swap
            if x[ii] > x[ii+1]:
                # ii is confirmed greater than x[ii+1], call swap function and swap values at ii and ii+1
                swap(x, ii, ii+1)


x = [1,7,0,59,2,39028,-1]
print(x)
bubble_sort(x)
print(x)
bubble_sort(x)
print(x)
bubble_sort(x)
print(x)
