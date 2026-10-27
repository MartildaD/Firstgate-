def reverse_array(array):
    for index in range(len(array)):
        first = 0
        second = len(array[index]) - 1
    
        while first < second:
            old = array[index][first]
            array[index][first] = array[index][second]
            array[index][second] = old
            first += 1 
            second -= 1
    return array
input_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
print(reverse_array(input_array))





