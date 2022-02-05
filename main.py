# main.py
import math

import queues
import queues_utilities

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# github - https://www.jetbrains.com/help/pycharm/github.html#register-account
# https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#share-on-GitHub
# docstrings - click function, alt+enter, insert a documentation string stub

# test sheet
# https://upedu.sharepoint.com/:x:/r/sites/GRP-Python-22/_layouts/15/Doc.aspx?sourcedoc=%7B5C6DEF46-23C0-4E95-8D91-3E87D403AA9B%7D&file=example%20just%20values.xlsx&action=default&mobileredirect=true


# queues_tests.py - Python program you wrote to verify that your functions (from queues.py) satisfy the requirements and function correctly
# queues.py – Each of the following functions (as described for Project 1) should be implemented in your queues.py:

# is_valid( lamda, mu, c=1)
# is_feasible(lamda1, mu, c=1)
# calc_p0(lamda, mu, c=1)
# calc_lq_mmc(lamda, mu, c=1)
# calc_bk_mmc(k, lamda, mu, c=1)
# calc_wqk_mmc(k, lamda, mu, c=1)
# calc_lqk_mmc(k, lamda, wqk, c=1)
# use_littles_law(lamda, mu, c=1, **kwargs)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # im going to do this


    # do this




# steps: create function, define test cases, loop cases,

# test_is_valid( lamda, mu, c=1)
# test_is_feasible(lamda1, mu, c=1)
# test_calc_p0(lamda, mu, c=1)
# test_calc_lq_mmc(lamda, mu, c=1)
# test_calc_bk_mmc(k, lamda, mu, c=1)
# test_calc_wqk_mmc(k, lamda, mu, c=1)
# test_calc_lqk_mmc(k, lamda, wqk, c=1)
# test_use_littles_law(lamda, mu, c=1, **kwargs)

# TODO find a way to confirm each test passes
# TODO loop through array of tests, send should log parameter,
# todo add descriptions to docstring

def test_calc_lamda_agg():
    func_name = "test_calc_lamda_agg"
    print('------------------------')
    print(f'TESTING {func_name} ')
    print('------------------------')
    print()


    # define test cases
    test_cases = (
        {'lamda': 6, 'expected_result': 6, 'test_case': 'lamda scalar 5'},
        {'lamda': (5,10,5), 'expected_result': 20, 'test_case': 'lamda tuple 20'},
    )

    did_pass = True
    failed_test = ""

    for args in test_cases:
        test_case = args['test_case']
        expected_result = args['expected_result']
        print(f'test case: {test_case}')
        case_return = queues_utilities.calc_lamda_agg(args['lamda'])
        print(f'expected result: {expected_result}')
        if (case_return != expected_result):
            failed_test = test_case
            did_pass = False
        print()

    print(f'-- DID "{func_name}" PASS: ** {did_pass} **')
    if (did_pass == False):
        print(f'Failed Test: {failed_test}')

    print()



def test_is_valid():
    func_name = "is_valid"
    print('------------------------')
    print(f'TESTING {func_name} ')
    print('------------------------')
    print()

    # TEST CASES
    # lamda scalar valid
    # lamda scalar invalid
    # lamda tuple valid
    # lamda tuple invalid
    # mu valid
    # mu invalid
    # c valid
    # c invalid

    # fixme - fewer tests: success, fail cases

    # define test cases
    test_cases = (
        {'lamda': 6, 'mu': 25, 'c': 1, 'expected_result': True, 'test_case': 'lamda scalar valid'},
        {'lamda': 0, 'mu': 25, 'c': 1, 'expected_result': False, 'test_case': 'lamda scalar invalid'},
        {'lamda': (5,10,5), 'mu': 25, 'c': 1, 'expected_result': True, 'test_case': 'lamda tuple valid'},
        {'lamda': (5,0,5), 'mu': 25, 'c': 1, 'expected_result': False, 'test_case': 'lamda tuple invalid'},
        {'lamda': (5,10,5), 'mu': 25, 'c': 1, 'expected_result': True, 'test_case': 'mu valid'},
        {'lamda': (5,10,5), 'mu': 0, 'c': 1, 'expected_result': False, 'test_case': 'mu invalid'},
        {'lamda': (5,10,5), 'mu': 25, 'c': 1, 'expected_result': True, 'test_case': 'c valid'},
        {'lamda': (5,10,5), 'mu': 25, 'c': 0, 'expected_result': False, 'test_case': 'c invalid'},
        {'lamda': (5,10,5), 'mu': 0, 'c': 0, 'expected_result': False, 'test_case': 'mu & c invalid'},
        {'lamda': (5,10,5), 'mu': 'mu', 'c': 0, 'expected_result': False, 'test_case': 'mu non numeric'},
    )

    did_pass = True
    failed_test = ""

    for args in test_cases:
        test_case = args['test_case']
        expected_result = args['expected_result']
        print(f'test case: {test_case}')
        case_return = queues.is_valid(args['lamda'], args['mu'], args['c'])
        print(f'expected result: {expected_result}')

        print(f'case_return: {case_return}')
        print()

        if (case_return != expected_result):
            failed_test = test_case
            did_pass = False
        print()

    print(f'-- DID "{func_name}" PASS: ** {did_pass} **')
    if (did_pass == False):
        print(f'Failed Test: {failed_test}')

    print()


def test_is_feasible():
    func_name = "test_is_feasible"
    print('------------------------')
    print(f'TESTING {func_name} ')
    print('------------------------')
    print()

    # define test cases
    test_cases = (
        {'lamda': (5,10,5), 'mu': 25, 'c': 1, 'expected_result': True, 'test_case': 'success case true'},
        {'lamda': (5,0,5), 'mu': 25, 'c': 1, 'expected_result': False, 'test_case': 'is_valid false'},
        {'lamda': 20, 'mu': 25, 'c': 1, 'expected_result': True, 'test_case': 'lamda scalar true'},
        {'lamda': (5,10,5), 'mu': 19, 'c': 1, 'expected_result': False, 'test_case': 'rho false'},
    )

    did_pass = True
    failed_test = ""

    for args in test_cases:
        test_case = args['test_case']
        expected_result = args['expected_result']
        print(f'test case: {test_case}')
        case_return = queues.is_feasible(args['lamda'], args['mu'], args['c'])
        print(f'expected result: {expected_result}')
        if (case_return != expected_result):
            failed_test = test_case
            did_pass = False
        print()

    print(f'-- DID "{func_name}" PASS: ** {did_pass} **')
    if (did_pass == False):
        print(f'Failed Test: {failed_test}')

    print()


def test_calc_p0():
    func_name = "test_calc_p0"
    print('------------------------')
    print(f'TESTING {func_name} ')
    print('------------------------')
    print()

    # fixme in testing p0 = 0.19999999999999996, use is close
    # define test cases
    test_cases = (
        {'lamda': (5,0,5), 'mu': 25, 'c': 1, 'expected_result': False, 'test_case': 'is_valid false'},
        {'lamda': (5,10,5), 'mu': 19, 'c': 1, 'expected_result': False, 'test_case': 'is_feasible false'},
        {'lamda': (5,10,5), 'mu': 25, 'c': 1, 'expected_result': 0.2, 'test_case': 'c <= 1'},
        {'lamda': (5,10,5), 'mu': 25, 'c': 3, 'expected_result': 4, 'test_case': 'c > 1'},
    )

    did_pass = True
    failed_test = ""

    for args in test_cases:
        test_case = args['test_case']
        expected_result = args['expected_result']
        print(f'TEST CASE: {test_case}')
        print('-')
        case_return = queues.calc_p0(args['lamda'], args['mu'], args['c'])
        print('-')
        print(f'expected result: {expected_result}')

        print(f'is instance: {isinstance(expected_result, bool)}')
        print(f'case_return: {case_return}')
        print()

        if (isinstance(expected_result, bool)):
            if (case_return != expected_result):
                failed_test = test_case
                did_pass = False
                break
        else:
            if (math.isclose(case_return, expected_result) == False):
                failed_test = test_case
                did_pass = False
                break

    print('------------------------')
    print(f'-- DID "{func_name}" PASS: ** {did_pass} **')
    if (did_pass == False):
        print(f'Failed Test: {failed_test}')

    print()

def test_calc_lq_mmc():
    func_name = "test_calc_lq_mmc"
    print('------------------------')
    print(f'TESTING {func_name} ')
    print('------------------------')
    print()

    # define test cases
    test_cases = (
        {'lamda': (5, 0, 5), 'mu': 25, 'c': 1, 'expected_result': False, 'test_case': 'is_valid false'},
        {'lamda': (5, 10, 5), 'mu': 19, 'c': 1, 'expected_result': False, 'test_case': 'is_feasible false'},
        {'lamda': (5, 10, 5), 'mu': 25, 'c': 1, 'expected_result': 3.2, 'test_case': 'c = 1'},
        {'lamda': (5, 10, 5), 'mu': 25, 'c': 2, 'expected_result': 5, 'test_case': 'c > 1'},
    )

    did_pass = True
    failed_test = ""

    for args in test_cases:
        test_case = args['test_case']
        expected_result = args['expected_result']
        print(f'test case: {test_case}')
        print('-')
        case_return = queues.calc_lq_mmc(args['lamda'], args['mu'], args['c'])
        print('-')
        print(f'expected result: {expected_result}')
        print()
        if (case_return != expected_result):
            failed_test = test_case
            did_pass = False
            break

    print('------------------------')
    print(f'-- DID "{func_name}" PASS: ** {did_pass} **')
    if (did_pass == False):
        print(f'Failed Test: {failed_test}')
        print(f'!! ( Expected: {expected_result}, returned: {case_return} ) !!')

    print()












#
#
# # loop through test cases
#
# def init_tests(test_case = 1):
#
#     print()
#
#     if test_case == 1:
#         # test case #1
#         print('------------------------')
#         print('TEST CASE #1')
#         print('------------------------')
#         print()
#
#         lamda = (5,10,5)
#         mu = 25
#         c = 1
#
#         print('ARGUMENTS:')
#         print(f'lamda: {lamda} ,mu: {mu}, c: {c}')
#         print()
#
#         # check validity
#         queue_valid = queues.is_valid(lamda, mu, c)
#         print(f'queue_valid: {queue_valid}')
#
#         print()
#
#         # calc lamda_agg
#         queues_utilities.calc_lamda_agg(lamda)
#
#
#
#     print()
#     print(f'------ End Case {test_case} ------')
#
# init_tests()
# print()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    # RUN TESTS

    print()

    run_test_calc_lamda_agg = 0
    run_test_validity = 0
    run_test_feasibility = 0
    run_test_p0 = 1
    run_test_lq = 0

    if (run_test_lq == 1):
        test_calc_lq_mmc()

    if (run_test_p0 == 1):
        test_calc_p0()

    if (run_test_feasibility == 1):
        test_is_feasible()

    if (run_test_validity == 1):
        test_is_valid()

    if (run_test_calc_lamda_agg == 1):
        test_calc_lamda_agg()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
