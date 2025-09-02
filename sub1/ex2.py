def sum_digit(n):
    fixed_n = n.strip()[1:] if n.strip().startswith("-") else n.strip() # Only 1 var is ok (the strip is cause in the tests the checker put " 21" and not just "21"..)
    if not fixed_n.isdigit():
        return "invalid input"
    return sum(map(int, list(fixed_n))) # sum every integer value of the chars that the string are made from


n = input("enter number\n")
print(sum_digit(n))
