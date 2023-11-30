from numpy import mean , sqrt
def STD(list_of_numbers)->float:
    '''Calculating standard deviation\nreturn -> float'''
    c = 0
    for number in list_of_numbers:
        val = (number-mean(list_of_numbers))**2
        c += val
    c /= len(list_of_numbers)
    return sqrt(c)

test_cases = [[7,14,9,21,32,15],[23,101,52,48,107],[10,40]]
for test in test_cases :
    print(f'Result for test case {test} :\n{STD(test)}') 