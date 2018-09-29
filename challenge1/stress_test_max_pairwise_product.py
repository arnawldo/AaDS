import random
from max_pairwise_product import max_pairwise_product_fast2, max_pairwise_product_naive

def generate_data(max_arr_len):
    n = random.randint(2, max_arr_len)
    a = [random.randint(0, 10) for _ in range(n)]

    return n, a

def run_stress_tests(max_iter=1000000, max_arr_len=9, log_step=None):
    for i in range(max_iter):
        n, a = generate_data(max_arr_len)
        naive_result = max_pairwise_product_naive(n, a)
        fast_result = max_pairwise_product_fast2(n, a)
        if naive_result == fast_result:
            print(f'Naive result: {naive_result} \n Fast_result: {fast_result}')
            print(f'n: {n} \n a: {a}')

        if log_step and i % log_step == 0:
            print(f'Iter: {i}')


if __name__ == '__main__':
    run_stress_tests(max_iter=20)
