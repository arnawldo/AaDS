# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

def max_pairwise_product(len_numbers, numbers):

    largest, second_largest = None, None

    if numbers[0] < numbers[1]:
        largest = numbers[1]
        second_largest = numbers[0]
    else:
        largest = numbers[0]
        second_largest = numbers[1]

    if len_numbers <= 2:
        return largest * second_largest
    
    for i, number in enumerate(numbers):
        if i < 2:
            continue
        if number > largest:
            second_largest = largest
            largest = number
            continue
        elif number > second_largest:
            second_largest = number

    return largest * second_largest

print(max_pairwise_product(n, a))