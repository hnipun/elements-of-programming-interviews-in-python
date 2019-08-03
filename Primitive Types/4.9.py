import math


# my  answer
def check_palindrome(string):
    i = 0
    length = len(string) - 1
    while (i < len(string) / 2):
        if string[i] == string[length]:
            i = i + 1
            length = length - 1
        else:
            return False

    return True


# correct answer
def is_palindrome_number(x):
    if x < 0:
        return False
    if x == 0:
        return True

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False

        x %= msd_mask
        x //= 10
        msd_mask //= 100

    return True


# LeetCode answer
def IsPalindrome(x):
    # Special cases:
    # As discussed above, when x < 0, x is not a palindrome.
    # Also if the last digit of the number is 0, in order to be a palindrome,
    # the first digit of the number also needs to be 0.
    # Only 0 satisfy this property.
    if (x < 0 or (x % 10 == 0 and x != 0)):
        return False

    revertedNumber = 0
    while (x > revertedNumber):
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10

    # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
    print(revertedNumber)
    return x == revertedNumber or x == revertedNumber // 10


def reverse(x):
    reverse = 0
    x_remaining = abs(x)

    while (x_remaining):
        reverse = reverse * 10 + x_remaining % 10
        if (reverse > (2 ** 31 - 1)):
            return 0
        x_remaining //= 10

    return -reverse if x < 0 else reverse


def main():
    ''

if __name__ == "__main__":
    main()



