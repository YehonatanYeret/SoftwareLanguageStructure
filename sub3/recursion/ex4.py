from tail_recurse import tail_call_optimized


# Check if the first and last are the same and the rest of the number is a palindrome
def isPalindrome(n):
    if len(n) <= 1:
        return True
    return isPalindrome(n[1:-1]) and n[0] == n[-1]


# If 1 peace is no palindrome - return False, otherwise - if we check all the chars return True
@tail_call_optimized
def isPalindrome_tail(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return isPalindrome_tail(n[1:-1])


def main():
    # print(isPalindrome("1" * 10000))
    print(isPalindrome_tail("1" * 10000))


if __name__ == '__main__':
    main()
