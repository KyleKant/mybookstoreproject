# print a tree
import re
import random
import sys
from time import time


def show_tree():
    tree = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]
    # 1 iterate over tree
    # if 0 -> print ''
    # if 1 -> print *
    fill = '*'
    empty = ' '
    new_line = ''
    for col in tree:
        for row in col:
            if row:
                print(fill, end='')
            else:
                print(empty, end='')
        print(new_line)

# Check for duplicates in list.


def check_duplicate_list():
    some_list = ['a', 'b', 'a', 'c', 'd', 'e', 'd',
                 'n', 'c', 's', 'g', 'c', 's', 'g', 'a']
    # some_list = ['a', 'b', 'a', 'c', 'a', 'a', 'c']
    # print items duplicated
    duplicated_list = []
    for item in some_list:
        if some_list.count(item) > 1:
            if item not in duplicated_list:
                duplicated_list.append(item)
    print(duplicated_list)

# Find highest even number


def highest_even(li):
    even_list = []
    for number in li:
        if number % 2 == 0:
            even_list.append(number)
    return max(even_list)


# print(highest_even([1, 19, 20, 2, 4, 8, 17, 24, 12, 56, 3, 45, 38, 69, 94]))


# class SuperList(list):
#     def __len__(self):
#         return super().__len__()


# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(3)
# print(super_list1)
# print(len(super_list1))

# # Order a list by the second item in a tuple of the list
# my_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
# my_list.sort(key=lambda item: item[1])
# print(my_list)

# # create list, dict, set by comprehension.
# my_list = [num ** 2 for num in range(0, 10)]
# my_list2 = [num for num in my_list if num % 2 == 0]
# print(my_list)
# print(my_list2)

# my_set = {num for num in [1, 1, 2, 3, 4, 1, 2, 5, 4, 5, 2, 6, 3]}
# print(my_set)

# my_dict = {key: value ** 2 for key, value in enumerate(range(0, 10))}
# my_dict2 = {key: value for key,
#             value in my_dict.items() if value % 2 == 0}
# my_dict3 = {num: num*3 for num in range(0, 10)}
# print(my_dict)
# print(my_dict2)
# print(my_dict3)

# # Check for duplicates in list by comprehension
# test_list = ['a', 'b', 'a', 'c', 'd', 'e', 'd',
#              'n', 'c', 's', 'g', 'c', 's', 'g', 'a']
# duplicates = list(set([duplicate_item for duplicate_item in test_list if test_list.count(
#     duplicate_item) > 1]))
# print(duplicates)

# # Decorator pattern
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrap_func


# @ my_decorator
# def hello(greeting, emoji):
#     print(greeting, emoji)


# hello('hello', ':)')

# Create a function to check the run time of a function that other
def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}s to run function')
        return result
    return wrap_func


@performance
def long_time():
    for item in range(1000000):
        item * 2


# long_time()

# # Error handling
# while True:
#     try:
#         age = int(input("What is your age?"))
#         print(age)
#     except ValueError:
#         print("Please enter your age")
#     except ZeroDivisionError:
#         print("Please enter your age that bigger than 0")
#     else:
#         print("Thank you!")
#         break

def total(*args):
    try:
        total = 0
        for num in args:
            total += num
        return total
    except (TypeError, ValueError) as err:
        print(err)
    else:
        print("Thank you")
    finally:
        print("Finally, we done.")

    # end try
# print(total(1, 2, 3, 4, 5))


# # Generators
# def generator_func(num):
#     for item in range(num):
#         yield item


# def new_list(li):
#     new_list = []
#     for num in generator_func(li):
#         new_list.append(num)
#     return new_list


# new_list = new_list(100000)
# print(new_list)


# # Under the hood of Generators
# class Generator():
#     current = 0

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if Generator.current < self.last:
#             num = Generator.current
#             Generator.current += 1
#             return num
#         raise StopIteration


# ge = Generator(0, 1000000)
# my_list = []
# for item in ge:
#     my_list.append(item)
# print(my_list)

# # Fibonacci Numbers by using list
# def fib(number: int):
#     fib = []
#     for item in range(0, number + 1):
#         if item < 2:
#             fib.append(item)
#         else:
#             fib.append(fib[item - 1] + fib[item - 2])
#     return fib


# print(fib(30))

# #  Fibonacci Numbers by using Generator


# class Fibonacci_generator():
#     current = 0
#     previous = 0
#     pre_previous = 0

#     def __init__(self, first, last) -> None:
#         self.first = first
#         self.last = last
#         pass

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if Fibonacci_generator.current <= self.last:
#             if Fibonacci_generator.current < 2:
#                 num = Fibonacci_generator.current
#                 if num == 0:
#                     Fibonacci_generator.pre_previous = num
#                 elif num == 1:
#                     Fibonacci_generator.previous = num
#             else:
#                 num = Fibonacci_generator.pre_previous + Fibonacci_generator.previous
#                 Fibonacci_generator.pre_previous = Fibonacci_generator.previous
#                 Fibonacci_generator.previous = num
#             Fibonacci_generator.current += 1
#             return num
#         raise StopIteration


# fi = Fibonacci_generator(0, 30)
# li = []
# for item in fi:
#     li.append(item)

# print(li)


# # Create Fibonacci Numbers by using Generator with yield
# def fib_gen(number: int):
#     fib_number = 0
#     pre_num = 0
#     pre_pre_num = 0
#     for num in range(0, number + 1):
#         if num < 2:
#             fib_number = num
#             if num == 0:
#                 pre_pre_num = num
#             elif num == 1:
#                 pre_num = num
#         else:
#             fib_number = pre_pre_num + pre_num
#             pre_pre_num = pre_num
#             pre_num = fib_number
#         yield fib_number


# fib_nums = []
# for fib_num in fib_gen(30):
#     fib_nums.append(fib_num)
# print(fib_nums)
# first_arg = sys.argv[1]
# last_arg = sys.argv[2]
# ran_num = random.randint(first_arg, last_arg)
# print(first_arg, last_arg)
# input('What your answer?')
# print(f'random number {ran_num}')
# Game guess a number
def GuessNumber(first: int, last: int):
    random_number = random.randint(first, last)
    while True:
        try:
            answer = int(
                input(f'Please enter a number from {first} to {last}: '))
            if answer >= first and answer <= last:
                if answer == random_number:
                    print("You a genius")
                    break
                else:
                    continue
        except ValueError as err:
            print(f'Please enter a number')

        # end try
# GuessNumber(1, 2)
# Email, Password Validation


def user_validate(email: str, password: str):
    email_pattern = re.compile()
