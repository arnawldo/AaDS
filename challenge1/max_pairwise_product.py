# Uses python3

def max_pairwise_product_naive(len_numbers, numbers):
    
    product = 0

    for i in range(len_numbers):
       for j in range(i + 1, len_numbers):
           product = max(product, numbers[i] * numbers[j])
    
    return product

def max_pairwise_product_fast(len_numbers, numbers):
    largest, second_largest = -1, -1

    for number in numbers:
        if number > largest:
            largest, second_largest = number, largest
        elif number > second_largest:
            second_largest = number

    product = largest * second_largest

    return product

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)
    print(max_pairwise_product_fast(n, a))
