import time
from functools import reduce

func = lambda x: x / 2 + 2

l = list(range(10001))

l_func = list(map(func, l))

# functional
start = time.time()
sum_functional = reduce(lambda a, b: a + b, l_func, 0)
end = time.time()
print(f"functional sum: {sum_functional}\nfunctional time: {end - start}")

# imperative
start = time.time()
sum_imperative = 0
for i in l_func:
    sum_imperative += i
end = time.time()
print(f"imperative sum: {sum_imperative}\nimperative time: {end - start}")

# in 1 func - the lambda and summing
func_and_sum = reduce(lambda a, b: a + func(b), l, 0)
print(func_and_sum)
