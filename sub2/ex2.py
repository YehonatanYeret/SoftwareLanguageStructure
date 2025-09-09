from functools import reduce

l = list(range(1, 1001))

l_odds = filter(lambda x: x % 2 != 0, l)
l_evens = filter(lambda x: x % 2 == 0, l)

# for each num append the last number (that already molted by the numbers before) mult by the
# current number, then its return None, so we do (or a) that return the list as the reduce function expected
cumulative_product = lambda lst, n: reduce(lambda a, x: a.append(a[-1] * x) or a, lst, [n])[1:]


# the func from ex1
func = lambda x: x / 2 + 2

# for each number add the last number (that is the sum till then) added with the number
# by applying him the linear func
linear_sum = lambda lst: reduce(lambda a, x: a.append(a[-1] + func(x)) or a, lst, [0])[1:]

print(f"sum of the cumulative product on the evens {sum(cumulative_product(l_evens, 1))}")
print(f"sum of the linear sum on the odds {sum(linear_sum(l_odds))}")
