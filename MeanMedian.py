# here we will write teo function
# one which will calculate the median and the mean of a list of numbers
# just a small revision of python functions
def _median(*numbers):
    n = len(numbers)
    median = 0
    if n % 2 == 0:
        #         if the length of the numbers is even
        median = (numbers[n // 2] + numbers[(n // 2) + 1-2]) / 2
    else:
        median = numbers[((n + 1) // 2)-1]
    print('the median of the list of numbers', median)


def _mean(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print('the mean of the list of numbers', sum / len(numbers))


_median(4, 5, 9, 10, 11, 20, 24, 56, 67)
_mean(4, 5, 9, 10, 11, 20, 24, 56, 67)
