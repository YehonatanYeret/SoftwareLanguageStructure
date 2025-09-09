def power_function(n):
    def est(x):
        return x ** n

    return est

power_of_2 = power_function(2)
