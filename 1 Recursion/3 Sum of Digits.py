# How to find the sum of digits of a positive integer number using recursion?

"""
Steps
    1 Recursive Case
    2 Stopping Criteria
    3 Unintentional case

1 To separate the digits by dividing by 10
     555 /10 = 55, rest 5*
     55 /10  = 5, rest 5*
      5 /10  = 0, rest 5*
        Get the rests. To sum the rests.

2 Stopping Criteria: When the division results in 0

3 integers and positive numbers only

"""


def sum(k):
    assert k >=0 and int(k) == k, 'integers and positive numbers only'
    g = k / 10
    h = k % 10
    if g == 0:
        return k
    else:
        return h + sum(int(g))


print(sum(1111))
print(sum(40))
print(sum(136))


# Solution
def sumOfDigits(n):
    assert 0 <= n == int(n), 'integers and positive numbers only'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))


print(sumOfDigits(50))
print(sumOfDigits(11))
print(sumOfDigits(1236))
