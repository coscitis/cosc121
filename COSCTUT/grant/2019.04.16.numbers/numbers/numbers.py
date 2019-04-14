import os

"""
numbers.py, a collection of random Python questions to test your code skills.

Below are three functions that you are to write: parse_file,
number_of_nonlonely, and maths_is_gross.

Instructions for what to do for each
are described in the comments before each function.
"""

###############
# NOTE: There are automated tests at the end of the file -- click Run in Wing
#       to test your functions against the test data.
###############

"""
Write a function parse_file that reads a file (with the file name given by
the parameter "filename"), then returns a list of integer lists, with each
inner list representing a line of integers from the file. Don't forget to
close the file afterwards.

The file will contain one or more non-negative integers on each line,
separated by commas. For example, input.txt contains this:

1 4 7
3 0 1 0
8 0 6
1 1 2

Test code:
print(parse_file('input.txt'))

Output:
[[1, 4, 7], [3, 0, 1, 0], [8, 0, 6], [1, 1, 2]]

===
Hint: use a nested for loop, a list comprehension (preferred if you know it),
or the map() function to convert the strings to integers after using
str.split().
"""
def parse_file(filename):
    """Parses a file."""
    # replace "pass" with your code
    pass

"""
A non-lonely integer is any integer that is not equal to 1 (e.g. 0, 2, -5...)

With the list of integer lists (in the same format as the output of the
parse_file function) as the input, write a function
number_of_nonlonely(numbers) that returns a list containing the number of
non-lonely numbers in each of the inner lists.

(Note: as with parse_file, it is guaranteed that there will be one or more
integers, all non-negative, in each inner list. There is no guarantee for the
number of inner lists.)

However, there is a catch: if the number 0 is present in the inner list (i.e.
occurs one or more times), you must flip the sign (multiply by -1) of the
number of non-lonely numbers once.

Test code:
numbers = [[1, 4, 7], [3, 0, 1, 0], [8, 0, 6], [1, 1, 2]]
print(number_of_nonlonely(numbers))

Output:
[2, -3, -3, 1]
"""
def number_of_nonlonely(numbers):
    """Returns a list containing the number of non-lonely numbers in each
    inner list."""
    # replace "pass" with your code
    pass

"""
With a list of zero or more three-integer lists as input, write a function
maths_is_gross(numbers, filename) that, for each three-integer list:
- finds the largest two numbers and adds them together, then
- divides that by the smallest number, then
- if the division does not cause an error due to dividing by zero, outputs the
  result *to a file* in its own line, to 2 decimal places.
- if the division does cause an error, output the word "error" to the file, in
  its own line.

For the purposes of this question, you must use "try" and "except" to check for
dividing by zero, from lab 7 "Exceptions", and not an "if" statement.

Test code:
numbers = [[5, 10, 15], [-12, 15, 2], [-5, 0, 10], [0, 2, 4]]
maths_is_gross(numbers, 'numbers_out.txt')

Output (in numbers_out.txt):
5.00
-1.42
-2.00
error

Note: do not modify the numbers list if you choose to sort anything --
      instead, create a new copy of the list that is sorted by using the
      sorted() function
      (see https://docs.python.org/3/howto/sorting.html for a guide)
"""
def maths_is_gross(numbers, filename):
    """Roses are red,
    violets are blue,
    nobody likes maths,
    but it's gonna be in the exam."""
    # replace "pass" with your code
    pass

###############
###############
# Checks functions to see if they return the right output; this should test
# your functions automatically when you run your python file.

def check():
    # please don't actually run your tests like this... if you're ever testing
    # more substantial programs in python, use a real test framework like
    # pytest: https://docs.pytest.org/en/latest/

    passed = True
    tests = {
        parse_file: [
            [ 'input.txt', [[1,4,7],[3,0,1,0],[8,0,6],[1,1,2]] ],
            [ 'input2.txt', [[1,1,1],[0,0],[1],[2,2,2],[1,0,1],[0,1,0],[100,100,100,100],[0,100,0]] ],
            [ 'input3.txt', [[1,307,72,3,0,74],[37,79],[3],[0],[34,777,30,1],[10],[74,10,0,4],[1,1,1,1,1],[2,2,2,2,1,1,1,1,0,2],[0,0,0,0,0,0,1],[0,0,0],[999,9,9,9,999]] ],
            [ 'input4.txt', [[0]] ],
            [ 'input5.txt', [[1],[2],[3],[4],[5],[6],[7],[8]] ],
            [ 'input6.txt', [] ],
        ],
        number_of_nonlonely: [
            [ [[1,4,7],[3,0,1,0],[8,0,6],[1,1,2]], [2,-3,-3,1] ],
            [ [[100,50,192,382,472,18,27,47,19,10,28],[29,10,1,48,5,1,29],[1]], [11,5,0] ],
            [ [[1,1,1,1,1],[0,0,0],[1,0,1],[0,0]], [0,-3,-1,-2] ],
            [ [[0],[0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0]], [-1,-2,-3,-4,-5] ],
            [ [[1,2,3]], [2] ],
            [ [], [] ],
        ],
    }
    for func in tests:
        for (i, test) in enumerate(tests[func]):
            print(f'--> Testing test {i + 1} in function {func.__name__}...', end='')
            output = func(test[0])
            if output == test[1]:
                print(' (passed)')
            else:
                passed = False
                print(f'\nError: Test "{test[0]}" failed in function {func.__name__}')
                print(f'Expected "{test[1]}", got "{output}".')
            print()
        print()

    tests_maths = [
        ([[5,10,15],[-12,15,2],[-5,0,10],[0,2,4]], 'tmp/numbers_out.txt', 'numbers.txt'),
        ([[0,0,0],[1,1,1],[2,2,2],[3,3,3],[-5,-20,-49],[-1,-1,-1],[-2,-3,-4],[0,-1019,-1029],[1,0,-1],[-20000,-20000,0],[-1,1,-1]], 'tmp/numbers2_out.txt', 'numbers2.txt'),
        ([], 'tmp/numbers3_out.txt', 'numbers3.txt'),
        ([[1,2,3]], 'tmp/numbers4_out.txt', 'numbers4.txt'),
        ([[1928758,192837273829,3],[9784,2861,392],[192,28,9]], 'tmp/numbers5_out.txt', 'numbers5.txt'),
    ]
    for (i, test) in enumerate(tests_maths):
        maths_is_gross(test[0], test[1])
        try:
            print(f'--> Testing test {i + 1} in function {func.__name__}...', end='')
            with open(test[1]) as result, open(test[2]) as expected:
                result_contents = result.read()
                expected_contents = expected.read()
                if result_contents == expected_contents:
                    print(' (passed)')
                else:
                    print(f'\nError: Test "{test[0]}" failed in function maths_is_gross')
                    print('Expected:')
                    print(expected_contents)
                    print('Got:')
                    print(result_contents)
                    passed = False
            # delete output file afterwards
            os.remove(test[1])
            print()
        except FileNotFoundError:
            print(f'\nError: could not find file {test[1]}.')
            print()
    print('======')
    if passed:
        print('Your functions passed all of the test cases. Congratulations!')
    else:
        print('There were some problems; see above.')

check()
