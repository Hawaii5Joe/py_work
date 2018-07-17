
#User input validation
def get_starting_num():
    x = int(input('Please enter a starting number: '))
    while x < 1:
        x = int(input('Please input a number greater than or equal to 1: '))
    return x

def get_ending_num(starting_num):
    y = int(input('Please enter an ending number: '))
    while y < starting_num * 5:
        y = int(input('Please input a number 5x greater than the starting number: '))
    return y

starting_num = get_starting_num()
ending_num = get_ending_num(starting_num)


#Calculation section
#full number range
user_generated_range = list(range(starting_num, ending_num + 1,))
print('Heres the full range', user_generated_range)

#even value and index print out
for index, num in enumerate(user_generated_range):
    if num % 2 == 0:
        print('Heres the index of the even number ', index, 'and heres the value ', num)

#odd value sum
def odd_value_sum(user_generated_range):
    odd_sum = 0
    for num in user_generated_range:
        if num % 2 == 1:
            odd_sum += num
    print('The total of the odd values is', odd_sum)

odd_value_sum(user_generated_range)
