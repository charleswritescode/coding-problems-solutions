#!/usr/bin/python3

def get_missing_num(array):
    array.sort()

    missing_num = -1

    for num in array:
        if(num >= 0 ):
            previous_num = num-1
            next_num = num+1
            
            if(previous_num > 0 and previous_num not in array):
                missing_num = previous_num
                break
            elif(next_num not in array):
                missing_num = next_num
                break
    return missing_num


test_data = [
    {
        'array': [-1, 0, 1, 9, 3, 5, 8],
        'expected': 2
    },
    {
        'array': [3,4,-1,1],
        'expected': 2
    },
    {
        'array': [1,2,0],
        'expected': 3
    },
    {
        'array': [92,33,11,44,7,0,4,22,22,22,22],
        'expected': 1
    }
]

print("CODING PROBLEM 4: First missing positive integer")
for data in test_data:
    array = data['array']
    expected = data['expected']
    print("Array: {0}, Expected: {1}".format(array, expected), end=', ')
    result = get_missing_num(array)
    print("Result: {0}".format(result))
    assert result == expected
