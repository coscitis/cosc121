# Challenge:
# The function weirdo(a, b) takes two integers as its parameters and returns
# another, mysterious integer.
#
# Rewrite this function so it only requires one line of code (the return
# statement) in the function your_weirdo(a, b), which has been started for you.
# It must return exactly the same output as weirdo(a, b) for *any* integer
# values of a and b.
#
# Hint: for each line, figure out what the values of a, b, and c are relative
#       to what a and b equal at the very beginning of the function.

def weirdo(a, b):
    """Does the weirdest of things..."""
    c = b - 10
    b = a + 10
    a = b * 2
    c = b * a
    b = a + 2
    (a, b) = (b, a) # swaps the two around
    a = a - b
    c = c // a
    return c

# Type your rewrite of weirdo(a, b) here.
def your_weirdo(a, b):
    """Still does the weirdest of things..."""
    return ??????

###############
###############
# The code below is to check your answer when you run this file, and can be safely ignored.

class WrongAnswerError(Exception):
    """Custom error for checking the weirdo function."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

def check():
    """Checks if your_weirdo(a, b) is correct with weirdo(a, b)."""
    try:
        for a in range(-200, 201):
            for b in range(-200, 201):
                if weirdo(a, b) != your_weirdo(a, b):
                    raise WrongAnswerError(a, b)

        more_tests = [(743270125, -10741270), (10000000000,10000000000)]
        for (a, b) in more_tests:
            if weirdo(a, b) != your_weirdo(a, b):
                raise WrongAnswerError(a, b)

        print('Passed! Congratulations :)')

    except WrongAnswerError as e:
        print('WrongAnswerError:')
        print('Values for {} and {} don\'t match!'.format(e.a, e.b))
        print('Got', your_weirdo(e.a, e.b), 'but expected', weirdo(a, e.b))

check()
