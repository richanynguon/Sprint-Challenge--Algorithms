'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

Inside the `recursive_count_th` directory you'll find the `count_th.py` file. In this file, please add your recursive implementation to the `count_th()` method following these rules:

* Your function should take in a signle parameter (a string `word`)
* Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
* Your function must utilize recursion. 
  * It cannot contain any loops.

Run `python test_count_th.py` to run the tests for your `count_th()` function to ensure that your implementation is correct.
'''


def count_th(word):
    # count how many lower case th are in a word - in python a string is basically an arr
    # must use recursion
    count = 0
    # edge case - there is not th in the word
    if 'th' not in word: #o(N)
        return count
    # if find a th will need to continue in the search for the next th until word is over
    # using recursive method will have to use a different way to mark ths' as found so
    # it doesnt recount 
    else:
        #string.replace(old, new, count)
        count += 1 + count_th(word.replace('th', ' ', 1))
        return count
