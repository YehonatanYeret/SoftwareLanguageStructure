from functools import reduce

l = list(range(1, 1001))

l_odds = filter(lambda x: x % 2 != 0, l)
l_evens = filter(lambda x: x % 2 == 0, l)

# for each num append the last number (that already molted by the numbers before) mult by the
# current number, then its return None, so we do (or a) that return the list as the reduce function expected
cumulative_product = lambda lst, n: reduce(lambda a, x: a.append(a[-1] * x) or a, list(lst)[:n], [1])[1:]

# the func from ex1
func = lambda x: x / 2 + 2

# for each number, add the next number then add the current number
# by applying him the linear func. a[0] is the list that we will return and a[1] is the sum till now
linear_sum = lambda lst: reduce(lambda a, x: (a[0] + [x + func(a[1])], a[1] + x + func(a[1])), lst, ([], 0))[0]


def main():
    print(f"sum of the cumulative product on the evens: {sum(cumulative_product(l_evens, 100))}")
    print(f"sum of the linear sum on the odds: {sum(linear_sum(l_odds))}")


if __name__ == '__main__':
    main()
